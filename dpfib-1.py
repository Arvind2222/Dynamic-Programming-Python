def fibDP():
	fib = []
	fib.append(0)
	fib.append(1)
	_in = int(input("Enter the element"))
	for i in range(2,_in + 1):
		# fib = fib[i - 1] + fib[i - 2]
		# fib.append(i - 1) + fib.append(i - 2)
		fib.append(fib[i - 1] + fib[i - 2])

	return fib[_in]

def main():
	print(fibDP())


if __name__ == '__main__':
	main()
