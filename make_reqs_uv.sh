#!/usr/bin/env bash

# 1. Resolve everything and write uv.lock
uv lock

# 2. Runtime only — this is what the Dockerfile installs
uv export --no-dev --no-emit-project --no-hashes -o requirements.txt

# 3. Runtime + dev — this is what CI installs to run pytest
uv export --no-emit-project --no-hashes -o requirements-dev.txt
