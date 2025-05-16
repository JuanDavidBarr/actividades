#Custom greeting
def custom_greeting(name):
    return print(f"Hello {name}, How is it going?")

custom_greeting("maría")

#Add two numbers
def adding_2_numbers(num1,num2):
    result = num1 + num2
    return print(result)

adding_2_numbers(3,5)

#Odd and even
def odd_even():
    flag = False
    while not flag:
        try:
            number = int(input("Introduce a number: "))
            if number % 2 == 0:
                print(f"{number} is even")
                flag = True
            else:
                print(f"{number} is odd")
                flag = True
        except:
            input("Please, numbers only")
odd_even()

#Is adult
def is_adult(age):
    if age >= 18:
        print("You are an adult")
    elif 0 <= age < 18:
        print("You are underage")
    else:
        print("Incorrect value")

is_adult(5)

#Temperature converter
def temperature_converter():
    flag = False
    while not flag:
        try:
            T_celcius = float(input("Introduce a temperature in Celcius (°C): "))
            T_farenheit = T_celcius + 32
            flag = True
        except:
            input("Please, numbers only")
    print(f"{T_celcius}° in farenheits is {T_farenheit} ")

temperature_converter()

#Area of a triangle
def triangle_area(base,height):
    result = (base * height) / 2
    return print(f"The area of a triangle whose base is {base} and height is {height} is {result}")

triangle_area(8,10)

#largest from a list
def largest_num_list(list):
    list_lenght = len(list)
    largest_num = 0
    for x in range(list_lenght-1):
        if list[x] > largest_num:
            largest_num = list[x]

    return print(f"the largest numbers is {largest_num}")

list = [2,8,1,6,9,25,100,4,7,8]

largest_num_list(list)

#how many times a letter on a string
def how_many_times(word,letter):
  result = word.count(letter)
  return print(f"{letter} is {result} in the word {word}")

how_many_times("knowledge","e")

#Even number
def even_number(list):
    even_number_list = []
    for element in list:
        if element % 2 == 0:
            even_number_list.append(element)
    for element in even_number_list:
        print(element)

list = [35,48,62,101,104,45]
even_number(list)

#Palindroma
def palindroma(word):
    a = word
    is_palindroma = False
    counter = -1
    for element in a:
        if element == a[counter]:
            is_palindroma = True
        counter -= 1
    if is_palindroma == True:
        print(f"{word} is palindroma")
    else:
        print(f"{word} is not palindroma")

palindroma("reconocer")

#Factorial
def factorial(number):
    counter = 2
    for x in range(1):
        result = number * (number - 1)
        for x in range(number - 2):
            result *= number - counter
            counter += 1
    return print(result)
            
factorial(5)

#Remove repited number
def remove_duplicated(lista):
    for element in lista:
        if lista.count(element) > 1:
            lista.remove(element)
    return print(lista)


lista = [1,8,8,2,5,9,9,1,4,5,63,8]
remove_duplicated(lista)

