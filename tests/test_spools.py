"""Test the Spool model for Spoolman."""

from __future__ import annotations

from typing import TYPE_CHECKING

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from spoolman import Spoolman


async def test_get_spools(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting a list of spools."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/spool",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("spools.json"),
        ),
    )
    spools = await spoolman_client.get_spools()
    assert spools == snapshot


async def test_get_spool(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting a specific spool."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/spool/1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("single_spool.json"),
        ),
    )
    spool = await spoolman_client.get_spool(spool_id=1)
    assert spool == snapshot
