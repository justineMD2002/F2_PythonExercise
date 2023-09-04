
def decToBinary(dec):
    res = ""
    while dec > 0:
        rem = dec % 2
        res = str(rem) + res
        dec = dec // 2
    return res

def binaryToN(bin, type):
    res = 0
    if type.lower() == "decimal":
        power = len(bin) - 1
        for i in bin:
            if i == "1":
                res += 2**i
            power -= 1
        return res

    elif type.lower() == "octal":
        temp = 0
        power = len(bin) - 1
        for i in bin:
            if i == "1":
                temp += 2 ** i
            power -= 1
        while temp > 0:
            rem = temp % 8
            oct = str(rem) + oct
            temp = temp // 8
        return oct

    elif type.lower() == "hexadecimal":
        decimal = 0
        power = len(bin) - 1
        for digit in bin:
            if digit == '1':
                decimal += 2 ** power
            power -= 1
        hexa = ""
        while decimal > 0:
            rem = decimal % 16
            hexa_dig = ""
            if rem < 10:
                hexa_dig = str(rem)
            else:
                hexa_dig = chr(ord('A') + rem - 10)
            hexa = hexa_dig + hexa
            decimal = decimal // 16
        return hexa

def decToOctal(dec):
    octal = ""
    while dec > 0:
        rem = dec % 8
        octal = str(rem) + octal
        dec = dec // 8
    return octal

def decToHex(dec):
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while dec > 0:
        remainder = dec % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        dec = dec // 16
    return hexadecimal


def main():
    print(decToBinary(10))
    print(binaryToN(1011, "hexadecimal"))
    print(decToOctal(10))
    print(decToHex(10))

if __name__ == "__main__":
    main()