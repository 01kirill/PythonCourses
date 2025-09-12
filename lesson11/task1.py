class BankAccount:
    def __init__(self, owner, balance):
        self.name = "AlphaBank"
        self.owner = owner
        self.balance = balance

    def _secret_message(self):
        print(f"Добро пожаловать в {self.name}")

    def show_info(self):
        self._secret_message()
        print(f"Счет: {self.owner}, баланс: {self.balance}")

    def __del__(self):
        print(f"Счет {self.owner} закрыт")

    def __call__(self, amount):
        self.balance += amount

    def __mul__(self, n):
        self.list = [BankAccount(self.owner, self.balance) for _ in range(n)]
