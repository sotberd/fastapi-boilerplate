#!/usr/bin/env bash

set -e
set -x

ruff check app scripts --fix
ruff format app scripts
