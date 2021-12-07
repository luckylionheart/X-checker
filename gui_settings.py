import pickle

import wx
import wx.xrc


class SettingsDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(308, 280), style=wx.DEFAULT_DIALOG_STYLE)

        with open('settings.pickle', 'rb') as f:
            self.saved_settings = pickle.load(f)
            self.proxy = self.saved_settings['Proxy']
            print(self.proxy)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_proxies_button = wx.Button(self, wx.ID_ANY, u"Select Proxies", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_proxies_button.Bind(wx.EVT_BUTTON, self.select_proxies)
        bSizer11.Add(self.m_proxies_button, 0, wx.ALL, 5)

        proxies_label_text = self.proxy
        print(proxies_label_text)
        self.m_proxies_label = wx.StaticText(self, wx.ID_ANY, proxies_label_text, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_proxies_label.Wrap(-1)
        bSizer11.Add(self.m_proxies_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Gmail Email:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer4.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_gmail_email_input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
        bSizer4.Add(self.m_gmail_email_input, 0, wx.ALL, 5)

        bSizer10.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer41 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText21 = wx.StaticText(self, wx.ID_ANY, u"Gmail Pass:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)
        bSizer41.Add(self.m_staticText21, 0, wx.ALL, 5)

        self.m_gmail_pass_input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1),
                                              wx.TE_PASSWORD)
        bSizer41.Add(self.m_gmail_pass_input, 0, wx.ALL, 5)

        bSizer10.Add(bSizer41, 1, wx.EXPAND, 5)

        bSizer42 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText22 = wx.StaticText(self, wx.ID_ANY, u"Notify Email:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)
        bSizer42.Add(self.m_staticText22, 0, wx.ALL, 5)

        self.m_notify_email_input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1),
                                                0)
        bSizer42.Add(self.m_notify_email_input, 0, wx.ALL, 5)

        bSizer10.Add(bSizer42, 1, wx.EXPAND, 5)

        bSizer_threads = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_threads = wx.StaticText(self, wx.ID_ANY, u"# of Threads:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_threads.Wrap(-1)
        bSizer_threads.Add(self.m_staticText_threads, 0, wx.ALL, 5)

        self.m_threads_input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1),
                                                0)
        bSizer_threads.Add(self.m_threads_input, 0, wx.ALL, 5)

        bSizer10.Add(bSizer_threads, 1, wx.EXPAND, 5)

        bSizer_headless = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText_headless = wx.StaticText(self, wx.ID_ANY, u"Headless Browser:", wx.DefaultPosition, wx.DefaultSize,
                                                  0)
        self.m_staticText_headless.Wrap(-1)
        bSizer_headless.Add(self.m_staticText_headless, 0, wx.ALL, 5)

        self.m_headless_checkbox = wx.CheckBox(self)
        bSizer_headless.Add(self.m_headless_checkbox, 0, wx.ALL, 5)

        bSizer10.Add(bSizer_headless, 1, wx.EXPAND, 5)


        bSizer1.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_save_button = wx.Button(self, wx.ID_OK, u"Save Settings", wx.DefaultPosition, wx.Size(130, -1), 0)
        bSizer12.Add(self.m_save_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_cancel_button = wx.Button(self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.Size(154, -1), 0)
        bSizer12.Add(self.m_cancel_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer1.Add(bSizer12, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        self.load_settings()

    def select_proxies(self, event):
        openFileDialog = wx.FileDialog(self, "Open", "", "",
                                       "Text files (*.txt)|*.txt",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()
        self.proxy = openFileDialog.GetPath()
        self.m_proxies_label.SetLabel(self.proxy)

        openFileDialog.Destroy()

    def load_settings(self):
        self.m_gmail_email_input.SetValue(self.saved_settings['GmailEmail'])
        self.m_gmail_pass_input.SetValue(self.saved_settings['GmailPass'])
        self.m_notify_email_input.SetValue(self.saved_settings['NotifyEmail'])
        try:
            self.m_threads_input.SetValue(self.saved_settings['Threads'])
        except KeyError:
            self.m_threads_input.SetValue('4')

        try:
            self.m_headless_checkbox.SetValue(self.saved_settings['Headless'])
        except:
            self.m_headless_checkbox.SetValue(True)

        proxies_label_text = self.saved_settings['Proxy']
        self.m_proxies_label.SetLabel(proxies_label_text)

    def get_data(self):
        return {
            "GmailEmail": self.m_gmail_email_input.GetValue(),
            'GmailPass': self.m_gmail_pass_input.GetValue(),
            'NotifyEmail': self.m_notify_email_input.GetValue(),
            'Threads': self.m_threads_input.GetValue(),
            'Proxy': self.proxy,
            'Headless': self.m_headless_checkbox.GetValue()
        }

    def __del__(self):
        pass
