# Base Python Project
As I come up to speed on the modern Python ecosystem, I thought I could save time and improve my tooling by creating a consistent base for future projects. This aims to provide opinionated defaults.

This project uses some projects that may not be ready for production use. I wanted to evaluate and learn new techologies as a part of creating this. The most new to me is [Nix](https://nixos.org/) and [poetry](https://python-poetry.org/) via [poetry2nix](https://github.com/nix-community/poetry2nix), which I'm using for reproducable builds and deterministic development environments. This project uses the experimental Nix feature, flakes.

Pyright (in VSCode as Pylance) is also fairly new to me. It's proven itself to be dramatically better than mypy, and I can't imagine ever going back to not having type-inference.

Other tools included:
 - [pyright](https://github.com/microsoft/pyright) for type-checking
 - [ruff](https://github.com/charliermarsh/ruff) for linting
 - [black](https://github.com/psf/black) for formatting
