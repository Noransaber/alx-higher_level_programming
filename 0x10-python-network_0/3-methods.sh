#!/bin/bash
#cURL only methods
curl -sI ALLOW $1 -L | grep "ALLOW" | cut -d " " -f2-
