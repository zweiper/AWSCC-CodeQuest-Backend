high_limit = None

print("================================================================================================")
print("|                                                                                              |")
print("|                                         FizzBuzz!                                            |")
print("|                                                                                              |")
print("================================================================================================")

print("\nWelcome to FizzBuzz!")

print("\nRules of FizzBuzz:\n\t1. If a number is divisible by 3, you get a 'Fizz'\n\t2. If a number is divisible by 5, you get a 'Buzz'\n\t3. If a number is both divisible by 3 and 5, you get a 'FizzBuzz!'")

high_limit=int(input("\nEnter a number limit: "))

for i in range(high_limit):
    i+=1
    if i%3 == 0:
        if i%5 == 0:
            print("FizzBuzz!")
        else:
            print("Fizz")
    elif i%5 == 0:
        if i%3 == 0:
            print("FizzBuzz!")
        else:
            print("Buzz")
    else:
        print(f"{i}")