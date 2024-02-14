while True:
    mode = input("Enter mode (LCM/GCF/Stop): ")
    
    if mode == "Stop":
        print("Program stopped.")
        break
    
    if mode not in ["LCM", "GCF"]:
        print("Invalid mode. Please enter either 'LCM', 'GCF', or 'Stop'.")
        continue
    
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")
    
    if mode == "LCM":
        a, b = num1, num2
        while b:
            a, b = b, a % b
        lcm = (num1 * num2) // a
        print("LCM:", lcm)
    else:
        a, b = num1, num2
        while b:
            a, b = b, a % b
        gcf = a
        print("GCF:", gcf)

while True:
    passage = input("Enter a passage of at least 200 characters: ")
    
    if len(passage) < 200:
        print("Passage is too short. Please enter a passage with at least 200 characters.")
        continue
    
    character = input("Enter a character: ")
    
    if len(character) != 1:
        print("Invalid input. Please enter a single character.")
        continue
    
    count = 0
    for char in passage:
        if char == character:
            count += 1
    
    if count == 0:
        print(f"The character '{character}' is not found in the passage.")
    else:
        print(f"Number of occurrences of '{character}' in the passage: {count}")
