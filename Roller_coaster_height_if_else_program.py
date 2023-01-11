print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
  print('You can ride the rollercoaster!')
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are 5₹.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are 7₹.")
  else:
    bill = 18
    print("Adult tickets are 18₹.")

  wants_photo = input("Do you want a photo? Y or N. ")
  if wants_photo == "y":
    #add 3₹ to their bill
    bill += 3

  print(f'Your total bill is {bill}')
    
else:
  print("Sorry, you have to grow taller before you can ride.")