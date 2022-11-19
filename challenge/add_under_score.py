# Create three functions. The first called add_hash takes a string and adds a hash 
# between the words. The second function called add_underscore removes the 
# hash (#) and replaces it with an underscore "_" The third function called 
# remove_underscore, removes the underscore and replaces it with nothing. 
# if you pass ‘Python’ as an argument for the three functions, and you call them 
# at the same time like: print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.


def add_hash(a: str): 
    return "#".join(a)


def add_underscore(a: str):
    return str(a).replace("#", "_")


def remove_underscore(a: str): 
    return str(a).replace("_", "")

print(remove_underscore(add_underscore(add_hash('Py thon_r aja#'))))


# For this challenge you have to use the string() method, join() to add the 
# hash(#). Then you use another string method, replace() to replace the hash with an underscore 
# ( _ ) and we also use the replace method to replace the underscore with nothing.