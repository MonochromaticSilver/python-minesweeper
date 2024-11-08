#!/bin/sh

# set active directory to this file's location
cd "$(dirname "$0")"

if command -v python3 &> /dev/null
then
    python3 -m minesweeper.main
else
    python -m minesweeper.main
fi
