




with open('personality.txt', 'r') as file:
    content = file.readlines()
    names = []
    personality_test = []

    for i in range(len(content)):
       if i % 2 == 0:
           names.append(content[i].rstrip('\n'))
       else:
           personality_test.append(content[i].rstrip('\n'))

    print(personality_test)
    print(personality_test[0])
    my_list = [0, 0, 0, 0]
    for j in range(10):
       # print(personality_test[3][j * 7])
        if personality_test[0][j * 7].upper() == 'A':
            my_list[0] += 1
#        print(personality_test[0][(j * 7) + 1])
        for k in range(1, 3):
            if personality_test[0][(j * 7) + k].upper() == 'A':
                my_list[1] += 1
        for k in range(3, 5):
            if personality_test[0][(j * 7) + k].upper() == 'A':
                my_list[2] += 1
        for k in range(5, 7):
            if personality_test[0][(j * 7) + k].upper() == 'A':
                my_list[3] += 1
    print(my_list)







# # Returns number of times a specific answer was recordedin each of the four categories.
# def sort_answers(answers, char):
#     my_list = [0, 0, 0, 0]
#     for i in range(10):
#         if answers[i * 7].upper() == char:
#             my_list[0] += 1
#         for j in range(3):
#             for k in range(1, 3):
#                 if answers[i*7 + j*2 + k].upper() == char:
#                     my_list[j+1] += 1
#     return my_list


# # Returns percentage of B answers in the Keirsey test to determine a personality type
# def percent_of_B(A_list, B_list):
#     result = []
#     for i in range(len(B_list)):
#         percentage = int(round(float(B_list[i] / (A_list[i] + B_list[i]) * 100)))
#         result.append(percentage)
#     return result





# def main():
#     intro()
#     input_file = input("input file name? ")
#     output_file = input("output file name? ")
#     fo = open(input_file, 'r')
#     fw = open(output_file, 'w')
#     content = fo.readlines()
#     names = []
#     personality_test = []
#     for i in range(len(content)):
#         if i % 2 != 0:
#             personality_test.append(content[i].rstrip('\n'))
#         else:
#             names.append(content[i].rstrip('\n'))
#     ppl_count = 0
#     while ppl_count < len(names):
#         A_response = sort_answers(personality_test[ppl_count], 'A')
#         B_response = sort_answers(personality_test[ppl_count], 'B')
#         overall_B = percent_of_B(A_response, B_response)
#         personality = extract_personality(overall_B);
#         data = names[ppl_count] + ": " + str(overall_B) + " = " + personality  + "\n";
#         fw.write(data);
#         ppl_count+= 1;

#     fo.close();
