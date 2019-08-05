import wx
from .LayoutManager import LayerCalculation, Apps_per_Row


'''
------------------------------------------------------------------------------
                                FRAME 
------------------------------------------------------------------------------
'''

#DashBoard Frame

class DashB_Frame(wx.Frame):
    def __init__(self,parent,id,title):
        
        #Frame Creating 
        wx.Frame.__init__(self,parent,id,title) 
        self.SetBackgroundColour('black')



'''
------------------------------------------------------------------------------
                                PANEL 
------------------------------------------------------------------------------
'''
#Dashboard Panel

class DashB_Panel(wx.Panel):
    def __init__(self, parent, id, btns, picbtns, txtbtns):

        #Panel Creation
        self.mainPanel = wx.Panel.__init__(self,parent,id)

        #Create Sections Widgets - It will hols the actual widgets
        app_sections = self.SectionCreation(btns)

        #Populate Sections - Fills the widget holders.
        self.sectionPopulater(app_sections, txtbtns)

        #Panel BoxSizer
        pnBxSz = wx.BoxSizer(wx.VERTICAL)

        #Add sections to panel sizer
        pnBxSz.Add(self.sectionSizers(app_sections),1,wx.ALL|wx.EXPAND)

        self.SetSizer(pnBxSz)

    def SectionCreation(self, apps):
        sections = list()
        num_layers = LayerCalculation(apps)
        #Create BoxSizers wich will hold the widgests conforming the sections
        #Inser BxSizers in list
        for lyrs in range(num_layers):
            sections.append(wx.BoxSizer(wx.HORIZONTAL))
        return sections
        
    def sectionPopulater(self,sections, nameApps):
        counter = 0
        #Get each section individually(section = BoxSizer)
        for section in sections:
            #Apps allow per section
            for app in range(Apps_per_Row):
                #Once App name has reach limit exit
                if len(nameApps) == counter:
                    break
                #populating section (BoxSizer)
                section.Add( wx.Button(self,-1,nameApps[counter]),1, wx.ALL|wx.EXPAND)
                counter += 1    
    
    def sectionSizers(self,sections):
        bxSz = wx.BoxSizer(wx.VERTICAL)
        for section in sections:
            bxSz.Add(section,1,wx.ALL|wx.EXPAND)
        return bxSz
