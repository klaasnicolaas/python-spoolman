"""Asynchronous Python client for Spoolman."""

from __future__ import annotations

import asyncio

from spoolman import Spoolman


async def main() -> None:
    """Show basic information about the Spoolman API."""
    async with Spoolman(host="IP_ADDRESS") as client:
        info = await client.info()
        health = await client.health()

        print(f"Healthy system: {health}")
        print(info)


if __name__ == "__main__":
    asyncio.run(main())
