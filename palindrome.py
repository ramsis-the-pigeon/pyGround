def highestValuePalindrome(n, k, s):
    digits = list(s)
    
    #Split the string into two parts
    half = n // 2
    
    #Make the string a palindrome
    changes = 0
    for i in range(half):
        if digits[i] != digits[n - 1 - i]:
            # Change the smaller digit to the larger one
            larger_digit = max(digits[i], digits[n - 1 - i])
            digits[i] = digits[n - 1 - i] = larger_digit
            changes += 1
    
    # If the changes exceed k, return -1 (not possible to create palindrome)
    if changes > k:
        return "-1"
    
    #Maximize the palindrome by turning digits to the largest possible
    remaining_changes = k - changes
    for i in range(half):
        if digits[i] != larger_digit:  # We only want to change digits that are not '9'
            if digits[i] == digits[n - 1 - i]:
                # If they are the same, it takes 2 changes to make both '9'
                if remaining_changes >= 2:
                    digits[i] = digits[n - 1 - i] = larger_digit
                    remaining_changes -= 2
            else:
                # If they are different, we already made them equal, and we can make them '9'
                if remaining_changes >= 1:
                    digits[i] = digits[n - 1 - i] = "9"
                    remaining_changes -= 1
    
    #Handle the middle character if the string length is odd and there are remaining changes
    if n % 2 == 1 and remaining_changes > 0:
        digits[half] = larger_digit
    
    # Return the final palindrome as a string
    return ''.join(digits)





n, k = map(int, input("Enter the number of digits and the maximum number of changes, separated by space: ").split())
s = input("Enter the string of digits : ")

print(highestValuePalindrome(n, k, s))
