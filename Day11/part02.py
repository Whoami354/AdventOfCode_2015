def is_valid(password):
    # Check if the password contains one increasing straight of at least three letters
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i + 1]) + 1 == ord(password[i + 2]):
            break
    else:
        return False

    # Check if the password does not contain the letters i, o, or l
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    # Check if the password contains at least two different, non-overlapping pairs of letters
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 2
        else:
            i += 1
    if len(pairs) < 2:
        return False

    return True


def increment_password(password):
    password = list(password)
    i = len(password) - 1
    while i >= 0:
        if password[i] == 'z':
            password[i] = 'a'
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    else:
        password = ['a'] * (len(password) + 1)
    return ''.join(password)


password = "vzbxkghb"
while is_valid(password) == False:
    password = increment_password(password)

password = increment_password(password)
while is_valid(password) == False:
    password = increment_password(password)
print("Santas next password is:", password)
