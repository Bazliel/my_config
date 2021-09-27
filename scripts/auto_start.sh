#!/bin/bash

lxsession &
nitrogen --restore &
compton -b --config ~/.config/compton/compton.conf &
xss-lock -n ~/scripts/dim_screen.sh -- i3lock-fancy -f Quicksand &
