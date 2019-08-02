import wx

#DashBoard Frame

class DashB_Frame(wx.Frame):
    def __init__(self,parent,id,title):
        
        #Frame Creating 
        wx.Frame.__init__(self,parent,id,title) 


#Dashboard Panel

class DashB_Panel(wx.Panel):
    def __init__(self,parent,id,btns,picbtns, txtbtns):

        #Panel Creation
        self.mainPanel = wx.Panel(parent,id)