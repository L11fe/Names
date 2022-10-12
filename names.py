names = ['Anna', 'Arturs', 'Eliza', 'Krista']
ages = [22, 19, 12, 18]

#for number in range(len(names)):
#    print(f'{names[number]} is {ages[number]} years old')

#UZDEVUMS 1: izveido kodu kas izvadīs:
#Anna has 4 letters in the name
#Arturs has 6 letters in the name
#...

print('Te būs kods ar indeksiem')
print('======================================')
for i in range(len(names)):
    print(f'{names[i]} has {len(names[i])} letters in the name.')

print('Bet, šis kods izmanto vienu mainīgo')
print('======================================')
for name in names:
    print(f'{name} has {len(name)} letters in the name.')
