#!/bin/sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd Scripts
python Filter.py $DIR
python ORG_SIRENE.py $DIR