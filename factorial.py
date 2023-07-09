def main():
    v = int(input("Enter your value: "))
    print(factorial(v))


def factorial(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else :
        return n*factorial(n-1);

main()