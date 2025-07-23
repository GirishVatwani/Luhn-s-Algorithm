def main():

    number = 0
    while number < 1:
        number = int(input(("Number: ")))

    length = len(str(number))
    checksum = get_checksum(number, length)
    series = int(number/(10**(length-2)))

    if (checksum):
        if (length == 15) and (series == 34 or series == 37):
            print("VALID AMEX CARD")
        elif (length == 16) and (series in range(51, 56)):
            print("VALID MASTERCARD CARD")
        elif ((length == 13 or length == 16) and int(series/10) == 4):
            print("VALID VISA CARD")
        else:
            print("VALID CARD")
    else:
        print("INVALID CARD")


def get_checksum(number, length):
    num_sum = 0
    num = 0
    for i in range(length):
        num = number % 10

        if (i+1) % 2 == 0:
            num *= 2
            if num > 9:
                num_sum += num % 10
                num = int(num/10)
            num_sum += num

        else:
            num_sum += num
        number = int(number/10)

    if (num_sum % 10) == 0:
        return True
    else:
        return False


main()
