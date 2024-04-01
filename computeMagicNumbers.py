# Austin Blair
# Building Tomorrow's Software
# 9/28/2020
# computeMagicNumbers
print('*' * 50)
user_input = input('Please enter a word. \n'
                   '-->')
print('*' * 50)


# 1 2 3 4 5 ... ! @ # $ % ^ .... a b c d e ... A B C D...

def getEquivalentNumber(_Mychar):
    _Mychar = _Mychar.lower()
    equivalentNumber = ord(_Mychar) - 96

    return equivalentNumber


# Define a function for the word
def computeSumOfCharacters(myWord):
    sum = 0
    for i in myWord:  # apple
        sum += getEquivalentNumber(i)

    return sum


print(computeSumOfCharacters(user_input))
