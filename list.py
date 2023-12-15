list1 = ["","",""]
list2 = ["","",""]
list3 = ["","",""]
index_list = ["a", "b", "c"]
final_list = [list1, list2, list3]

user_input = input("where to? ")
ui = input("string: ")

final_list[int(user_input[-1])-1][index_list.index(user_input[0])] = ui
    
print(f"{list1}\n{list2}\n{list3}")