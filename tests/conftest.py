"""Fixture for the Spoolman tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from spoolman import Spoolman


@pytest.fixture(name="spoolman_client")
async def client() -> AsyncGenerator[Spoolman, None]:
    """Create a Spoolman client."""
    async with (
        ClientSession() as session,
        Spoolman(host="192.168.x.x", session=session) as spoolman_client,
    ):
        yield spoolman_client
