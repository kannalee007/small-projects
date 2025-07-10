nums = list(map(int, input("Enter numbers separated by space: ").split()))

while True:
    print("\n=== List Analyzer Menu ===")
    print("1. Find Largest Number")
    print("2. Find Smallest Number")
    print("3. Sum of Even Numbers")
    print("4. Sum of Odd Numbers")
    print("5. Count Numbers Greater Than X")
    print("6. Find First Duplicate")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 7:
        print("Exiting... Goodbye!")
        break
    elif choice == 1:
        largest = largest[0]
        for i in nums:
            if i > largest:
                largest = i
        print("Largest number is:", largest)
    elif choice == 2:
        smallest = nums[0]
        for i in nums:
            if i < smallest:
                smallest = i
        print("Smallest number is:", smallest)
    elif choice == 3:
        sum_even = 0
        for i in nums:
            if i %2 == 0:
                sum_even += i
        print("Sum of even numbers is:", sum_even)
    elif choice == 4:
        sum_odd = 0
        for i in nums:
            if i % 2 !=0:
                sum_odd += i
        print("Sum of odd numbers is:", sum_odd)
    elif choice == 5:
        x = int(input("what is your x value:"))
        while x < nums or x > nums:
            print("x must be in the range of the numbers provided.")
            x = int(input("Please enter a valid x value: "))
        count_greater = sum(1 for i in nums if i > x)
        print("Count of numbers greater than", x, "is:", count_greater)
    elif choice == 6:
        seen = set()
        first_duplicate = None
        for i in nums:
            if i in seen:
                first_duplicate = i
                break
            seen.add(i)
        if first_duplicate is not None:
            print("First duplicate number is:", first_duplicate)
        else:
            print("No duplicates found.")
    else:
        print("You chose option", choice)