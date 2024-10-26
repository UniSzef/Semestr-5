class Card:
    def __init__(self, card_number: str, pin: str):
        self.card_number = card_number
        self.pin = pin
    def verify_pin(self, pin: str) -> bool:
        return self.pin == pin

class Account:
    def __init__(self, balance: float = 0.0):
        self.balance = balance

    def check_balance(self) -> float:
        return self.balance

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount: float) -> bool:
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

class User:
    def __init__(self, name: str, card: Card, account: Account):
        self.name = name
        self.card = card
        self.account = account

    def login(self, pin: str) -> bool:
        return self.card.verify_pin(pin)

class ATM:
    def __init__(self):
        self.logged_in_user = None

    def insert_card(self, user: User, pin: str) -> bool:
        if user.login(pin):
            self.logged_in_user = user
            print("Zalogowano pomyślnie.")
            return True
        print("Nieprawidłowy PIN.")
        return False

    def withdraw_cash(self, amount: float):
        if self.logged_in_user and self.logged_in_user.account.withdraw(amount):
            print(f"Wydano {amount} PLN.")
        else:
            print("Nie udało się wypłacić środków.")

    def deposit_cash(self, amount: float):
        if self.logged_in_user and self.logged_in_user.account.deposit(amount):
            print(f"Wpłacono {amount} PLN.")
        else:
            print("Nie udało się wpłacić środków.")

    def check_balance(self):
        if self.logged_in_user:
            balance = self.logged_in_user.account.check_balance()
            print(f"Saldo konta: {balance} PLN.")
        else:
            print("Brak zalogowanego użytkownika.")

    def transfer_funds(self, target_account: Account, amount: float):
        if self.logged_in_user and self.logged_in_user.account.transfer(target_account, amount):
            print(f"Przelano {amount} PLN.")
        else:
            print("Nie udało się wykonać przelewu.")

    def purchase_prepaid_code(self, amount: float):
        if self.logged_in_user and self.logged_in_user.account.withdraw(amount):
            print(f"Zakupiono kod pre-paidowy za {amount} PLN.")
        else:
            print("Nie udało się zakupić kodu pre-paidowego.")

card = Card("1234567890123456", "1234")
account = Account(1000)  # starting balance: 1000 PLN
user = User("Jan Kowalski", card, account)

atm = ATM()
atm.insert_card(user, "1234")

card1 = Card("1234567890123456", "1234")
account1 = Account(500)
user1 = User("Jan Kowalski", card1, account1)

atm = ATM()
atm.insert_card(user1, "1234")  # Logowanie użytkownika Jan Kowalski

atm.check_balance()             # Sprawdzenie salda
atm.deposit_cash(200)           # Wpłata 200 PLN
atm.check_balance()             # Saldo powinno wynosić 700 PLN

atm.withdraw_cash(150)          # Wypłata 150 PLN
atm.check_balance()             # Saldo powinno wynosić 550 PLN

atm.withdraw_cash(600)          # Próba wypłaty 600 PLN - brak wystarczających środków
atm.check_balance()             # Saldo powinno pozostać bez zmian (550 PLN)

atm.purchase_prepaid_code(50)   # Zakup kodu pre-paidowego za 50 PLN
atm.check_balance()             # Saldo powinno wynosić 500 PLN

atm.purchase_prepaid_code(350)
atm.check_balance()


atm.insert_card(user1, "5679")
atm.check_balance()
