#!/bin/bash
# displays the size
curl -s "$1" | wc -c
