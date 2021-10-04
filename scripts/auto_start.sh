#!/bin/bash

lxsession &
nitrogen --restore &
picom -b --config ~/.config/picom/picom.conf &
xss-lock -n ~/scripts/dim_screen.sh -- i3lock-fancy -f Quicksand &
