#!/bin/bash
# Sends a request to URL and displays size of the body
curl -s "$1" | wc -c
