#!/bin/bash
if [ $# -eq 0 ]; then
  echo "sans argument"
  exit 0
fi
while [ $# -gt 0 ]; do
  echo $1
  shift
done
