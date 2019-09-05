import wx


'''
------------------------------------------------------------------------------
                                microsrvM
------------------------------------------------------------------------------
'''

def onClickAbout(self):
    about = about_Dialog()
    about.ShowModal()


'''
------------------------------------------------------------------------------
                                Event Handler
------------------------------------------------------------------------------
'''

class about_Dialog(wx.Dialog):

    def __init__(self):

        #Dialog
        wx.Dialog.__init__(self,None,-1,"About")

        #Content
        self.text_fields = ["TITLE","DESCRIPTION","CONTACT","LANGUAGE","FRAMEWORKS"]
        self.text = {
            "TITLE":"Nuvo Tools",
            "DESCRIPTION":"Nuvo Tools is a set of MicroServices focused on helping ease some of the tasks\n found in our production department.",
            "LANGUAGE":"Python 3.7",
            "FRAMEWORKS":"wxPython 4.0.1",
            "CONTACT":"jairo.perez@thenuvogroup.com",
        }

        '''
            txt_widgets:
                GUI
                Description:
                    is a list of lists of staticText widgets
        '''
        self.txt_widgets = self.create_TextFields()

        '''
            txtwdg_boxsizer:
                is list of the BoxSizers in linked to each item in txt_widgets.
        '''
        self. txtwdg_boxsizer = self.create_boxzisers()

        #Dialog BoxSizer
        about_boxsizer = wx.BoxSizer(wx.VERTICAL)

        #Add sizer to Dialog BoxSizer
        for sz in self.txtwdg_boxsizer:
            about_boxsizer.Add(sz,-1,wx.ALL|wx.EXPAND)

    
    def create_TextFields(self):
        #List of text Fields
        txt = list()
        for f in self.text_fields:
            field = wx.StaticText(self,-1,f,style=wx.ALIGN_LEFT)
            value = wx.StaticText(self,-1,self.text[f])
            txt.append([field,value])
        return txt
    
    def create_boxzisers(self):
        #Groups of Sizers
        szrs = list()
        #Create BoxSizers
        for i in range(len(self.txt_widgets)):
            szrs.append(wx.BoxSizer(wx.HORIZONTAL))
        #Populate Sizers
        for idx, wdg in enumerate(self.txt_widgets):
            for i in wdg:
                szrs[idx].Add(i,1,wx.ALL|wx.EXPAND)
        return szrs