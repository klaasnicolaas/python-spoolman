"""Test the Filament model for Spoolman."""

from __future__ import annotations

from typing import TYPE_CHECKING

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from spoolman import Spoolman


async def test_get_filaments(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    spoolman_client: Spoolman,
) -> None:
    """Test getting all available filaments."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/filament",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("filaments.json"),
        ),
    )
    filaments = await spoolman_client.get_filaments()
    assert filaments == snapshot


async def test_get_filament(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    spoolman_client: Spoolman,
) -> None:
    """Test getting a specific filament."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/filament/1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("single_filament.json"),
        ),
    )
    filament = await spoolman_client.get_filament(filament_id=1)
    assert filament == snapshot
