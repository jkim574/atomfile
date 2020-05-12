# temp = {'id':'test', 'password': 'qwer'}
# a = {}
# for k,v in temp.items():
#     print(k,v)
#     a[k] = v
# print(a)


# there is not cow
# names = ['Joong', 'Sun', 'Sat', 'Moon']

# list_counts = {}

# for i, name in enumerate(names):
#     list = ['Min', 'Mon', 'spelling'], [1, 2, 3, 4], ["college", 'Marine', 'English']
#     print("%d : %s" % (i, name))
#     list_counts[i] = list
# print(list_counts)

# class BusinessCard(object):
#     def __init__(self, name, email, address):
#         self.name = name
#         self.email = email
#         self.address = address

#     def print_info(self):
#         print("name is: ", self.name)
#         print("email is : ", self.email)
#         print("address is: ", self.address)

# member1 = BusinessCard("Joong", "jkim574@wisc.edu", "Seoul")
# member1.print_info()


class Foo:
    def function1():
        print("function1")



    def function2(self):
        print(id(self))
        print("function2")
        print()




f = Foo()
#print(id(f))
print(Foo.function2())
