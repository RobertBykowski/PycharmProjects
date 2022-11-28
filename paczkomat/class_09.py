class Message(object):
    def __init__(self, text):
        self.text = text

    def play_message(self):
        print(f"Twoje imię to {self.text}")

    def print_(self):
        t = self.text
        print(t.lower())

name_list = ["Robert","Bob","Agata"]
for name in name_list:
    message_1 = Message(name)
    message_1.play_message()

message_2 = Message("PrzyKładowy TeKSt")
message_2.print_()
