def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1

    return fib(x-1) + fib(x-2)

    

def main():
    print(fib(int(input("Enter the number: "))))


if __name__ == '__main__':
	main()
