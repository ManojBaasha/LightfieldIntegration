# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.1.0-0-g733bf3d)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"LightFieldGUI", pos = wx.DefaultPosition, size = wx.Size( 1104,715 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook7 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel4 = wx.Panel( self.m_notebook7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook7.AddPage( self.m_panel4, u"a page", False )
		self.m_panel5 = wx.Panel( self.m_notebook7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook7.AddPage( self.m_panel5, u"a page", False )
		self.m_testpanel = wx.Panel( self.m_notebook7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_connectcamerabutton = wx.Button( self.m_testpanel, wx.ID_ANY, u"Connect to Camera", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_connectcamerabutton, 0, wx.ALL, 5 )

		self.m_closebutton = wx.Button( self.m_testpanel, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_closebutton, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_testpanel, wx.ID_ANY, u"Experiment Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer2.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.m_expname = wx.TextCtrl( self.m_testpanel, wx.ID_ANY, u"testpics", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_expname, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_testpanel, wx.ID_ANY, u"Experimenter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		fgSizer2.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_expermentrname = wx.TextCtrl( self.m_testpanel, wx.ID_ANY, u"manoj", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_expermentrname, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.m_testpanel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		fgSizer2.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self.m_testpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_acquireimagebutton = wx.Button( self.m_testpanel, wx.ID_ANY, u"Acquire Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_acquireimagebutton, 0, wx.ALL, 5 )

		self.m_button18 = wx.Button( self.m_testpanel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button18, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self.m_testpanel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( self.m_testpanel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self.m_testpanel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button21, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self.m_testpanel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self.m_testpanel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button24, 0, wx.ALL, 5 )


		self.m_testpanel.SetSizer( fgSizer2 )
		self.m_testpanel.Layout()
		fgSizer2.Fit( self.m_testpanel )
		self.m_notebook7.AddPage( self.m_testpanel, u"Testing Panel", True )

		bSizer2.Add( self.m_notebook7, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.HORIZONTAL )

	def __del__( self ):
		pass


