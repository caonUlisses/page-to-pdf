#!/bin/bash

function cleanup() {
  rm output.zip
  rm -Rf output
}

function setup() {
  mkdir output
}

cleanup
setup
pipenv lock -r > requirements.txt
pip install -r requirements.txt --no-deps -t output
zip -r output.zip output
cleanup
