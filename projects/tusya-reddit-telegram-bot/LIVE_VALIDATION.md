# LIVE_VALIDATION

Perform these steps only when server-side secrets are available. Do not paste real secret values into GitHub, chat, or repository files.

## 1. Create Telegram Bot

1. Create the bot with BotFather.
2. Save the token only in deployment environment secrets.
3. Send one message to the bot from the owner Telegram account.

## 2. Obtain Owner Chat ID

1. Read the chat ID from your trusted Telegram method.
2. Store it as `OWNER_TELEGRAM_CHAT_ID` in deployment environment.

## 3. Add Secrets

Set these server-side only:

- `TELEGRAM_BOT_TOKEN`
- `OWNER_TELEGRAM_CHAT_ID`
- `DEEPSEEK_API_KEY`
- `DEEPSEEK_BASE_URL`
- `DEEPSEEK_MODEL`
- `DEEPSEEK_TIMEOUT_SECONDS`
- `DATABASE_PATH`
- `BACKUP_DIR`
- `POLL_INTERVAL_SECONDS`
- `REDDIT_USER_AGENT`
- `REDDIT_TIMEOUT_SECONDS`
- `LOG_LEVEL`

## 4. Start Deployment

1. Build the image or run compose.
2. Confirm the healthcheck passes.
3. Inspect logs for non-secret startup diagnostics only.

## 5. Verify Owner Authorization

1. Send `/start` from the owner chat.
2. Confirm the menu appears.
3. Send `/start` from a different Telegram user.
4. Confirm the response is `Access denied.`

## 6. Add Resource And Keyword

1. Add `https://www.reddit.com/r/WedditNYC/new/`
2. Add keyword `photography`
3. Run `/status`

## 7. Verify Baseline

1. Run `/check_now`
2. Confirm no old posts are delivered from the first baseline pass.

## 8. Verify Controlled New Post Notification

1. Wait for a controlled new matching Reddit post or use a safe known fixture post.
2. Run `Check now` or wait for scheduler.
3. Confirm exactly one Telegram notification card arrives.

## 9. Verify Post View And Links

1. Tap `📖 Открыть в боте`
2. Confirm full post text is visible and long text is split safely.
3. Tap `🔗 Открыть Reddit`
4. Confirm the link is clickable and correct.

## 10. Verify DeepSeek Draft Flow

1. Tap `✍️ Создать черновик`
2. Confirm the response is visibly labeled `Черновик`.
3. Tap `🔁 Регенерировать`
4. Confirm a new revision appears.
5. Tap `🛠 Уточнить`
6. Send a short instruction and confirm a refined saved draft appears.

## 11. Verify Restart Persistence

1. Stop the container or process.
2. Start it again.
3. Confirm resources, keywords, feed state, draft settings, and saved drafts remain.

## 12. Verify Unauthorized User Denial

1. Trigger commands and callbacks from a non-owner Telegram account.
2. Confirm access is denied and no protected state is exposed.

## 13. Verify No Reddit Publishing

1. Search the code and runtime behavior for any Reddit post/reply submission path.
2. Confirm none exists.
