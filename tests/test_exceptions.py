"""Test exceptions for Spoolman."""

# pylint: disable=protected-access
from __future__ import annotations

from unittest.mock import patch

import pytest
from aiohttp import ClientError, ClientSession
from aresponses import ResponsesMockServer

from spoolman import Spoolman
from spoolman.exceptions import (
    SpoolmanConnectionError,
    SpoolmanResponseError,
)


async def test_client_error() -> None:
    """Test request client error is handled correctly."""
    async with ClientSession() as session:
        client = Spoolman("192.168.x.x", session=session)
        with (
            patch.object(
                session,
                "request",
                side_effect=ClientError,
            ),
            pytest.raises(SpoolmanConnectionError),
        ):
            assert await client._request("test")


async def test_response_error(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
) -> None:
    """Test request client response error is handled correctly."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/info",
        "GET",
        aresponses.Response(
            status=401,
            text='{"message": "Unauthorized"}',
        ),
    )
    with pytest.raises(SpoolmanConnectionError):
        assert await spoolman_client._request("test")


async def test_not_found_error(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
) -> None:
    """Test request not found error is handled correctly."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/test",
        "GET",
        aresponses.Response(
            status=404,
            headers={"Content-Type": "application/json"},
            text='{"message": "Not found"}',
        ),
    )
    with pytest.raises(SpoolmanResponseError):
        assert await spoolman_client._request("test")
