#!/usr/bin/env bash
NEW_REQUIREMENTS=$(poetry export -f requirements.txt --without-hashes | cut -d';' -f1)

if [ ! -f requirements.txt ]; then
    echo "requirements.txt does not exist!"
    poetry export --without-hashes | cut -d';' -f1 > requirements.txt
    exit 1
fi

REQUIREMENTS=$(cat requirements.txt)

if [ "$NEW_REQUIREMENTS" = "$REQUIREMENTS" ]; then
    exit 0
else
    echo "requirements.txt is not up to date!"
    poetry export --without-hashes | cut -d';' -f1 > requirements.txt
    exit 1
fi
