
# ჩვენს კოდს უფრო მარტივს და ხელმისაწვდომს ხდის ასევე ვიზუალურად უფრო ლამაზია მარტივი keyword აქვს ფუნქციები, გვიმარტივებს საქმეს მაგალითად ერთ ფუნქციაში, შეგვიძლია ბევრი argument ის იგივე პარამეტრის, ჩაშენება.


# რესურსისთვის უნდა გადგვეხედა

list = [1,2,3,4]
def double_values(list):
    for i in list:
        return i * 2
    
def num(list):
    if num % 2 == 0:
        return list
    
def powTwo(numbers):
    result = []

    for num in numbers:
        result.append(num * num)
    
    return result


print(powTwo([1,2,3]))

def filter(word):
    vowels = "aeiou"
    result = ""

    for char in word:
        if char in vowels:
            result += char
    
    return result


filter("guga")




def filter_positive(numbers):
    negative_numbers = []

    for number in numbers:
        if number < 0:
            negative_numbers.append(number)
    
    return negative_numbers

filter_positive([1,2,3,-5,-8,-10,7,11])



def filter(numbers):
    positive_numbers = []

    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    
    return positive_numbers

filter_positive([1,2,3,-5,-8,-10,7,11])
    
def math_operation(number):
    return (number ** 2) * 10

def x_and_y(x,y):
    return x ** y