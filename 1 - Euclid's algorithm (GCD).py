# find the greatest common denominator (GCD)
def gcd(x, y):
    a = x
    b = y
    r = a % b
    while (r != 0): 
        a = b
        b = r
        r = a % b
    return b

def main():
    a = 20
    b = 8
    print(f'\na = {a}, b = {b}, GCD = {gcd(a,b)}')

    a = 8
    b = 7
    print(f'\na = {a}, b = {b}, GCD = {gcd(a,b)}')

    a = 60
    b = 96
    print(f'\na = {a}, b = {b}, GCD = {gcd(a,b)}')

if __name__ == "__main__": main()