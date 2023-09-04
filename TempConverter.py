def num1_convert():
    try:
        num = input("Enter celsius: ")
        res = float(num) * 9/5 + 32
        print("Temperature in fahrenheit is: {:.2f}".format(res))
    except ValueError:
        print("Invalid Input!")