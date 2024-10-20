import wx

class ChazGpt(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Chaz(GPT)', size=(720, 900))
        
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.chat_display = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.message_input = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
        
        self.sizer.Add(self.chat_display, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.message_input, 0, wx.EXPAND | wx.ALL, 5)
        
        self.message_input.Bind(wx.EVT_TEXT_ENTER, self.on_send)

        self.panel.SetSizer(self.sizer)
        self.Show()

    def on_send(self, event):
        message = self.message_input.GetValue()

        if message:
            self.chat_display.AppendText(f"You: {message}\n")
            self.message_input.Clear()
            # send `message` to server/chatgpt api

if __name__ == '__main__':
    app = wx.App(False)
    ChazGpt()
    app.MainLoop()