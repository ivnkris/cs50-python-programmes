# import get_string function from cs50 library
from cs50 import get_string

# save user's answer into variable
answer = get_string("What's your name? ")
# print formatted string
print(f"hello, {answer}")