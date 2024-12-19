def is_divisible_by_10():
    # Input the size of the array
    n = int(input("Enter the size of the array: "))

    # Input the array elements
    arr = list(map(int, input("Enter the array elements: ").split()))

    # Ensure the input array has the correct size
    if len(arr) != n:
        print("The number of elements entered does not match the size of the array.")
        return

    # Get the last digits of the numbers in the array
    last_digits = [num % 10 for num in arr]

    # Form the number by concatenating the last digits
    formed_number = int(''.join(map(str, last_digits)))

    # Check divisibility by 10
    if formed_number % 10 == 0:
        print("Yes")
    else:
        print("No")

# Run the function
is_divisible_by_10()