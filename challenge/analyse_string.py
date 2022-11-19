# Words & Special Characters Write a function called analyse_string that returns the number of special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words, and, total characters (all letters and special characters minus whitespaces) in a string. Return everything in a dictionary format:

# {“special character”: “number”, “words”: “number”, “total characters”: “number”}

# Use the string below as an argument:

# “Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".

# Source Wikipedia.


import string


def char(a):
    special_cha = []
    numeric_cha = []
    d = {
        'numeric': '',
        'special_cha': '',
        'total_char': ''
    }

    for i in a.replace(' ', ''):
        if i in string.punctuation:
            if i not in special_cha:
                special_cha.append(i)
            d['special_cha'] = len(special_cha)

        if i in string.digits:
            if i not in numeric_cha:
                numeric_cha.append(i)
            d['numeric'] = len(numeric_cha)
        else:
            d['total_char'] = len(a.replace(' ', ''))
    return d


print(char('Python has a string format operator %. '
           'This functions analogously to '
           'printf format strings in C, e.g.'
           '"spam=%s eggs=%d" % ("blah", 2) '
           'evaluates to "spam=blah eggs=2?'))


# We are using the string module to generate all the elements that we are looking for in the string. We have created variables for special characters (specia_cha) numeric characters(numeric_cha) and the d variable for our dictionary. The replace() method is to get rid of all the whitespaces between string elements.
