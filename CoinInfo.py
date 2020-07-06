class CoinInfo:
    name = ''
    price_usd = ''
    price_krw = ''
    price_diff = ''

    def __init__(self, name, price_usd, price_krw, price_diff):
        self.name = name
        self.price_usd = price_usd
        self.price_krw = price_krw
        self.price_diff = price_diff