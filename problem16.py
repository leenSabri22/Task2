class ChatRoom:
    """Mediator class"""

    def show_message(self, sender, message):
        print(f"[{sender}]: {message}")


class User:
    def __init__(self, name, chatroom):
        self.name = name
        self.chatroom = chatroom

    def send_message(self, message):
        self.chatroom.show_message(self.name, message)


if __name__ == "__main__":
    chatroom = ChatRoom()

    user1 = User("user1", chatroom)
    user2 = User("user2", chatroom)
    user3 = User("user3", chatroom)

    user1.send_message("tets message from user1")
    user2.send_message("tets message from user2")
    user3.send_message("tets message from user3")
