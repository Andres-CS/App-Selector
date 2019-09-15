import wx
import json

'''
------------------------------------------------------------------------------
                                microsrvM
------------------------------------------------------------------------------
'''

'''
------------------------------------------------------------------------------
                                Event Handler
------------------------------------------------------------------------------
'''

def onClickAdd_ms(self):
    addForm = add_MS_dialgo()
    addForm.ShowModal()


'''
------------------------------------------------------------------------------
                                Complementary Widgets
------------------------------------------------------------------------------
'''

class add_MS_dialgo(wx.Dialog):

    def __init__(self):
        #Dialog
        wx.Dialog.__init__(self, None, -1, "Add Service")
        
        #Labels for Widgets in corresponging menuItem_widgets

        self.Add_WdgLbls = ["Name","Executable","Config","Logo"]
        self.Add_actionButton = ["Save","Discard"]

        '''
            Form:
                GUI 
                Description:
                    StaticText - FileDialog
                    StaticText - FileDialog
                    ....
                Form is a list of lists, wiht X number of lists as the widget pairs conforming label and field.
                list [ [], [], ...]
        '''
        self.form = self.formCreation()

        '''
            FormBoxSizers
                is a list of the BoxSizer that corresponds to the widget pairs, whihc will be added to the general Dialog BoxSizer.
        '''
        self.formBoxSizer = self.formBoxSizer_setup()

        '''
            Action Buttons:
                GUI:
                Description:
                    Button | Button
                Action Button save or discards action to be performed.
        '''
        self.actionBtns = self.actBtnsCreation()

        '''
            ActionBtn_Sizer:
                is list of BoxSizer that holds action buttons in a HORIZONTAL layout.
        '''
        self.ActBtnSizer = self.actBtn_Sizer()

        #Dialog BoxSizer
        dg_Bxz = wx.BoxSizer(wx.VERTICAL)

        #Adding BoxSizers groups to Dialgo BoxSizer formBoxSizer
        for bx in self.formBoxSizer:
            dg_Bxz.Add(bx,1,wx.ALL|wx.EXPAND)
        
        #ActionBtnSizer
        dg_Bxz.Add(self.ActBtnSizer,1,wx.ALL|wx.EXPAND)

        #Binding Events to ActionButtons
        self.Bind(wx.EVT_BUTTON, self.saveButton_setup, self.actionBtns[0]) # Save Btn
        self.Bind(wx.EVT_BUTTON, self.cancelButton_setup, self.actionBtns[1]) #Dismissed Btn

        #Setting BoxSizer of Dialogs
        self.SetSizer(dg_Bxz)

    # formCreation: is called by onClickAdd_ms
    def formCreation(self):
        wdgGroups = list()
        for lb in self.Add_WdgLbls:
            wdgLabel = wx.StaticText(self, -1, lb)
            wdgPthDlg = wx.FilePickerCtrl(self,-1,"","None")
            wdgGroups.append([wdgLabel, wdgPthDlg])
        return wdgGroups

    #formBoxSizer_setup: is called by onClickAdd_ms
    def formBoxSizer_setup(self):
        #Remember that self.form is a list of list. Each item list is the ordered pair of widgets.
        Sizers = list()
        #BoxSizerPair
        for n in range(len(self.form)):
            Sizers.append(wx.BoxSizer(wx.HORIZONTAL))
        #Adding widgets into Sizers
        for idx, pair in enumerate(self.form):
            for wdg in pair:
                Sizers[idx].Add(wdg,1,wx.ALL|wx.EXPAND)
        return Sizers

    #actBtnsCreation: is called by onClickAdd_ms
    def actBtnsCreation(self):
        wdgs = list()
        for wg in self.Add_actionButton:
            wdgs.append(wx.Button(self,-1,wg))
        return wdgs

    #actBtn_Sizer: is called by onClickAdd_ms
    def actBtn_Sizer(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for btn in self.actionBtns:
            sizer.Add(btn,1,wx.ALL|wx.EXPAND)
        return sizer

    #saveButton: is called by onClickAdd_ms
    def saveButton_setup(self, event):
        print("save")

    #cancelButton: is called by onClickAdd_ms
    def cancelButton_setup(self, event):
        print("canceled")
        self.Destroy()