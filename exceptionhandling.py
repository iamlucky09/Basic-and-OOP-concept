# Exception Handling in python
try:
    a=int(input("Enter a number"))
    b=int(input("Enter another number"))
    c=float (a/b)

#yesle chai multiple exception throw garcha at once.
except (ZeroDivisionError , ValueError) as e:
    print("Cannot be divide by zero")

except ZeroDivisionError:
    print("Cannot be divide by zero")

except ValueError:
    print("Invalid input ,enter a number")

# using else block.when no exception occur then it will execute
else:
    print(c)

# finally block chai execute huncha huncha no matter the exception occur or not

# custom exception (raise)
def age(age):
    if age<18:
        raise ValueError("Age must be above 18")
    return "Access"
try:
    print(age(19))
except ValueError as e:
    print("Error:",e)