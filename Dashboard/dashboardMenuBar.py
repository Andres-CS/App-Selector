import wx

from .menusItems import *

class dshbrdMenuB(wx.MenuBar):
    def __init__(self):
        self.MB = wx.MenuBar.__init__(self)

        self.MenuItems()
    
    #Set Up Menu Items
    def MenuItems(self):
        self.Append(FileM(),"File")
        self.Append(microsrvM(),"MicroSrvs")
        self.Append(AboutM(), "About")
