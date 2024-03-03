class Phone:

    phone_name=None
    phone_price=None
    def __init__(self,name,price):
        self.phone_name=name
        self.phone_price=price
    def call(self,number):
        return 'Hello'+number

