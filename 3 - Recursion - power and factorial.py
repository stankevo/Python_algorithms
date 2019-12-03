# power: 5ˆ4 = 5*5*5*5   5ˆ1 = 5
# factorial: 5! = 5*4*3*2*1      0! = 1

def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr - 1)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

def main():
    print('power({}, {}) = {}'.format(2,3,power(2,3)))
    print('power({}, {}) = {}'.format(2,1,power(2,1)))
    print('power({}, {}) = {}'.format(2,0,power(2,0)))
    print('power({}, {}) = {}'.format(1,5,power(1,5)))
    print('factorial({}) = {}'.format(0,factorial(0)))
    print('factorial({}) = {}'.format(1,factorial(1)))
    print('factorial({}) = {}'.format(5,factorial(5)))

if __name__ == '__main__': main()


