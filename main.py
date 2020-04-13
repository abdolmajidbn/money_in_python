class add_coma_in_money:
    def __init__(self, money):
        self.money = money

    def add_coma(self):
        self.money = float(self.money)
        amount_format = "{:,.0f}".format(self.money)
        return amount_format

    def remove_coma(self):
        money_str = str(self.money)
        remove_coma_in_money = money_str.replace(",", "")
        return remove_coma_in_money


