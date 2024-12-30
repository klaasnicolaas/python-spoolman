"""Test the Info model for Spoolman."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from spoolman import Spoolman


async def test_get_info(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    spoolman_client: Spoolman,
) -> None:
    """Test getting the info."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/info",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("info.json"),
        ),
    )
    info = await spoolman_client.info()
    assert info == snapshot


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ('{"status": "healthy"}', True),
        ('{"status": "unhealthy"}', False),
    ],
)
async def test_get_health(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
    payload: str,
    expected: bool,  # noqa: FBT001
) -> None:
    """Test getting the health."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/health",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=payload,
        ),
    )
    health = await spoolman_client.health()
    assert health is expected
