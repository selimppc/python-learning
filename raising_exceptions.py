# Raising exceptions

# try:
#     file = open("question1.py")
#     # python will file.close() if we use with
#     # we don't need finally clause.
#     with open("question1.py") as file:
#         print("File is openned.")
#     age = abs(int(input("Age : ")))
#     xfactor = 10 / age
#     print(age)
# except (ValueError, ZeroDivisionError):
#     print(" You did not enter a valid age.")
# else:
#     print("Contibue programming")


def calcualte_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be zero or less.")
    return 10/age


try:
    calcualte_xfactor(-1)
except ValueError as error:
    print(error)


# cost of raising exceptions
