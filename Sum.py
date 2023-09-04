def num4_sum():
    sum = 0
    try:
        rens = int(input("Enter number: "))
    except ValueError:
        print("Invalid Input!")
    for i in range(1, rens+1):
        sum += i
    print(sum)
