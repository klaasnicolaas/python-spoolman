"""Asynchronous Python client for Spoolman."""

from __future__ import annotations

import asyncio

from spoolman import Filament, Spoolman


async def main() -> None:
    """Show basic information about the Spoolman API."""
    async with Spoolman(host="IP_ADDRESS") as client:
        print("All filaments")
        print("=============")
        filaments: list[Filament] = await client.get_filaments()
        for filament in filaments:
            print(filament)

        print()
        print("Single filament")
        print("===============")
        single_filament: Filament = await client.get_filament(filament_id=1)
        print(single_filament)


if __name__ == "__main__":
    asyncio.run(main())
