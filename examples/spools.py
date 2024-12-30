"""Asynchronous Python client for Spoolman."""

from __future__ import annotations

import asyncio

from spoolman import Spool, Spoolman


async def main() -> None:
    """Show basic information about the Spoolman API."""
    async with Spoolman(host="IP_ADDRESS") as client:
        print("All spools")
        print("==========")
        spools: list[Spool] = await client.get_spools()
        for spool in spools:
            print(spool)

        print()
        print("Single spool")
        print("============")
        single_spool: Spool = await client.get_spool(spool_id=10)
        print(single_spool)


if __name__ == "__main__":
    asyncio.run(main())
