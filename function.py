def add(a,b):
   result = a+b
   return result


def subtract(a, b):
    print("%d minus %d is %d." %(a,b,a-b))

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

def add_multi(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
    elif choice == 'multiple':
        result = 1
        for j in args:
            result *= j
    return result

def say_nickname(nick):
    if nick == "whatever":
        return
    print("Your nickname is %s" % nick)

def myself(name,age,man=True):
    print("my name is %s" % name)
    print("I am %d years old." % age)
    if man:
        print("male")
    else:
        print("female")


if __name__ == '__main__':
    print(add(3,4))
    subtract(7,2)
    num = add_many(1,2,3,4,5)
    print(num)
   #
    idea = add_multi("add",2,3)
    print(idea)
    times = add_multi("multiple", 2,5,10)
    print(times)
   #
    say_nickname('sarge')
    myself("Joong Ho Kim", 27, True)
