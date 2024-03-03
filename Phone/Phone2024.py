from  Phone import Phone
class Phone2024(Phone):
    call_5g=None
    def __init__(self,name,price,call_5g):
        super().__init__(name,price)
        self.call_5g=call_5g
    def get_call_5g(self):
        return self.call_5g

phone=Phone2024('iphone15',15999,True)
print(phone.get_call_5g())