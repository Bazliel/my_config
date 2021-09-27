# # # # # # # # # # # # # # # #
#   
#        _           _   _                     Bazliel Wondimagegn
#       | |__  _   _| |_| |__   ___  _ __      @archlinux
#       | '_ \| | | | __| '_ \ / _ \| '_ \     qtile configuration file
#       | |_) | |_| | |_| | | | (_) | | | |    
#   ____|_.__/ \__, |\__|_| |_|\___/|_| |_|     
#  |_____|     |___/                          
#                                              
# # # # # # # # # # # #
# A customized config.py for Qtile("https://www.qtile.org") 
# Configured by Bazliel Wondimagegn 

# Default config comments for qtile below

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.


# IMPORTS
import os
import socket
import subprocess
from typing import List, Text 
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Defining some variables
mod = "mod4"
terminal = "alacritty"


# KEYBINDING
keys = [
    Key(
        [mod], "d",   
        lazy.spawn("rofi -no-lazy-grab -show drun -modi drun"), 
        desc="Run Rofi"
    ),                                                  
    
    Key(
        [mod], "j", 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),

    Key(
        [mod], "semicolon", 
        lazy.layout.right(), 
        desc="Move focus to right"
    ),

    Key(
        [mod], "k", 
        lazy.layout.down(), 
        desc="Move focus down"
    ),

    Key(
        [mod], "l", 
        lazy.layout.up(), 
        desc="Move focus up"
    ),
    
    Key(
        [mod], "space", 
        lazy.layout.next(),
        desc="Move window focus to other window"
    ),

    Key(
        [mod, "shift"], "j", 
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),

    Key(
        [mod, "shift"], "semicolon", 
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),

    Key(
        [mod, "shift"], "k", 
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),

    Key(
        [mod, "shift"], "l", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
    ),
    
    Key(
        [mod, "control"], "j", 
        lazy.layout.grow_left(),
        desc="Grow window to the left"
    ),

    Key(
        [mod, "control"], "semicolon", 
        lazy.layout.grow_right(),
        desc="Grow window to the right"
    ),

    Key(
        [mod, "control"], "k", 
        lazy.layout.grow_down(),
        desc="Grow window down"
    ),

    Key(
        [mod, "control"], "l", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),

    Key(
        [mod], "n", 
        lazy.layout.normalize(),
        desc="Reset all window sizes"
    ),

    Key(
        [mod, "shift"], "Return", 
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
    ),

    Key(
        [mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
    ),

    Key(
        [mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
    ),

    Key(
        [mod, 'shift'], "q", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),

    Key(
        [mod, "control"], "r", 
        lazy.restart(), 
        desc="Restart Qtile"
    ),

    Key(
        [mod, "control"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),
    
    Key(
	[mod], "F1",
	lazy.spawn("loginctl lock-session"),
        desc="lock the screen"
    ),

    KeyChord([mod, 'shift'], 'x', [
            Key([], "e", lazy.spawn("shutdown now")),
            Key([], "r", lazy.spawn("reboot")),
            Key([], "l", lazy.spawn("loginctl lock-session")),
            Key([], "s", lazy.spawn("pm-suspend")),
            Key([], "h", lazy.spawn("pm-hibernate")),
        ]
    ),

    Key(
        [mod], "r", 
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
    ),

    Key(
        [], "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl -s set +5%")
    ),

    Key(
        [], "XF86MonBrightnessDown", 
        lazy.spawn("brightnessctl -s set 5%-")
    ),

    Key(
        [], "XF86AudioRaiseVolume", 
        lazy.spawn("amixer set Master 5%+")
    ),

    Key(
        [], "XF86AudioLowerVolume", 
        lazy.spawn("amixer set Master 5%-")
    ),
    
    Key(
        [], "XF86AudioMute", 
        lazy.spawn("amixer -D pulse set Master toggle")
    ),	
]


## GROUP CONFIGURATION ##
group_names = [("1", {'layout': 'columns'}),
               ("2", {'layout': 'columns'}),
               ("3", {'layout': 'columns'}),
               ("4", {'layout': 'columns'}), 
               ("5", {'layout': 'columns'}),
               ("6", {'layout': 'columns'}),
               ("7", {'layout': 'columns'}),
               ("8", {'layout': 'columns'}),
               ("9", {'layout': 'columns'})]
groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))      
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True)))
    keys.append(Key([mod, "control"],  str(i), lazy.window.togroup(name)))


