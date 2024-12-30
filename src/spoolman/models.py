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
    name: str
    color: str = field(metadata=field_options(alias="color_hex"))
    vendor: Vendor
    external_id: str
    registered: datetime

    material: str
    density: float
    diameter: float
    weight: float
    spool_weight: float
    extruder_temp: int = field(metadata=field_options(alias="settings_extruder_temp"))
    bed_temp: int = field(metadata=field_options(alias="settings_bed_temp"))


@dataclass
class Spool(DataClassDictMixin):
    """Data class for spool data."""

    id: int
    filament: Filament

    initial_weight: float
    spool_weight: float
    used_weight: float
    used_length: float
    remaining_weight: float
    remaining_length: float

    archived: bool
    registered: datetime
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
    external_id: str
    registered: datetime
