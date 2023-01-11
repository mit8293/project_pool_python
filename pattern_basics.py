#square
n=5
for i in range(n):#Outer row loop
    for j in range(n):#inner column loop
        print("*",end=" ")
    print()

# Increasing Triangle
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

# Decreasing Triangle
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

# Right side / Mirror increasing Triangle
for i in range(n):
    for j in range(i,n):# for decreasing space
        print(" ",end=" ")
    for j in range(i+1):# for increasing stars
        print("*",end=" ")
    print()

# Right side / Mirror decreasing Triangle
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

# Hill Pattern
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

#reverse Hill Pattern
# 1. Increasing space
# 2. decreasing stars
# 3. decreasing stars
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

#Diamond Pattern
# Merge increasing and decreasing hill pattern
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()