# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`df` is a Python code/docs repository for the DF lab. It uses Python 3.12 and is managed with `uv`.

## Commands

```bash
# Install dependencies
uv sync

# Run the main entry point
uv run df

# Run a Python script or module
uv run python -m df.main

# Add a dependency
uv add <package>
```

## Structure

- `df/` — main Python package
- `notes/` — markdown notes, named by date (e.g. `2026-05-04-topic.md`)
