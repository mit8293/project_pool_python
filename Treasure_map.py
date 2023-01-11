# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️",1]
row2 = ["⬜️","⬜️","️⬜️",2]
row3 = ["⬜️️","⬜️️","⬜️️",3]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])
print(horizontal,vertical)
row = map[vertical-1]
print(row)
print()
row[horizontal-1] = 'X'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

