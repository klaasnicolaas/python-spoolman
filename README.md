<!-- Banner -->
![alt Banner of the Spoolman package](https://raw.githubusercontent.com/klaasnicolaas/python-spoolman/main/assets/header_spoolman-min.png)

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![PyPi Downloads][downloads-shield]][downloads-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]
[![Open in Dev Containers][devcontainer-shield]][devcontainer]

[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]
[![Code Coverage][codecov-shield]][codecov-url]


Asynchronous Python client for [Spoolman][spoolman].

## About

Spoolman is a self-hosted platform for managing 3D printer filament spools. It integrates with popular 3D printing software to track spool weights in real time, providing instant insights into filament usage.

## Installation

```bash
pip install spoolman
```

## Data

- Application info and health
- Filaments
- Spools
- Vendors

### Example

```python
import asyncio

from spoolman import Spoolman


async def main() -> None:
    """Show example on using this package."""
    async with Spoolman(host="IP_ADDRESS") as client:
        # Get all filaments
        filaments = await client.get_filaments()
        print(filaments)


if __name__ == "__main__":
    asyncio.run(main())
```

More examples can be found in the [examples folder](./examples/).

## Class Parameters

| Parameter | value Type | Description                                                       |
| :-------- | :--------- | :---------------------------------------------------------------- |
| `host`    | `str`      | The IP address of your Spoolman instance.                         |
| `port`    | `int`      | The port of your Spoolman instance (optional). Default is `7912`. |

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

The simplest way to begin is by utilizing the [Dev Container][devcontainer]
feature of Visual Studio Code or by opening a CodeSpace directly on GitHub.
By clicking the button below you immediately start a Dev Container in Visual Studio Code.

[![Open in Dev Containers][devcontainer-shield]][devcontainer]

This Python project relies on [Poetry][poetry] as its dependency manager,
providing comprehensive management and control over project dependencies.

You need at least:

- Python 3.11+
- [Poetry][poetry-install]

### Installation

Install all packages, including all development requirements:

```bash
poetry install
```

_Poetry creates by default an virtual environment where it installs all
necessary pip packages_.

### Pre-commit

This repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. To setup the pre-commit check, run:

```bash
poetry run pre-commit install
```

And to run all checks and tests manually, use the following command:

```bash
poetry run pre-commit run --all-files
```

### Testing

It uses [pytest](https://docs.pytest.org/en/stable/) as the test framework. To run the tests:

```bash
poetry run pytest
```

To update the [syrupy](https://github.com/tophat/syrupy) snapshot tests:

```bash
poetry run pytest --snapshot-update
```

## License

MIT License

Copyright (c) 2024 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


<!-- LINKS FROM PLATFORM -->
[spoolman]: https://github.com/Donkie/Spoolman

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/klaasnicolaas/python-spoolman/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/klaasnicolaas/python-spoolman/actions/workflows/tests.yaml
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-spoolman/branch/main/graph/badge.svg?token=C92VQ5QJ21
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-spoolman
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-spoolman.svg
[commits-url]: https://github.com/klaasnicolaas/python-spoolman/commits/main
[devcontainer-shield]: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
[devcontainer]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/klaasnicolaas/python-spoolman
[downloads-shield]: https://img.shields.io/pypi/dm/spoolman
[downloads-url]: https://pypistats.org/packages/spoolman
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-spoolman.svg
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-spoolman.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/spoolman/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/spoolman
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-spoolman.svg
[releases]: https://github.com/klaasnicolaas/python-spoolman/releases
[typing-shield]: https://github.com/klaasnicolaas/python-spoolman/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-spoolman/actions/workflows/typing.yaml

[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
