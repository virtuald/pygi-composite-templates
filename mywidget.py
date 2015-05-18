#!/usr/bin/env python

from __future__ import print_function

from gi.repository import Gtk
from gi_composites import GtkTemplate, GtkCallback, GtkChild


@GtkTemplate(ui='mywidget.ui')
class MyWidget(Gtk.Box):

    # Required else you would need to specify the full module
    # name in mywidget.ui (__main__+MyWidget)
    __gtype_name__ = 'MyWidget'
    
    entry = GtkChild()
    
    # Alternative way to specify multiple widgets
    #label1, entry = GtkChild.widgets(2)

    def __init__(self, text):
        super(Gtk.Box, self).__init__()
        
        # This must occur *after* you initialize your base
        self.init_template()
        
        self.entry.set_text(text)
    
    @GtkCallback
    def button_clicked(self, widget):
        print("The button was clicked with entry text: %s" % self.entry.get_text())

    @GtkCallback
    def entry_changed(self, widget):
        print("The entry text changed: %s" % self.entry.get_text())


if __name__ == '__main__':
    
    win = Gtk.Window()
    win.connect('delete-event', Gtk.main_quit)
    
    widget = MyWidget("The entry text!")
    win.add(widget)
    
    win.show_all()
    
    Gtk.main()
