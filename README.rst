pygi-composite-templates
========================

A prototype implementation of Gtk+ composite widget templates for PyGI. This library
will allow you to declare a composite widget, and mark particular properties
as widgets or methods as signals that are declared in a GtkBuilder XML file
created with glade. Usage of this functionality reduces the amount of
boilerplate required to create a composite widget when using Python/GTK3

This implementation was developed for the `Exaile audio player <http://www.exaile.org>`_
to help us as we move to GTK3. I'm still feeling this out to see what bugs
come up, so please provide feedback!

This implementation was inspired by this `blog post <https://blogs.gnome.org/tvb/2013/05/29/composite-templates-lands-in-vala/>`_
and some comments on it, though I should point out that several years ago I
independently created something that was `very similar for PyGTK <https://github.com/frc2423/2013/blob/master/driver_station/ui/util.py#L25>`_.

There is a `bug open at GTK's bugzilla <https://bugzilla.gnome.org/show_bug.cgi?id=701843>`_
to get composite widget templates implemented in PyGI (it's been open for
awhile, I created this implementation before I realized it existed).

Ideally, this will get integrated into PyGI itself and will no longer be
necessary. Until then, if you find a bug, please report it or submit a
pull request on github!

Requirements
============

* Currently only tested on Linux, GTK 3.14, and Python 2.7.
* Composite templates requires GTK 3.10 or greater
* PyGObject 3.13.2 or greater

Installation
============

This project is easily installed via pip:

    pip install pygi-composite-templates

Usage
=====

See `examples` on the github repo for simple yet complete examples. There are
two examples, one using a ui file embedded in a GResource, and the other using
local file paths.

Author
======

Dustin Spicuzza (dustin@virtualroadside.com)

License
=======

LGPL 2.1+ (Same as PyGI)

