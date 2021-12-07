print('Welcome to the tip calculator!')
print()
billValue = float(input('What was the total bill? '))
numberOfPeople = int(input('How many people to split the bill? '))
tipValue = int(input('What percentage tip would you like to give (10, 12 or 15)? '))
percentageTip = tipValue/100
total = billValue*(1+percentageTip)/numberOfPeople;
print()
print(f'Each person should pay: ${round(total,2)}')