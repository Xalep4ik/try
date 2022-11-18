amount = 10
cookieprise = 8
candyprice = 7

rest = amount - cookieprise

if rest >= candyprice:
    print("I have enough money")
else:
    print("I haven't enough money ")


amount -= cookieprise
print("Amount is", amount)

if amount >= cookieprise:
    print("I nave money")
else:
    print("I haven't money")

type_x = type(amount)
print(type_x)

print(isinstance(amount, str))