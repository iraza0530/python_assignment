
# ## 1. Write a program that asks the user how many Fibonnaci numbers to generate and then generates them

# number_times = int(input("Enter length of Fibonacci series: "))
# a = 0
# b = 1
# next_number = 0
# count = 1
  
# while(count <= number_times):
#     print(next_number, end=" ")
#     count += 1
#     a = b
#     b = next_number
#     next_number = a + b


# ##  2. Write a program to remove duplicate elements from a user given list.


# list_numbers = [1, 2, 3, 4, 2, 1, 9, 3,4]
# print(list(set(list_numbers)))


# ##  3.  Write a program to find squares of all elements of a user given list. It shall contain only numbers.

# list_numbers = [3,4,5]


# def  SquareListElements(list_numbers):
#     squaredList = []
#     for item in list_numbers:
#         squaredList.append(item ** 2)     
#     return squaredList
# print(SquareListElements(list_numbers))


# ##  4. Write a program to find the reverse of a user given number. E.g. 12345  54321


# num_to_be_reversed = int(input("Enter number to be reversed: "))
# reversed_num = 0

# while num_to_be_reversed != 0:
#     digit = num_to_be_reversed % 10
#     reversed_num = reversed_num * 10 + digit
#     num_to_be_reversed = num_to_be_reversed // 10

# print("Reversed Number: " + str(reversed_num))


# ## 5.  Find the sum of all the primes below 200,000. (e.g. The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17 )


# num = int(input("Enter number: "))

# def isPrime(x):
#     prime = True
#     for i in range(2, x):
#         if x % i == 0:
#             prime = False
#             break
#         else:
#             continue
#     return prime

# primes = (a for a in range(2, num)
#  if isPrime(a))
# print(sum(primes))

# import Practice_2

# Practice_2.printName('Imran Raza Khan')
# print(Practice_2.__dir__())

# class DisplayInformation:
#     'some docstring'

#     def __init__(self,school,city):
#         self.school = school
#         self.city  = city


#     def displayInf(self):
#         print("We study in school "+ self.school +" and the city is "+ self.city)

    
# displayInf = DisplayInformation("Thompson","Gonda")   

# displayInf.grade  = "First"
# print(displayInf.displayInf())
        
