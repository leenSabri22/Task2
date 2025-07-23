class VendingMachine:
    def __init__(self):
        self.idle = Idle(self)
        self.has_money = HasMoney(self)
        self.state = self.idle

    def insert_coin(self):
        self.state.insert_coin()

    def set_state(self, state):
        self.state = state


class Idle:
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("idle")
        self.machine.set_state(self.machine.has_money)


class HasMoney:
    def __init__(self, machine):
        self.machine = machine

    def insert_coin(self):
        print("Already has money.")


if __name__ == "__main__":
    vm = VendingMachine()
    vm.insert_coin()
    vm.insert_coin()
