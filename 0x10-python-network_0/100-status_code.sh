#!/bin/bash
#send a request to a URL
curl -sI -w '%{response_code}' "$1" -o /dev/null
