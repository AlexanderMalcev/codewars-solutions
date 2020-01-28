#my codewars profile:https://www.codewars.com/users/Shichika%20Yasuri

def creating(name):
    dst = 'D:/Users/user/Desktop/codewars solutions'
    result = []
    digit = name[0]
    for word in name[2:]:
        result.append(word.replace(' ','_'))
    return f"{dst}/{digit}{''.join(result)}.py"

f = open(creating('name of a kata'), 'w+')
f.write('#solution')
f.close()
