import wx
import subprocess

from .LayoutManager import LayerCalculation, Apps_per_Row
from .dashboardMenuBar import dshbrdMenuB


'''
------------------------------------------------------------------------------
                                FRAME 
------------------------------------------------------------------------------
'''

#DashBoard Frame

class DashB_Frame(wx.Frame):
    def __init__(self,parent,id,title):
        
        #Frame Creating 
        wx.Frame.__init__(self,parent,id,title,size=(400,400)) 
        self.SetBackgroundColour('black')

        self.DshMbar = dshbrdMenuB()
        self.SetMenuBar(self.DshMbar)


'''
------------------------------------------------------------------------------
                                PANEL 
------------------------------------------------------------------------------
'''
#Dashboard Panel

class DashB_Panel(wx.Panel):
    def __init__(self, parent, id, MSs, picMS, txtMS):

        #Panel Creation
        self.mainPanel = wx.Panel.__init__(self,parent,id)

        app_sections = self.SectionCreation(MSs) #Create Sections Widgets - It will hols the actual widgets
        app_wdgts = self.WdgtCreation( len(app_sections), txtMS) #Create Widgets - Container that stores the actual widges in groups list(list())
        self.sectionPopulater(app_sections, app_wdgts) #Populate Sections - Fills the widget holders.

        
        pnBxSz = wx.BoxSizer(wx.VERTICAL) #Panel BoxSizer
        pnBxSz.Add(self.sectionSizers(app_sections),1,wx.ALL|wx.EXPAND) #Add sections to panel sizer

        #---
        bxPck = wx.DirPickerCtrl(self,-1)
        pnBxSz.Add(bxPck,1,wx.ALL|wx.EXPAND)
        #---
        
        self.SetSizer(pnBxSz)

        # -- BINDING -- 
        for s in range(len(app_sections)):
            for a in range(len(app_wdgts[s])):
                app_wdgts[s][a].Bind(wx.EVT_BUTTON, self.btn_handler)

    
    ''' METHODS '''

    def SectionCreation(self, numApps):
        row = list()
        num_layers = LayerCalculation(numApps)
        #Create BoxSizers wich will hold the widgests conforming the sections
        #Inser BxSizers in list
        for lyrs in range(num_layers):
            row.append(wx.BoxSizer(wx.HORIZONTAL))
        return row
    
    def WdgtCreation(self, numSections, nameApps):
        counter = 0
        groups = list() #Holder of all sections in the DashBoard

        #Populae groups with the number of groups needed.
        for gn in range(numSections):
            groups.append(list())

        for sct in range(numSections): #Iterate through the number of sections
            for app in range(Apps_per_Row): #Iterate throught the number of apps per section/row
                if counter == len(nameApps): #Check counter does not exceed the number of apps.
                    break
                groups[sct].append(wx.Button(self,-1,nameApps[counter])) #Create the button that will launch the Apps.
                counter += 1
        return groups
            
        
    def sectionPopulater(self, sections, groupApps):
        #The number of groupApps and sections should be the same.
        for groupNum, MicroService in enumerate(groupApps):
            for app in MicroService:
                sections[groupNum].Add(app, 1, wx.ALL| wx.EXPAND)
    
    def sectionSizers(self,sections):
        bxSz = wx.BoxSizer(wx.VERTICAL)
        for section in sections:
            bxSz.Add(section,1,wx.ALL|wx.EXPAND)
        return bxSz

    ''' ------ Test ------ '''

    def btn_handler(self, event):
        app = event.GetEventObject()
        app_lb = app.GetLabel()
        if app_lb == "PrintingResources":
            subprocess.call(["/Users/Andres/Desktop/NTools/dist/nuvotools/nuvotools.exe"])
        elif app_lb =="FireFox":
           subprocess.call(["/Program Files/Mozilla Firefox/firefox.exe"])