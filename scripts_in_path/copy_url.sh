#!/bin/bash

# You can enable both at the same time

# copy an url to clipboard
printf "%s" "$1" | xsel -b
# copy to tmux
#printf "%s" "$1" | tmux loadb -
