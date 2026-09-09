import sys
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, Pango

class ZeroMesh(Gtk.Window):
    def __init__(self):
        super().__init__(title="Zero Mesh - Ultimate Studio")
        self.set_default_size(1100, 750)
        
        self.header = Gtk.HeaderBar()
        self.header.set_show_close_button(True)
        self.header.props.title = ""
        self.header.get_style_context().add_class("hidden-header")
        self.set_titlebar(self.header)
        
        self.setup_css()
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(main_box)
        
        # ================= SIDEBAR =================
        self.sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.sidebar.set_size_request(280, -1)
        self.sidebar.get_style_context().add_class("sidebar")
        main_box.pack_start(self.sidebar, False, False, 0)
        
        logo = Gtk.Label(label="Z E R O M E S H")
        logo.get_style_context().add_class("sidebar-logo")
        logo.set_margin_top(20)
        logo.set_margin_bottom(30)
        self.sidebar.pack_start(logo, False, False, 0)
        
        btn_connect = Gtk.Button(label="🌐 CONNECT TO GRID")
        btn_connect.get_style_context().add_class("action-btn")
        self.sidebar.pack_start(btn_connect, False, False, 10)
        
        lbl_nodes = Gtk.Label(label="ACTIVE NODES")
        lbl_nodes.get_style_context().add_class("section-label")
        lbl_nodes.set_halign(Gtk.Align.START)
        lbl_nodes.set_margin_start(20)
        lbl_nodes.set_margin_top(20)
        self.sidebar.pack_start(lbl_nodes, False, False, 10)
        
        nodes = [
            ("US-EAST-1", "🟢 12ms"),
            ("EU-CENTRAL", "🟢 45ms"),
            ("AP-SOUTH", "🟡 120ms"),
            ("SA-EAST", "🔴 Offline")
        ]
        
        for name, ping in nodes:
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
            box.set_margin_start(20)
            box.set_margin_end(20)
            box.set_margin_bottom(15)
            
            ln = Gtk.Label(label=name)
            ln.get_style_context().add_class("node-name")
            lp = Gtk.Label(label=ping)
            lp.get_style_context().add_class("node-ping")
            
            box.pack_start(ln, True, True, 0)
            box.pack_end(lp, False, False, 0)
            self.sidebar.pack_start(box, False, False, 0)
            
        # ================= MAIN DASHBOARD =================
        self.workspace = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.workspace.get_style_context().add_class("workspace")
        main_box.pack_start(self.workspace, True, True, 0)
        
        title = Gtk.Label(label="Global Mesh Telemetry")
        title.get_style_context().add_class("dashboard-title")
        self.workspace.pack_start(title, False, False, 40)
        
        grid = Gtk.Grid(column_spacing=30, row_spacing=30)
        grid.set_halign(Gtk.Align.CENTER)
        self.workspace.pack_start(grid, False, False, 0)
        
        grid.attach(self.make_stat_card("Encrypted Traffic", "1.2 TB/s"), 0, 0, 1, 1)
        grid.attach(self.make_stat_card("Active Tunnels", "8,432"), 1, 0, 1, 1)
        grid.attach(self.make_stat_card("Blocked Threats", "14,092"), 0, 1, 1, 1)
        grid.attach(self.make_stat_card("Network Health", "99.99%"), 1, 1, 1, 1)
        
    def make_stat_card(self, title, val):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.get_style_context().add_class("stat-card")
        box.set_size_request(250, 150)
        
        lt = Gtk.Label(label=title)
        lt.get_style_context().add_class("stat-title")
        lt.set_margin_top(20)
        
        lv = Gtk.Label(label=val)
        lv.get_style_context().add_class("stat-val")
        lv.set_margin_top(15)
        
        box.pack_start(lt, False, False, 0)
        box.pack_start(lv, False, False, 0)
        return box
        
    def setup_css(self):
        css = b'''
            window { background-color: #030305; }
            .hidden-header { background: #030305; min-height: 0px; padding: 0px; border: none; box-shadow: none; }
            .sidebar { background-color: rgba(6, 8, 12, 0.98); border-right: 1px solid rgba(255, 255, 255, 0.05); }
            .sidebar-logo { color: #FFFFFF; font-size: 22px; font-weight: 900; letter-spacing: 5px; text-shadow: 0 0 15px rgba(57, 255, 20, 0.6); }
            .action-btn { background: linear-gradient(45deg, #39FF14, #00CC00); color: #000000; border-radius: 12px; font-weight: bold; padding: 15px; margin: 0 20px; border: none; box-shadow: 0 5px 20px rgba(57, 255, 20, 0.3); transition: all 0.3s; }
            .action-btn:hover { box-shadow: 0 8px 30px rgba(57, 255, 20, 0.6); transform: scale(1.02); }
            .section-label { color: #4A5568; font-size: 11px; font-weight: 900; letter-spacing: 2px; }
            .node-name { color: #FFFFFF; font-weight: bold; font-size: 14px; }
            .node-ping { color: #8B94A5; font-size: 14px; }
            .workspace { background: radial-gradient(circle at center, #0B101A, #030305); }
            .dashboard-title { color: #FFFFFF; font-size: 36px; font-weight: bold; text-shadow: 0 5px 15px rgba(0,0,0,0.5); }
            .stat-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(57, 255, 20, 0.2); border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); transition: all 0.3s ease; }
            .stat-card:hover { border: 1px solid #39FF14; box-shadow: 0 15px 40px rgba(57, 255, 20, 0.2); transform: translateY(-5px); }
            .stat-title { color: #8B94A5; font-size: 16px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; }
            .stat-val { color: #39FF14; font-size: 48px; font-weight: 200; text-shadow: 0 0 20px rgba(57, 255, 20, 0.4); }
        '''
        provider = Gtk.CssProvider()
        provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

if __name__ == "__main__":
    win = ZeroMesh()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
