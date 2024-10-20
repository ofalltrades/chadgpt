import wx
import socket
import threading


class ChazGpt(wx.Frame):
    def __init__(self, host="127.0.0.1", port=3000):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

    def OnInit(self):
        self.frame = wx.Frame(None, title="Chaz(GPT)", size=(720, 900))
        self.panel = wx.Panel(self.frame)

        self.chat_display = wx.TextCtrl(
            self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY
        )
        self.message_input = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
        self.send_button = wx.Button(self.panel, label="Send")
        self.message_input.Bind(wx.EVT_TEXT_ENTER, self.on_send)
        self.send_button.Bind(wx.EVT_BUTTON, self.on_send)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.chat_display, 1, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.message_input, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.send_button, 0, wx.EXPAND)
        self.panel.SetSizer(self.sizer)

        self.Show()
        return True

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr} has been established!")
            client_thread = threading.Thread(
                target=self.handle_client, args=(client_socket,)
            )
            client_thread.start()

    def on_send(self, event):
        message = self.message_input.GetValue()

        if message:
            self.chat_display.AppendText(f"You: {message}\n")
            self.send_message(message)
            self.message_input.Clear()

    def send_message(self, message):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", 3000))
        server_socket.listen(5)

    def handle_client(self, client_socket):
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Received: {message}")
        client_socket.close()


if __name__ == "__main__":
    app = ChazGpt()
    app.start()
