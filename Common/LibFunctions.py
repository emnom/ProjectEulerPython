def xth_prime(x):
    counting_tool = 0
    prime_list = [2]
    last_number = 2
    primes_found = 1
    while primes_found < x:
        last_number += 1
        for primes in prime_list[:]:
            if (last_number % primes) != 0:
                counting_tool += 1
        if len(prime_list) == counting_tool:
            prime_list.append(last_number)
            primes_found += 1
        counting_tool = 0
    return(prime_list[-1])
def to_xth_prime(x):
    counting_tool = 0
    prime_list = [2]
    last_number = 2
    primes_found = 1
    while primes_found < x:
        last_number += 1
        for primes in prime_list[:]:
            if (last_number % primes) != 0:
                counting_tool += 1
        if len(prime_list) == counting_tool:
            prime_list.append(last_number)
            primes_found += 1
        counting_tool = 0
    return(prime_list[:])
def multiples_below_x(number_below, number1):
    number_list = []
    for numbers in range(number_below):
        if ((numbers + 1) % number1) != 0:
            append.number_list(numbers)
    return number_list
def multiples_below_x_and_y(number_below, number1 , number2):
    number_list = []
    for numbers in range(number_below):
        if ((numbers + 1) % number1) == 0:
            number_list.append(numbers + 1)
        elif((numbers + 1) % number2) == 0:
            number_list.append(numbers + 1)
    return number_list