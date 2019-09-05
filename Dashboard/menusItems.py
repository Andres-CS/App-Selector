import wx

from .McSr_MenuItems_Events import onClickAdd_ms
from .About_MenuItems_Events import onClickAbout

'''
------------------------------------------------------------------------------
                                GenericMenu 
------------------------------------------------------------------------------
'''

class GenericMenu(wx.Menu):
    def __init__(self):
        pass
    
    #Menu Items
    def grCreateMenuItems(self,lbs,infotxt):
        itemswdg = list()
        for idx, lb in enumerate(lbs):
            item = wx.MenuItem(None,-1,lb,infotxt[idx],wx.ITEM_NORMAL)
            itemswdg.append(item)
        return itemswdg 

'''
------------------------------------------------------------------------------
                                FileM 
------------------------------------------------------------------------------
'''

class FileM(GenericMenu):
    def __init__(self):
        self.flM = wx.Menu.__init__(self)
        items = ["Properties","Quit"]
        infotxt = ["Modify the DashBoard","Kill the DashBoard"]
        mitems = self.grCreateMenuItems(items, infotxt)

        for x in mitems:
            self.Append(x)


'''
------------------------------------------------------------------------------
                                microsrvM
------------------------------------------------------------------------------
'''

class microsrvM(GenericMenu):
    def __init__(self):
        self.MSr = wx.Menu.__init__(self)

        items = ["Add","Remove","Edit","Inspect"]
        infotxt = ["Add a new MicroSrv", "Remove a MicroSrv","Edit a MicroSrv", "See Settings of a MicroSrv"]
        mitems = self.grCreateMenuItems(items,infotxt)

        #Adding Items to Menu
        for x in mitems:
            self.Append(x)
        
        self.Bind(wx.EVT_MENU, onClickAdd_ms, mitems[0])


'''
------------------------------------------------------------------------------
                                AboutM 
------------------------------------------------------------------------------
'''

class AboutM(GenericMenu):
    def __init__(self):
        self.AbtM = wx.Menu.__init__(self)
        itemsLb = ["About","License"]
        infotxt = ["Infomation about NuvoTools","License under which NuvoTools is govern"]
        self.MnItems = self.grCreateMenuItems(itemsLb, infotxt)
        
        #Adding Items to Menu
        for x in self.MnItems:
            self.Append(x)
        
        #Adding Event to Items
        self.Bind(wx.EVT_MENU, onClickAbout, self.MnItems[0])