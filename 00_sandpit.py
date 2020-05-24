response = input("enter somthing: ")

try:
    float(response)

    response = int(response)
    print("You chose", response)

except ValueError:
    print("nope")

