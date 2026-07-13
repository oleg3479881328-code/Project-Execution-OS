from __future__ import annotations


class TusyaBotError(Exception):
    """Base project error."""


class UnauthorizedChatError(TusyaBotError):
    """Raised when an update comes from a non-owner chat."""


class DuplicateResourceError(TusyaBotError):
    """Raised when a canonical resource already exists."""


class DuplicateKeywordError(TusyaBotError):
    """Raised when a normalized keyword already exists."""


class NotFoundError(TusyaBotError):
    """Raised when a repository entity cannot be found."""
