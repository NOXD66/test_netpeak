my_list = [46, 33, 10, 99, 73, 84, 47, 100, 52, 88, 21]

for i in range(my_list[-1]):
        for j in range(my_list[-i-1]):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print(my_list)






# for x in range(len(my_list)):
#     for y in range(len(my_list)):
#
#         if my_list[x] < my_list[y]:
#             my_list[x], my_list[y] = my_list[y], my_list[x]
#
# print(my_list)


# text = "abcdefghijklmnopqrstuvwxyz"
# b = [x for x in text]
# d = {a: b[a-1] for a in range(1, len(b)+1)}
# print(d)

# list_1 = ["print", print]
# print (list_1[])
# text = "dworlds all worlds is world"

# for x in range(3, 6):
#     print(x)
#
# #     # Prints out the numbers 0,1,2,3,4
# # for x in range(5):
# #     print(x)
#
# # Prints out 3,4,5
# for x in range(3, 6):
#     print(x)

# # Prints out 3,5,7
# # for x in range(0, 13):
# data = [-33, 68, -5, -65, 47, -55, -36, 85, -6, 50]
# #
# data = [x for x in data if x >= 0]
#
#
# my_list = [x for x in range(0, 13) if x != 6 and x!= 7]

# length = len(data)
# i = 0
# while i < len(data):
#     if data[i] < 0:
#         data.remove(data[i])
#         #length -= 1
#     else:
#         i += 1
# print(my_list)

# text = text.split()
# //print(bool(text.find(word + " ") + 1))

# if text.find(word) != -1:
#     a = bool(text.find(word))
#     print("kek")
#     print(a)

# for text in text.split():
#     if word == text:
#         a = 1
# return a

# print("oops")
# print(text.split())
