# Cool Sequence! Always equate to 1 with all numbers!
try:
    num = int(input())
    if num > 0:
        while num != 1:
            print(int(num))
            if num % 2 == 0:
                num = num / 2
            elif num % 2 == 1:
                num = 3 * num + 1
            else:
                break
        print(int(num))
    else:
        print('Input value cannot be zero or negative!')

except ValueError:
    print('Input Error! Put a positive integer!')