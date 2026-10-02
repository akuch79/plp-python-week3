count = 1
total = 0

# BUG: The while statement was missing a colon.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The original condition was count < 5, so 5 was not included.
# Changed it to count <= 5.

# BUG: A string cannot be directly joined with an integer.
# Converted total to a string using str().
print("Sum of 1 to 5 is: " + str(total))