## Author: Manoj Elango

# Import the .NET class library
import clr

# Import python sys module
import sys

# Import os module
import os

# Import System.IO for saving and opening files
from System.IO import *

# Import c compatible List and String
from System import String
from System.Collections.Generic import List

# Add needed dll references
sys.path.append(os.environ['LIGHTFIELD_ROOT'])
sys.path.append(os.environ['LIGHTFIELD_ROOT']+"\\AddInViews")
clr.AddReference('PrincetonInstruments.LightFieldViewV5')
clr.AddReference('PrincetonInstruments.LightField.AutomationV5')
clr.AddReference('PrincetonInstruments.LightFieldAddInSupportServices')

# PI imports
from PrincetonInstruments.LightField.Automation import Automation
from PrincetonInstruments.LightField.AddIns import ExperimentSettings
from PrincetonInstruments.LightField.AddIns import DeviceType

import wx
from LFGUI import MyFrame1 as LFGUI

class MyFrame(LFGUI):
    def __init__(self, parent):
        LFGUI.__init__(self, parent)
        self.init_lightfield()
        self.init_bindings()
        
    def init_bindings(self):
        self.m_connectcamerabutton.Bind(wx.EVT_BUTTON, self.on_connect_camera)
        self.m_closebutton.Bind(wx.EVT_BUTTON, self.on_close)
        self.m_acquireimagebutton.Bind(wx.EVT_BUTTON, self.on_acquire_image)

    def init_lightfield(self):
        self.auto = Automation(True, List[String]())
        # Get experiment object
        self.experiment = self.auto.LightFieldApplication.Experiment
        # print("opened lightfield application")
    
    def on_close(self, event):
        self.Close()
        # self.experiment.Close()
        # self.auto.Application.Exit()
        
    def on_acquire_image(self, event):
        
        # check if camera is connected
        if (self.device_found() == False):
            return
        
        experimentor = self.m_expname.GetValue()
        experimentname = self.m_expermentrname.GetValue()

        
        # Set the base file name
        self.experiment.SetValue(
            ExperimentSettings.FileNameGenerationBaseFileName,
            Path.GetFileName(experimentname + "_" + experimentor + "_"))
        
        # Option to Increment, set to false will not increment
        self.experiment.SetValue(
            ExperimentSettings.FileNameGenerationAttachIncrement,
            True)
        
        # Option to add date
        self.experiment.SetValue(
            ExperimentSettings.FileNameGenerationAttachDate,
            False)
        
        # Option to add time
        self.experiment.SetValue(
            ExperimentSettings.FileNameGenerationAttachTime,
            False)
        
        # Acquire image
        self.experiment.Acquire()
        
        # show location to save file
        self.m_statusBar1.SetLabel(String.Format("{0} {1}",
                            "Image saved to",
                            self.experiment.GetValue(
                                ExperimentSettings.
                                FileNameGenerationDirectory)))
        
    def device_found(self):
        # Find connected device
        for device in self.experiment.ExperimentDevices:
            if (device.Type == DeviceType.Camera):
                return True

        # If connected device is not a camera inform the user
        self.m_statusBar1.SetLabel("Camera not found. Please add a camera and try again.")
        # create an alert dialog
        dlg = wx.MessageDialog(self, "Camera not found. Please add a camera and try again.", "Error", wx.OK | wx.ICON_ERROR)
        dlg.ShowModal() 
        return False

    
    
    
    def on_connect_camera(self, event): # do not need this since it auto connects to the camera
        
        auto = Automation(True, List[String]())
        # Get experiment object
        self.experiment = auto.LightFieldApplication.Experiment
        
        # Check for device and inform user if one is needed
        if (self.experiment.AvailableDevices.Count == 0):
            dlg = wx.MessageDialog(self, "Device not found. Please add a device and try again.", "Error", wx.OK | wx.ICON_ERROR)
            dlg.ShowModal() 
        else:
            # Find connected device
            for device in self.experiment.ExperimentDevices:
                if (device.Type == DeviceType.Camera):
                    self.m_statusBar1.SetLabel("Camera found")
                    return True
         
        # If connected device is not a camera inform the user
        self.m_statusBar1.SetLabel("Camera not found. Please add a camera and try again.")
        # create an alert dialog
        dlg = wx.MessageDialog(self, "Camera not found. Please add a camera and try again.", "Error", wx.OK | wx.ICON_ERROR)
        dlg.ShowModal() 
        return False

# init main loop
app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()
