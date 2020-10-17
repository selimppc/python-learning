numbers = [1, 2]

try:
    file = open("question1.py")
    # python will file.close() if we use with
    # we don't need finally clause.
    with open("question1.py") as file:
        print("File is openned.")
    age = abs(int(input("Age : ")))
    xfactor = 10 / age
    print(age)
except (ValueError, ZeroDivisionError):
    print(" You did not enter a valid age.")
else:
    print("Contibue programming")
