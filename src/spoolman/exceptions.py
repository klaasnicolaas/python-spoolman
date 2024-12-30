"""Asynchronous Python client for Spoolman."""


class SpoolmanError(Exception):
    """Base class for Spoolman exceptions."""


class SpoolmanConnectionError(SpoolmanError):
    """Error raised when connection to the API fails."""


class SpoolmanResponseError(SpoolmanError):
    """Error raised when the API returns a error."""

    def __init__(self, data: dict[str, str], code: int) -> None:
        """Initialize the exception."""
        super().__init__(f'{data["message"]} (code: {code})')
