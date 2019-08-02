import wx

import SettingsManager

from Dashboard.dashboardGUI import DashB_Frame , DashB_Panel

class DashB_App(wx.App):
    def __init__(self, numButtons, picButtons, textButtons):
        self.numButtons = numButtons
        self.picButtons = picButtons
        self.textButtons = textButtons
        wx.App.__init__(self)


    def OnInit(self):
        F = DashB_Frame(None,-1,"Nuvo Tools")
        P = DashB_Panel(F,-1, self.numButtons, self.picButtons, self.textButtons)
        F.Show()
        return True

def main():
    #Retrive MicroServices Info for DashBoard build
    microService_num = SettingsManager.numApps()
    microService_txt = SettingsManager.nameApps()
    microService_img = SettingsManager.logoApps()

    #Launch DashBoard
    DshB = DashB_App(microService_num, microService_txt, microService_img)
    DshB.MainLoop()

main()