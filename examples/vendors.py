"""Asynchronous Python client for Spoolman."""

from __future__ import annotations

import asyncio

from spoolman import Spoolman, Vendor


async def main() -> None:
    """Show basic information about the Spoolman API."""
    async with Spoolman(host="IP_ADDRESS") as client:
        print("All vendors")
        print("===========")
        vendors: list[Vendor] = await client.get_vendors()
        for vendor in vendors:
            print(vendor)

        print()
        print("Single vendor")
        print("=============")
        single_vendor: Vendor = await client.get_vendor(vendor_id=1)
        print(single_vendor)


if __name__ == "__main__":
    asyncio.run(main())
