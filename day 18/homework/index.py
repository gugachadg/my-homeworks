# count append clear insert pop

# list = ["guga", "giorgi"]
# list.insert(1,"Google")
# print(list)

# ჩვენ ინსერტით შეგვიძლია ჩავამატოდ რაც გვინდა სიაში და რომელ ინდექსზეც გვინდა
# list1 = [1,2,3,4,5,6,7,8,9]
# list1.append(10)
# print(list1)
# ჩენ აპენდით შეგვიძლია რომ დავამატოთ ნებისმიერი ბოლო ინდექსზე ანუ სიის ბოლოში
# list2 = ["apple","banana"]
# list2.clear()
# print(list2)
# clear ფუნქცია შლის ყველაფერს

# list3 = ["giorgi", "lasha","gogita"]
# list3.pop(2)
# print(list3)
# პოპ ფუნქცია სიიდან აგდებს იმ ინდექსზე მყოფ ელემენტს რომელიც მონიშნულია ინდექსინგის მეშვეობით

# list4 = [1,5,6,7]
# list4.count(3)
# print(list4)


list5 = [1,2,3,5]
def insert_add(list5):
    insert_add.insert(3,4)
    return insert_add

list6 = [1,2,3,5]
def append_add(list6):
    append_add.append(6)
    return append_add

list7 = [1,2,3,5]
def pop_out(list7):
    pop_out.pop(1)
    return pop_out

list8 = [1,2,3,5]
def copy_list(list8):
    copy_list.copy
    return copy_list

list9 = [1,2,3,5]
def clear_list(list9):
    clear_list.clear()
    return clear_list
    

list10 = [1,2,3,5]
def count(list10):
    count.count(1)
    return count

list11 = [1,2,3,4,5]   
user_input = input("do you want to clear this list: ")
if user_input == "yes":
    print(list11.clear())
else:
    print(list11)
    
    
fruit_list = ["banana","apple","mango","strawberrys"]
user_index = int(input("which fruit to delete say it with index: "))
if user_index == 0:
    print(fruit_list.remove("banana"))
elif user_index == 1:
    print(fruit_list.remove("apple"))
elif user_index == 2:
    print(fruit_list.remove("mango"))
elif user_index == 3:
    print(fruit_list.remove("strawberrys"))
    
print(fruit_list)
