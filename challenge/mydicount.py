# Create a function called my_discount.
# The function takes no arguments but asks the user to input the price and the discount (percentage) of the product.
# Once the user inputs the price and discount, it calculates the price after the discount.
# The function should return the price after the discount.
# For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.

def my_discount():
    price = int(input('Enter the price: '))
    discount = int(input('Enter the discount: '))
    aft_dsc = price * (100-discount)/100
    return 'Price after discount is ', aft_dsc


print(my_discount())


# In this code, our function takes no parameters. We ask the user for input using the input() function.
# Since the input is in string format, we convert it to an integer using the int() function before we can calculate the discount.
# The output in this code assumes the input price of 150 and a discount of 15%.
