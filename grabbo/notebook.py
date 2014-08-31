from gi.repository import Gtk
import os
import grabbo

r = os.path.realpath(__file__)
CB_UI = os.path.join(r, '..', 'ui', 'CloseButton.xml')

class _CloseButton(grabbo.Builder):
    def __init__(self, notebook, content):
        super(_CloseButton, self).__init__(CB_UI)

        self.get().connect("clicked", self.on_it)

        self.n = notebook
        self.c = content

    def get(self):
        return self.ui.get_object("CloseButton")

    def on_it(self, button):
        self.n.stack.remove(self.c)
        self.n.switcher.remove(self)


TABS_UI = os.path.join(r, '..', 'ui', 'Tabs.xml')

class Notebook(grabbo.Builder):
    def __init__(self, stack = Gtk.Stack(), addable = True, closeable = True, orientation = Gtk.Orientation.HORIZONTAL):
        super(Notebook, self).__init__(TABS_UI)


        self.set_orientation(orientation)
        self.stack = stack

        self.set_addable(addable)
        self.AddButton.connect("clicked", self.on_add)

        self.switcher = Gtk.StackSwitcher()
        self.switcher.set_stack(self.stack)

        vp.add(self.switcher)
        self._sc = Gtk.ScrolledWindow()

    def get(self):
        return self.ui.get_object("box")

    def on_add(self, button):
        content = Gtk.Label()
        content.set_label("Content")
        self.add_tab(content)

    def add_tab(self, content, closeable = True):

        self.stack.add_titled(content, "_Namestack", "LabelInTheSwitcher")

        if closeable:
            cb = _CloseButton(self, content)
            self.switcher.add(cb)
            cb.show()

    def set_addable(self, addable):
        if addable:
            self.AddButton.show()

