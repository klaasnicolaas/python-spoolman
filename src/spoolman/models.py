"""Asynchronous Python client for Spoolman."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime  # noqa: TC003

from mashumaro import DataClassDictMixin, field_options


@dataclass
class Info(DataClassDictMixin):
    """Data class for the 'info' endpoint."""

    version: str
    debug_mode: bool
    automatic_backups: bool
    db_type: str
    git_commit: str
    build_date: datetime
    data_dir: str
    logs_dir: str
    backups_dir: str


@dataclass
class Filament(DataClassDictMixin):
    """Data class for filament data."""

    id: int
    registered: datetime
    name: str | None = None
    color: str | None = field(default=None, metadata=field_options(alias="color_hex"))
    vendor: Vendor | None = None
    external_id: str | None = None

    material: str | None = None
    density: float | None = None
    diameter: float | None = None
    weight: float | None = None
    spool_weight: float | None = None
    extruder_temp: int | None = field(
        default=None, metadata=field_options(alias="settings_extruder_temp")
    )
    bed_temp: int | None = field(
        default=None, metadata=field_options(alias="settings_bed_temp")
    )


@dataclass
class Spool(DataClassDictMixin):
    """Data class for spool data."""

    id: int
    filament: Filament

    used_weight: float
    used_length: float

    archived: bool
    registered: datetime
    initial_weight: float | None = None
    spool_weight: float | None = None
    remaining_weight: float | None = None
    remaining_length: float | None = None
    first_used: datetime | None = field(
        default=None, metadata=field_options(alias="first_used")
    )
    last_used: datetime | None = field(
        default=None, metadata=field_options(alias="last_used")
    )


@dataclass
class Vendor(DataClassDictMixin):
    """Data class for vendor data."""

    id: int
    name: str
    registered: datetime
    external_id: str | None = None
