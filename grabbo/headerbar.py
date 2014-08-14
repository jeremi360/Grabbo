from gi.repository import Gtk

class HeaderBar(Gtk.HeaderBar, Gtk.Box):
    def __init__(self):
        super(HeaderBar, self).__init__()
        self.set_show_close_button(True)
        self.set_title("")
        self.props.border_width = 0
        self.props.margin = 0
        self.set_has_subtitle(False)

    def pack_start(self, child, expand, fill, padding):
        Gtk.Box.pack_start(self, child, expand, fill, padding)

    def pack_end(self, child, expand, fill, padding):
        Gtk.Box.pack_end(self, child, expand, fill, padding)