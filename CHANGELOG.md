0.2.1 - 2015-09-28
------------------
* Allow initialization of templates from GLib resources or from file

0.2.0 - 2015-05-21
------------------
* Allow initializing multiple widgets

Breaking changes:
* No longer require user-data/object to be set in XML file, so if they're set
  they will be passed to the signal handler as per usual
* GtkChild -> GtkTemplate.Child
* GtkCallback -> GtkTemplate.Callback

0.1.0 - 2015-05-17
------------------
* Initial release, seems to work!

