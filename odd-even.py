def check():
    if (int(input("Enter the number please: ")) % 2 == 0):
        return "It is an even number."
    else:
        return "It is an odd number."

print(check())