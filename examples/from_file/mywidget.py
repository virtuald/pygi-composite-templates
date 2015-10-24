#!/usr/bin/env python

from __future__ import print_function

# This is only required to make the example with without requiring installation
# - Most of the time, you shouldn't use this hack
import sys
from os.path import join, dirname
sys.path.insert(0, join(dirname(__file__), '..', '..'))


from gi.repository import Gtk
from gi_composites import GtkTemplate

@GtkTemplate(ui='mywidget.ui')
class MyWidget(Gtk.Box):

    # Required else you would need to specify the full module
    # name in mywidget.ui (__main__+MyWidget)
    __gtype_name__ = 'MyWidget'
    
    entry = GtkTemplate.Child()
    
    # Alternative way to specify multiple widgets
    #label1, entry = GtkTemplate.Child.widgets(2)

    def __init__(self, text):
        super(Gtk.Box, self).__init__()
        
        # This must occur *after* you initialize your base
        self.init_template()
        
        self.entry.set_text(text)
    
    @GtkTemplate.Callback
    def button_clicked(self, widget, user_data):
        # 'object' attribute (user-data in glade) is set
        print("The button was clicked with entry text: %s" % self.entry.get_text())
        print("The user-data is %s" % user_data)

    @GtkTemplate.Callback
    def entry_changed(self, widget):
        # 'object' attribute (user-data in glade) is not set
        print("The entry text changed: %s" % self.entry.get_text())

    @GtkTemplate.Callback
    def on_MyWidget_destroy(self, widget):
        print("MyWidget destroyed")


class MySubWidget(MyWidget):
    pass

if __name__ == '__main__':
    
    win = Gtk.Window()
    win.connect('delete-event', Gtk.main_quit)
    
    widget = MySubWidget("The entry text!")
    win.add(widget)
    
    win.show_all()
    
    Gtk.main()
