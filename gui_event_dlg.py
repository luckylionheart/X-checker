# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################
import time

import wx
import wx.xrc


###########################################################################
## Class AddEventDialog
###########################################################################
from data_checker import get_event_name_and_date


class AddEventDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Add Event", pos=wx.DefaultPosition,
                           size=wx.Size(218, 299), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl_url = wx.TextCtrl(self, wx.ID_ANY, u"Event URL", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl_url, 0, wx.ALL | wx.EXPAND, 5)

        # self.m_textCtrl_date = wx.TextCtrl(self, wx.ID_ANY, u"Date in YYYY-MM-DD", wx.DefaultPosition, wx.DefaultSize,
        #                                    0)
        # bSizer4.Add(self.m_textCtrl_date, 0, wx.ALL | wx.EXPAND, 5)
        #
        # self.m_textCtrl_name = wx.TextCtrl(self, wx.ID_ANY, u"Event Name", wx.DefaultPosition, wx.DefaultSize, 0)
        # bSizer4.Add(self.m_textCtrl_name, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Interval in Minutes", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText1.Wrap(-1)
        bSizer5.Add(self.m_staticText1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_slider_interval = wx.Slider(self, wx.ID_ANY, 5, 1, 100, wx.DefaultPosition, wx.DefaultSize,
                                           wx.SL_LABELS | wx.SL_TOP)
        bSizer5.Add(self.m_slider_interval, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Ticket Rows:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer6.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl_ticket_row = wx.TextCtrl(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(-1, -1), 0)
        bSizer6.Add(self.m_textCtrl_ticket_row, 0, wx.ALL, 5)

        bSizer4.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_add = wx.Button(self, wx.ID_OK, u"Add", wx.DefaultPosition, wx.Size(-1, -1), 0)
        bSizer7.Add(self.m_button_add, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button_cancel = wx.Button(self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button_cancel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)



    def add_event(self):
            url = self.m_textCtrl_url.GetValue()
            name, date = get_event_name_and_date(url)
            # self.m_textCtrl_date.Clear()
            # self.m_textCtrl_name.Clear()
            # self.m_textCtrl_name.SetValue(name)
            # self.m_textCtrl_date.SetValue(date)
            interval = self.m_slider_interval.GetValue()
            row = self.m_textCtrl_ticket_row.GetValue()
            self.Destroy()
            return {
                'url': url,
                'date': date,
                'name': name,
                'interval': str(interval),
                'row': row
            }


class EditEventDialog(wx.Dialog):

    def __init__(self, parent, event):
        self.event = event
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Add Event", pos=wx.DefaultPosition,
                           size=wx.Size(218, 299), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl_url = wx.TextCtrl(self, wx.ID_ANY, u"Event URL", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl_url, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_date = wx.TextCtrl(self, wx.ID_ANY, u"Date in YYYY-MM-DD", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        bSizer4.Add(self.m_textCtrl_date, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl_name = wx.TextCtrl(self, wx.ID_ANY, u"Event Name", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_textCtrl_name, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Interval in Minutes", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText1.Wrap(-1)
        bSizer5.Add(self.m_staticText1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_slider_interval = wx.Slider(self, wx.ID_ANY, 5, 1, 100, wx.DefaultPosition, wx.DefaultSize,
                                           wx.SL_LABELS | wx.SL_TOP)
        bSizer5.Add(self.m_slider_interval, 0, wx.ALL | wx.EXPAND, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Ticket Rows:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer6.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl_ticket_row = wx.TextCtrl(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(-1, -1), 0)
        bSizer6.Add(self.m_textCtrl_ticket_row, 0, wx.ALL, 5)

        bSizer4.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button_add = wx.Button(self, wx.ID_OK, u"Add", wx.DefaultPosition, wx.Size(-1, -1), 0)
        bSizer7.Add(self.m_button_add, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button_cancel = wx.Button(self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.m_button_cancel, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer4.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer4)
        self.Layout()

        self.Centre(wx.BOTH)
        self.load_data()


    def add_event(self):
            url = self.m_textCtrl_url.GetValue()
            date = self.m_textCtrl_date.GetValue()
            name = self.m_textCtrl_name.GetValue()
            interval = self.m_slider_interval.GetValue()
            row = self.m_textCtrl_ticket_row.GetValue()
            self.Destroy()
            return {
                'url': url,
                'date': date,
                'name': name,
                'interval': str(interval),
                'row': row
            }

    def load_data(self):
        self.m_textCtrl_url.SetValue(self.event[4])
        self.m_textCtrl_date.SetValue(self.event[1])
        self.m_textCtrl_name.SetValue(self.event[0])
        self.m_textCtrl_ticket_row.SetValue(self.event[5])
        self.m_slider_interval.SetValue(int(self.event[3]))

