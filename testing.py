# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

global self


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(859, 434), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow(self)
        self.m_mgr.SetFlags(
            wx.aui.AUI_MGR_ALLOW_ACTIVE_PANE | wx.aui.AUI_MGR_ALLOW_FLOATING | wx.aui.AUI_MGR_DEFAULT | wx.aui.AUI_MGR_HINT_FADE | wx.aui.AUI_MGR_LIVE_RESIZE)

        self.m_dirPicker5 = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                             wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        self.m_mgr.AddPane(self.m_dirPicker5,
                           wx.aui.AuiPaneInfo().Left().MaximizeButton(True).MinimizeButton(True).PinButton(
                               True).Gripper().Float().FloatingPosition(
                               wx.Point(2726, 293)).Fixed().CentrePane().DefaultPane())

        self.m_mgr.Update()
        self.Centre(wx.BOTH)

        # Connect Events
        self.m_dirPicker5.Bind(wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker5OnDirChanged)

    def __del__(self):
        self.m_mgr.UnInit()

    # Virtual event handlers, overide them in your derived class
    def m_dirPicker5OnDirChanged(self, event):
        event.Skip()

MyFrame1(self)