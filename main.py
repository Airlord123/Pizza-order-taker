print("Thank you for choosing Python Pizza Deliveries!")
size = input('\nWhat size pizza do you want? S, M, or L: ') 
add_pepperoni = input('\nAdd pepperoni? Y or N: ') 
extra_cheese = input('\nDo u want extra cheese: ')  
Bill= 0
if size == 'S':
  Bill = Bill + 15
  if add_pepperoni == 'Y':
    Bill = Bill + 2
  elif add_pepperoni == 'N':
    Bill = Bill 
  if  extra_cheese == 'Y':
    Bill = Bill + 1
  elif extra_cheese == 'N':
    Bill = Bill 
elif size == 'M':
  Bill= Bill + 20
  if add_pepperoni == 'Y':
    Bill = Bill + 3
  elif add_pepperoni == 'N':
    Bill = Bill
  if  extra_cheese == 'Y':
    Bill = Bill + 1
  elif extra_cheese == 'N':
      Bill = Bill 
elif size =='L':
  Bill = Bill + 25
  if add_pepperoni == 'Y':
    Bill = Bill + 3
  elif add_pepperoni == 'N':
    Bill = Bill
  if  extra_cheese == 'Y':
    Bill = Bill + 1
  elif extra_cheese == 'N':
    Bill = Bill
else:
  print ('Invalid input')

print(f'\nYour final bill is: ${Bill}')