# COLORS
colors = [["#0D1117", "#0D1117"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"]] # font color for group names
                                 
## PROMPT ##
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

## Default layout themes
layout_theme = {
    'margin': 5,
    'border_normal': colors[0][0],
    'border_focus': colors[1][1]
}

## LAYOUTS

layouts = [
    layout.Columns(border_focus_stack=colors[0], border_width=2, **layout_theme),
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

## WIDGET AND BAR CONFIGS ##

widget_defaults = dict(
    font='Cascadia Code PL Bold',
    fontsize=13,
    padding=0,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
            widget.Sep(
                    linewidth = 0,
                    padding = 10,
                    foreground = colors[2],
                ),

               widget.GroupBox(font="Cascadia Code PL Bold",
                        fontsize = 12,
                        margin_y = 2,
                        margin_x = 0,
                        disable_drag = True,
                        padding_y = 5,
                        padding_x = 9,
                        borderwidth = 0,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[1],
                        highlight_method = "line",
                        #this_current_screen_border = colors[3],
                        #this_screen_border = colors [4],
                        other_current_screen_border = colors[0],
                        other_screen_border = colors[0],
                        foreground = colors[2],
                        background = colors[0],
			hide_unused = True
                    ),

               widget.Prompt(
                        prompt=prompt,
                        font="Cascadia Code",
                        padding=10,
                        foreground = colors[2],
                        background = colors[0]
                    ),
               widget.Sep(
                        linewidth = 0,
                        padding = 20,
                        foreground = colors[2],
                        background = colors[0]
                    ),
                
               widget.WindowName(
                        foreground = colors[1],
                        background = colors[0],
                        padding = 0
                    ),
        
               widget.Net(
                        format = " ↓↑ {down}",
                        background = colors[0],
                        foreground = colors[2],
                        interface = "wlp3s0",
                        margin = 0,
                        padding = 20
                    ),

                widget.Spacer(length = 2, background = colors[0]),
   
                widget.TextBox(
                        text="",
                        fontsize=27,
                        background = colors[0],
                        foreground = colors[2],
                        padding=0
                ),
                widget.Backlight(
                       backlight_name = "intel_backlight",
                       max_brightness_file = "max_brightness",
                       brightness_file = "brightness",
                       background = colors[0],
                       foreground = colors[2],
                       step = 5,
                       update_interval = 0.2,
                       padding = 4,
                       
                    ),
                
                widget.Spacer(length = 10, background = colors[0]),
        
                widget.TextBox(
                       text="",
                       fontsize=25,
                       foreground=colors[2],
                       background=colors[0],
                       padding = 0
                    ),

                widget.Volume(
                        foreground = colors[2],
                        background = colors[0],
                        padding = 4
                    ),

                widget.Spacer(length = 10, background = colors[0]),
			
                widget.Battery(
                    notify_below=17,
                    charge_char="",
                    discharge_char="",
                    low_foreground="FF0000",
                    empty_char="!",
                    format="{char} {percent:2.0%}",
                    background=colors[0],
                    update_interval=0.1,
                    padding=10
                ),


                widget.Spacer(length = 10, background = colors[0]),

                widget.CurrentLayoutIcon(
                        custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                        foreground = colors[2],
                        background = colors[0],
                        padding = 0,
                        scale=0.5
                    ),
               widget.CurrentLayout(
                        foreground = colors[2],
                        background = colors[0],
                        padding = 5
                    ),
                widget.Spacer(length = 10, background = colors[0]),
                
                widget.Clock(
                        foreground = colors[2],
                        background = colors[0],
                        format = "%a, %b%d %y",
                        padding = 10
                    ),
                
                widget.Spacer(length = 10, background = colors[0]),
                
                widget.Clock(
                        foreground = colors[2],
                        background = colors[0],
                        format = "%H:%M",
                        padding = 10
                    ),
                widget.Systray(
                        background = colors[0],
                        padding = 2
                    ),
		widget.Sep(
		        line_width = 0,
			padding = 10,
			foreground = colors[0]    
		    )
            ],
            24,
	    opacity=.6
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
])

## Auto start 
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([f'{home}/scripts/auto_start.sh'])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
