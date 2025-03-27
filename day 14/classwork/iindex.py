# numbers = []

# for i in range(5):
#     number = int(input("Please enter a number: "))
#     numbers.append(number)

# for number in numbers:
#     if number % 2 == 0:
#         print(number, "is even")
#     else:
#         print(number, "is odd")
    
# names = []

# for i in range(5):
#     name = input("Please enter a number: ")
#     names.append(name)


# for name in names:
#     if len(name) > 5:
#         print(name)
        
        
# healthy_products = ["Tomato", "Apple", "Orange", "Alucha", "Cucumber"]

# healthy_products.pop(0)
# healthy_products.pop()

# print(healthy_products)



list = [5,3,2,1,7]
sn = sorted(list)
for i in sn:
    if sn.count(i) == 1:
        x = i
        break
print(x)

list = [1,2,3,4,5]
print(list[2])