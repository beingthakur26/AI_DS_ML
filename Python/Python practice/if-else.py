# find even or odd

# n = int(input("Enter a number : "))

# if(n % 2 == 0):
#     print("N is even")
# else:
#     print("N is odd")


# print * in a pattern

# for i in range(1,6):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# check a number is prime or not

# n =int(input("Enter a number : "))

# if(n % 2 == 0):
#     print("It is not prime number.")
# else:
#     print("It is prime")


# print a pattern

n =int(input("Enter a number : "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()