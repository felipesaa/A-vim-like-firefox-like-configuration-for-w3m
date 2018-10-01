#!/bin/bash
#copy an url to clipboard
printf "%s" "$1" | xsel -b
