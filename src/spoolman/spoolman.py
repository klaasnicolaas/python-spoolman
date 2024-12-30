"""Asynchronous Python client for Spoolman."""

from __future__ import annotations

import asyncio
import socket
from dataclasses import dataclass
from importlib import metadata
from typing import Any, Self, cast

from aiohttp import ClientError, ClientSession
from aiohttp.hdrs import METH_GET
from yarl import URL

from .exceptions import SpoolmanConnectionError, SpoolmanError, SpoolmanResponseError
from .models import Filament, Info, Spool, Vendor

VERSION = metadata.version(__package__)


@dataclass
class Spoolman:
    """Main class for handling connections with the Spoolman API."""

    host: str
    port: int = 7912

    request_timeout: float = 10.0
    session: ClientSession | None = None

    _close_session: bool = False

    async def _request(
        self,
        uri: str,
        *,
        method: str = METH_GET,
        params: dict[str, Any] | None = None,
    ) -> Any:
        """Handle a request to the Spoolman API.

        Args:
        ----
            uri: Request URI, without '/api/', for example, 'status'.
            method: HTTP method to use.
            params: Extra options to improve or limit the response.

        Returns:
        -------
            A Python dictionary (JSON decoded) with the response from
            the Spoolman API.

        Raises:
        ------
            SpoolmanConnectionError: If the connection to the API fails.
            SpoolmanError: If the API returns an error.
            SpoolmanResponseError: If the API returns a error.

        """
        url = URL.build(
            scheme="http",
            host=self.host,
            port=int(self.port),
            path="/api/v1/",
        ).join(URL(uri))

        headers = {
            "User-Agent": f"PythonSpoolman/{VERSION}",
            "Accept": "application/json",
        }

        if self.session is None:
            self.session = ClientSession()
            self._close_session = True

        try:
            async with asyncio.timeout(self.request_timeout):
                response = await self.session.request(
                    method,
                    url,
                    params=params,
                    headers=headers,
                )

                if response.status == 404:
                    response_data = await response.json()
                    raise SpoolmanResponseError(response_data, response.status)

                response.raise_for_status()

        except TimeoutError as exception:
            msg = "Timeout occurred while connecting to the Spoolman API."
            raise SpoolmanConnectionError(msg) from exception
        except (ClientError, socket.gaierror) as exception:
            msg = "Error occurred while connecting to the Spoolman API."
            raise SpoolmanConnectionError(msg) from exception

        content_type = response.headers.get("content-type", "")
        if "application/json" not in content_type:
            text = await response.text()
            msg = "Unexpected response from the Spoolman API."
            raise SpoolmanError(
                msg,
                {"Content-Type": content_type, "Response": text},
            )

        return cast(dict[str, Any], await response.json())

    async def info(self) -> Info:
        """Get information about the Spoolman API.

        Returns
        -------
            A dictionary with information about the Spoolman API.

        """
        response = await self._request("info")
        return Info.from_dict(response)

    async def health(self) -> bool:
        """Check the health of the Spoolman API.

        Returns
        -------
            True if the API is healthy, False otherwise.

        """
        response: dict[str, str] = await self._request("health")
        return response["status"] == "healthy"

    async def get_filaments(self) -> list[Filament]:
        """Get a list of all available filaments.

        Returns
        -------
            A list with filament data.

        """
        response = await self._request("filament")
        return [Filament.from_dict(item) for item in response]

    async def get_filament(self, filament_id: int) -> Filament:
        """Get a specific filament by ID.

        Args:
        ----
            filament_id: The ID of the filament to retrieve.

        Returns:
        -------
            A dictionary with the filament data.

        """
        response = await self._request(f"filament/{filament_id}")
        return Filament.from_dict(response)

    async def get_spools(self) -> list[Spool]:
        """Get a list of all available spools.

        Returns
        -------
            A list with spool data.

        """
        response = await self._request("spool")
        return [Spool.from_dict(item) for item in response]

    async def get_spool(self, spool_id: int) -> Spool:
        """Get a specific spool by ID.

        Args:
        ----
            spool_id: The ID of the spool to retrieve.

        Returns:
        -------
            A dictionary with the spool data.

        """
        response = await self._request(f"spool/{spool_id}")
        return Spool.from_dict(response)

    async def get_vendors(self) -> list[Vendor]:
        """Get a list of all available vendors.

        Returns
        -------
            A list with vendor data.

        """
        response = await self._request("vendor")
        return [Vendor.from_dict(item) for item in response]

    async def get_vendor(self, vendor_id: int) -> Vendor:
        """Get a specific vendor by ID.

        Args:
        ----
            vendor_id: The ID of the vendor to retrieve.

        Returns:
        -------
            A dictionary with the vendor data.

        """
        response = await self._request(f"vendor/{vendor_id}")
        return Vendor.from_dict(response)

    async def close(self) -> None:
        """Close open client session."""
        if self.session and self._close_session:
            await self.session.close()

    async def __aenter__(self) -> Self:
        """Async enter.

        Returns
        -------
            The Spoolman object.

        """
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit.

        Args:
        ----
            _exc_info: Exec type.

        """
        await self.close()
