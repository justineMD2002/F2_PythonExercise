def num2_max():
    try:
        for i in range(3):
            num = int(input(f"Enter num {i+1}: "))
            if i == 0 or num > maxx:
                maxx = num
        print(f"Highest number is: {maxx}")
    except ValueError:
        print("Invalid Input!")
