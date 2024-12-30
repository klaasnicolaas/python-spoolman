"""Test the Vendor model for Spoolman."""

from __future__ import annotations

from typing import TYPE_CHECKING

from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from spoolman import Spoolman


async def test_get_vendors(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting a list of vendors."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/vendor",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("vendors.json"),
        ),
    )
    vendors = await spoolman_client.get_vendors()
    assert vendors == snapshot


async def test_get_vendor(
    aresponses: ResponsesMockServer,
    spoolman_client: Spoolman,
    snapshot: SnapshotAssertion,
) -> None:
    """Test getting a specific vendor."""
    aresponses.add(
        "192.168.x.x:7912",
        "/api/v1/vendor/1",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("single_vendor.json"),
        ),
    )
    vendor = await spoolman_client.get_vendor(vendor_id=1)
    assert vendor == snapshot
