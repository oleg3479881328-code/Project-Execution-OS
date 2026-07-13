from __future__ import annotations

from pathlib import Path

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    telegram_bot_token: SecretStr
    owner_telegram_chat_id: int

    deepseek_api_key: SecretStr
    deepseek_base_url: str = "https://api.deepseek.com"
    deepseek_model: str = "deepseek-v4-flash"
    deepseek_timeout_seconds: float = Field(default=30.0, ge=5.0, le=120.0)

    database_path: Path = Path("data/tusya.sqlite3")
    poll_interval_seconds: int = Field(default=300, ge=60, le=86_400)
    reddit_user_agent: str = "tusya-reddit-monitor/0.1 by owner"
    reddit_timeout_seconds: float = Field(default=20.0, ge=5.0, le=120.0)
    log_level: str = "INFO"
    backup_dir: Path = Path("backups")

    @field_validator("deepseek_base_url")
    @classmethod
    def normalize_base_url(cls, value: str) -> str:
        return value.rstrip("/")

    @field_validator("log_level")
    @classmethod
    def normalize_log_level(cls, value: str) -> str:
        return value.upper()

    @field_validator("owner_telegram_chat_id")
    @classmethod
    def validate_owner_chat_id(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("OWNER_TELEGRAM_CHAT_ID must be a positive integer")
        return value

    @field_validator("database_path")
    @classmethod
    def validate_database_path(cls, value: Path) -> Path:
        if not value.suffix:
            raise ValueError("DATABASE_PATH must include a file name")
        return value

    @field_validator("telegram_bot_token")
    @classmethod
    def validate_telegram_token(cls, value: SecretStr) -> SecretStr:
        token = value.get_secret_value().strip()
        if ":" not in token or len(token) < 10:
            raise ValueError("TELEGRAM_BOT_TOKEN does not look valid")
        return value

    @field_validator("deepseek_api_key")
    @classmethod
    def validate_deepseek_key(cls, value: SecretStr) -> SecretStr:
        token = value.get_secret_value().strip()
        if len(token) < 10:
            raise ValueError("DEEPSEEK_API_KEY does not look valid")
        return value

    def prepare_directories(self) -> None:
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        Path("logs").mkdir(parents=True, exist_ok=True)
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def runtime_diagnostics(self) -> dict[str, str | int]:
        return {
            "database_path": str(self.database_path),
            "backup_dir": str(self.backup_dir),
            "poll_interval_seconds": self.poll_interval_seconds,
            "reddit_user_agent": self.reddit_user_agent,
            "reddit_timeout_seconds": int(self.reddit_timeout_seconds),
            "deepseek_base_url": self.deepseek_base_url,
            "deepseek_model": self.deepseek_model,
            "deepseek_timeout_seconds": int(self.deepseek_timeout_seconds),
            "owner_telegram_chat_id": self.owner_telegram_chat_id,
            "log_level": self.log_level,
        }
