try:
    num = int(input("enter any number"))
    print(f"you entered: {num}")

except ValueError:
    print("you did not enter a numerical value")
