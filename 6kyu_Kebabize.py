""" 
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters 
"""


#solution
def kebabize(string):
    result = ''
    for letter in string:
        if letter.isupper():
            result += '-' + letter.lower()
        elif letter.islower():
            result += letter
    return result.lstrip('-')