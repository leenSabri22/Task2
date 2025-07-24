#  interface
class Observer:
    def update(self, data):
        pass


class Subscriber:
    def __init__(self):
        self._observers = []

    def add_subscriber(self, observer):
        self._observers.append(observer)

    def remove_subscriber(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)


class EmailNotifier(Observer):
    def update(self, user, filename):
        print(f"Email sent to {user} confirming upload of {filename}")


class Logger(Observer):
    def update(self, user, filename):
        print(f"[LOG] {user} uploaded {filename}")


class DashboardUpdater(Observer):
    def update(self, user):
        print(f"Dashboard updated for {user}")


class FileUploader(Subscriber):
    def upload_file(self, user, filename):
        print(f"{user} uploaded {filename}")
        self.notify_observers((user, filename))


def main():
    uploader = FileUploader()

    uploader.add_subscriber(EmailNotifier())
    uploader.add_subscriber(Logger())
    uploader.add_subscriber(DashboardUpdater())

    uploader.upload_file("leen", "test.pdf")


main()
