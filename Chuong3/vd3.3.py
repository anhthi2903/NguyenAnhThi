y=int(input('yrsOfService = '))
s=int(input('salary = '))
b=int(input('bonus = '))
if y <5:
    if s < 500:
        bonus = 100
    else:
        bonus = 200
else:
    bonus = 700
print('Bonus amount:',bonus)