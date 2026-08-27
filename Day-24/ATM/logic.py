data={
    123456:{'pin':123,'balance':7000,'history':[]},
    234567:{'pin':234,'balance':3000,'history':[]},
    345678:{'pin':345,'balance':4909,'history':[]}

}


def menu():
    print('[C]heck Balance')
    print('[D]eposit ')
    print('[W]ithdrawl')
    print('[V]iew transaction')
    print('[E]xit')


def login():
    global acc_num
    acc_num=int(input("Enter the account number:"))
    pin=int(input('Enter the pin'))
    if