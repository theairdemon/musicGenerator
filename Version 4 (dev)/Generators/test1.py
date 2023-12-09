test_dict = {(1, 0): 4}
print(test_dict[(1, 0)])


test_list = [1,2 ,3, 4, 5, 6, 7]
list2 = test_list[:3]
list3 = test_list[:3]

print(list2, list3)

list2[0] = 98123

print(list2, list3)

test_list[0] = "twenty-four"

print(list2, list3)