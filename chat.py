class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def __str__(self):
        return f"[{self.sender.name}]: {self.text}"


class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(f"{user.name} joined '{self.room_name}'")

    def leave(self, user):
        self.users.remove(user)
        print(f"{user.name} left '{self.room_name}'")

    def send_message(self, sender, text):
        if sender in self.users:
            msg = Message(sender, text)
            self.messages.append(msg)
        else:
            print(f"{sender.name} is not in the room!")

    def view_history(self):
        print(f"\n--- Chat History: {self.room_name} ---")
        for msg in self.messages:
            print(msg)
        print("-------------------------------\n")


# ── Test ──
rahul = User("Rahul")
priya = User("Priya")
arjun = User("Arjun")

room = ChatRoom("Python Gang")

room.join(rahul)
room.join(priya)
room.join(arjun)

room.send_message(rahul, "Hey everyone!")
room.send_message(priya, "Hello Rahul!")
room.send_message(arjun, "What's up guys!")

room.leave(arjun)
room.send_message(arjun, "Anyone there?")  # not in room!

room.view_history()