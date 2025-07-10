def is_prime(num):
    """
    Checks if a given number is a prime number.

    Args:
        num: An integer.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False  
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime


number_to_check = int(input("Enter a number: "))

if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")

    