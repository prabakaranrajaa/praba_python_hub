# Pay Your Tax
# Write a function called your_vat. The function takes no parameter. 
# The function asks the user to input the price of an item and VAT (vat should be a percentage).
# The function should return the price of the item plus VAT. If the price is 220 and, VAT is 15% 
# your code should return a vat inclusive price of 253. Make sure that your code can handle ValueError. 
# Ensure the code runs until valid numbers are entered. (hint: Your code should include a while loop).


def your_vat(): 
    while True:
        try:
            price = int(input("Enter the price of item: ")) 
            vat = int(input('Enter vat: '))
        except ValueError:
            print("Enter a valid number") 
        else:
            total_price = price + \
            (price * vat / 100 + 1) - 1
            return 'The price VAT inclusive is', total_price


print(your_vat())


# In this challenge, you get to use typecasting, the input() function, and the try and except blocks to handle errors. 
# The input from the user is always in string format, so we use the int() function to convert it into an integer. 
# The except block ensures that we handle the ValueError. 
# We have added the while loop to ensure that the code runs until valid numbers are entered.
