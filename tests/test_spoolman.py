"""Basic tests for Spoolman."""

# pylint: disable=protected-access
import asyncio

import pytest
from aiohttp import ClientResponse, ClientSession
from aresponses import Response, ResponsesMockServer

from spoolman import Spoolman
from spoolman.exceptions import SpoolmanConnectionError, SpoolmanError


async def test_json_request(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
) -> None:
    """Test JSON request."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
    )
    await spoolman_client._request("test")
    await spoolman_client.close()


async def test_different_port(aresponses: ResponsesMockServer) -> None:
    """Test different port is handled correctly."""
    aresponses.add(
        "192.168.x.x:7913",
        "/api/v1/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
    )
    async with Spoolman(host="192.168.x.x", port=7913) as client:
        await client._request("test")


async def test_different_scheme(aresponses: ResponsesMockServer) -> None:
    """Test different scheme is handled correctly."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
    )

    called_with_url = None

    async with ClientSession() as session:
        client = Spoolman(host="192.168.x.x", scheme="https", session=session)

        # Patch the session.request to capture the URL
        original_request = session.request

        async def capture_request(method, url, **kwargs):
            nonlocal called_with_url
            called_with_url = str(url)
            return await original_request(method, url, **kwargs)

        session.request = capture_request
        await client._request("test")

    # Verify the URL used https scheme
    assert called_with_url is not None
    assert called_with_url.startswith("https://")


async def test_internal_session(aresponses: ResponsesMockServer) -> None:
    """Test internal session is handled correctly."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
        ),
    )
    async with Spoolman(host="192.168.x.x") as client:
        await client._request("test")


async def test_timeout(aresponses: ResponsesMockServer) -> None:
    """Test request timeout is handled correctly."""

    # Faking a timeout by sleeping
    async def reponse_handler(_: ClientResponse) -> Response:
        await asyncio.sleep(0.2)
        return aresponses.Response(
            body="Goodmorning!",
        )

    aresponses.add("192.168.x.x:7912", "/api/v1/test", "GET", reponse_handler)

    async with ClientSession() as session:
        client = Spoolman(host="192.168.x.x", session=session, request_timeout=0.1)
        with pytest.raises(SpoolmanConnectionError):
            assert await client._request("test")


async def test_content_type(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
) -> None:
    """Test request content type error is handled correctly."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "blabla/blabla"},
        ),
    )
    with pytest.raises(SpoolmanError):
        assert await spoolman_client._request("test")
