# Fibonacci sequence
def fib(count):
    fib_list = [1, 2]
    for i in range(2, count):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list


fib_count = int(input("Enter the number of fibonacci sequence: "))
print(fib(fib_count))

