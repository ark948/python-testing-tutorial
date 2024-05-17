
class InsufficientFund(Exception):
    pass

class BankAccount:
    def __init__(self, balance: float) -> None:
        if balance < 0:
            raise ValueError('Balance cannot be negative.')
        self._balance = balance # supposedly hidden

    @property
    def balance(self) -> float:
        return self._balance
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('The amount must be positive.')
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('The withdraw amount must be more than 0.')
        
        if amount > self._balance:
            raise InsufficientFund('Insufficient amount for withdrawal.')
        
        self._balance -= amount