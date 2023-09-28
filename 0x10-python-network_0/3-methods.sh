#!/bin/bash
# takes url
curl -Is "$1" | grep "Allow: " | cut -d ' ' -f 2-
