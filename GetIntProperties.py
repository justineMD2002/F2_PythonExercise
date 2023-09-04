def num3_count():
    ctr = 0
    try:
        tine = int(input("Please enter a number: "))
    except ValueError:
        print("Invalid Input!")
    while tine != 0:
        nums = tine % 10
        if ctr == 0 or nums > maxx:
            maxx = nums
        if ctr == 0 or nums < minn:
            minn = nums
        tine //= 10
        ctr += 1
    print(f"Number of digits in the given number is: {ctr}")
    print(f"Smallest number is: {minn}")
    print(f"Highest number is: {maxx}")