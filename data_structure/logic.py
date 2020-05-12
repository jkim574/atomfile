# wordlist = ['cat', 'dog', 'rat', 'elephant', 'monkey']
# letterlist = []
# for word in wordlist:
#     for letter in word:
#         if letter not in letterlist:

#             letterlist.append(letter)

# print(letterlist)

wordlist = ['cat','dog','rabbit']

print ([ch for ch in "".join(['cat', 'dog', 'rabbit'])])

alist =  [word[i] for word in ['cat', 'dog', 'rabbit'] for i in range (len(word))]
print (alist)

print (list(set(alist)))
