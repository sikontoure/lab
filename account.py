class Account:
    def __init__(self, name: str) -> None:
        """
        Constructor to set up account object.
        :param name: Account name
        """

        self.__account_balance = 0
        self.__account_name = name

    def deposit(self, amount: float) -> bool:
        """
        Method to increase the balance by a specified amount.
        :param amount: Account balance
        :return: True if successful, False otherwise
        """
        if amount > 0:
            self.__account_balance += amount
            return True

        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Method to extract a specified amount from the balance.
        :param amount: Account balance
        :return: True if successful, False otherwise
        """

        if (self.__account_balance >= amount) or (amount <= 0):
            return False

        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        :return: Account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        :return: Account name
        """
        return self.__account_name







