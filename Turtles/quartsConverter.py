quarts = input("Enter a positive number of quarts:")

quarts = int(quarts) #Converts quarts input from str to int to save time
ounces = (quarts * 32)
barrel = (quarts // 168)
barrelRemainder = (int(quarts) % 168)

if (quarts < 0):
    print("Please make sure you are using a positive number.")
else:
    print(f"Quart(s): {quarts}. Which is:\n{barrel} barrel(s) and {barrelRemainder} quarts,\nor,\n{ounces} ounces")




