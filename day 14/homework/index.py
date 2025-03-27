# name = "guga"
# print(name[1])
# print(name[3])

# False სტრინგები არის immutable და lists არის mutable

# ეს არასწორია რადგან ლისტებში შეგვიძლია შევცვალოთ რაიმე აპენდის მეშვეობით ხოლო სტრინგის არა
list = []
name = input("pls enter your name: ")
lastname = input("pls enter your lasname: ")
birthday = input("pls enter your birthday: ")
height = input("pls enter your height: ")
age = input("pls enter your age: ")
addres = input("pls enter your addres: ")
email = input("pls enter email: ")
password = input("pls enter your password: ")

list.append(name)
list.append(lastname)
list.append(birthday)
list.append(height)
list.append(age)
list.append(addres)
list.append(email)
list.append(password)
print(list)