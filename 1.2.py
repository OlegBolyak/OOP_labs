class Subscriber:
    def __init__(self, number: str, name: str):
        self.number=number
        self.name=name
    def return_user(self): 
       
        return self.name, self.number
class SMS:
    def __init__(self, user: list, txt):
        self.user=user
        self.txt=txt
        self.sms={}  
    def send_sms(self):
        self.sms[self.user]=self.txt
        return self.sms
class Balance:
    def __init__(self, balance):
        self.balance=balance
    def user_balance(self, sms: dict): 
        for k,v in sms.items():
            if sms[k]=='':
                return f'''Користувач: {list(sms.keys())}\nbalance: {self.balance}\nвідсутнє повідомлення, оплату не знято'''
        self.balance=self.balance-5
        n=list(sms.keys())
        return f'''Користувач: {n}\nbalance: {self.balance}'''
user1=Subscriber("+380978767383", 'qwerty').return_user()
txt1=''
txt2='hello'
sms1=SMS(user1, txt1).send_sms()
sms2=SMS(user1, txt2).send_sms()
balance_user1=Balance(300)
print(balance_user1.user_balance(sms1))
print(balance_user1.user_balance(sms2))


