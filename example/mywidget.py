#!/usr/bin/env python
#
# To run this example, first compile the GLib Resource file containing
# the UI description:
#
#    cd example
#    glib-compile-resources --target=mywidget.gresource mywidget.gresource.xml
#    ./mywidget.py
#

from __future__ import print_function

# Find and load the compiled resources - see note at top of this
# file. This must be done before any classes using resources are
# defined, since the UI file is loaded then, not when the class is
# used. This would normally be done by the application's launch
# script, at the same time as setting Gettext domains, etc.

import os
import sys
from gi.repository import Gio

scriptdir = os.path.dirname(os.path.abspath(sys.argv[0]))
resource = Gio.resource_load(os.path.join(scriptdir, 'mywidget.gresource'))
Gio.Resource._register(resource)

# Now we can define the custom widget.

from gi.repository import Gtk
from gi_composites import GtkTemplate

@GtkTemplate(ui='/org/example/MyWidget/mywidget.ui')
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


if __name__ == '__main__':
    win = Gtk.Window()
    win.connect('delete-event', Gtk.main_quit)
    
    widget = MyWidget("The entry text!")
    win.add(widget)
    
    win.show_all()
    
    Gtk.main()
