# -*- coding: utf-8 -*-

# Copyright (C) 2019 Purism SPC
# SPDX-License-Identifier: GPL-3.0+
# Author: David Boddie <david.boddie@puri.sm>

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy
Handy.init()


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='com.example.title_bar')
        GLib.set_application_name('Title Bar')
        GLib.set_prgname('com.example.title_bar')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_icon_name('com.example.title_bar')

        title_bar = Handy.TitleBar()
        header = Gtk.HeaderBar(title='Title Bar', show_close_button=True)

        title_bar.add(header)
        window.set_titlebar(title_bar)

        #label = Gtk.Label(wrap=True)
        #label.set_markup('<big>This ws how to use a libhandy '
        #                 'title bar to hold a regular header bar.</big>')

       # btn = Gtk.Button(label="Hello, World!")
       # btn.connect('clicked', lambda x: window.close())

        #draw=Gtk.DrawingArea();


        canvas = Canvas()
        window.add(canvas)
        #window.add(draw)
        window.show_all()

        #draw.connect("expose-event", window.expose)



class Canvas(Gtk.DrawingArea):
    def __init__(self):
        super(Canvas, self).__init__()
        self.x=0;
        self.connect("draw", self.expose)#not expose but draw
        self.set_size_request(800,500)

    def expose(self, widget, event):
        #print(event);
        cr = event
        rect = self.get_allocation()

        # you can use w and h to calculate relative positions which
        # also change dynamically if window gets resized
        w = rect.width
        h = rect.height
        self.x+=1
        # here is the part where you actually draw
        cr.move_to(self.x,0)
        cr.line_to(w/2, h/2)
        cr.stroke()
        widget.queue_draw();

def main(version):

    app = Application()
    return app.run(sys.argv)
