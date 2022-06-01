import random

print('Mire se erdhe ne gjeneratotin e pasvordave ')

chars ='asdfghjklzxcvbnmqwertyuiopASDFGHJKLZXCVBNMQWERTYUIOP1234567890,.>?<!@#$%^&*'

number = input('sasia e pasvordeve qe do gjeneroni: ')
number = int(number)

length = input('Shkruaj gjatesin e pasvordit: ')
length = int(length)

print('\ketu janë pasvordat qe u gjeneruan: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
