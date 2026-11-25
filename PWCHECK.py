import string

score = 0
pw = input("Enter password: ")


def length(pw):
    global score

    if len(pw) < 12:
        print("Too short")
        score -= 1
    else:
        print("Good job, it's long")
        score += 1

    return score


def numeric(pw):
    global score
    digitss = False

    for i in pw:
        if i.isdigit():
            digitss = True
            break

    if digitss:
        print("You got digits")
        score += 1
    else:
        print("No digits")
        score -= 1

    return score


def special(pw):
    global score
    special_char = False

    for i in pw:
        if i in string.punctuation:
            special_char = True
            break

    if special_char:
        print("Contains special character")
        score += 1
    else:
        print("Needs special character")
        score -= 1

    return score


def upper(pw):
    global score
    has_upper = False

    for s in pw:
        if s.isupper():
            has_upper = True
            break

    if has_upper:
        print("Good job")
        score += 1
    else:
        print("Need uppercase")
        score -= 1

    return score


def pwnd(pw):
    global score

    with open("worst_pw.txt", "r") as file:
        worstest_pw = [line.strip() for line in file]

    if pw in worstest_pw:
        print("Bad password")
        score -= 1
    else:
        print("Password not found")
        score += 1

    return score


length(pw)
numeric(pw)
special(pw)
upper(pw)
pwnd(pw)

print("Final score:", score)




