import random

def generate_number():
    # Generate a list of all possible digits
    digits = list(range(10))
    
    # Shuffle the list of digits to get a random order
    random.shuffle(digits)
    
    # Take the first four digits from the shuffled list
    number = digits[:4]
    
    # Convert the list of digits to a single integer
    number = int("".join(map(str, number)))
    
    return number

def check_guess(number, guess):
    # Convert the number and guess to lists of digits
    number_digits = [int(d) for d in str(number)]
    guess_digits = [int(d) for d in str(guess)]
    
    # Count the number of digits that are in the right position
    num_correct_position = sum([1 for i in range(4) if number_digits[i] == guess_digits[i]])
    
    # Count the number of digits that are correct but in the wrong position
    num_correct_digit = sum([1 for d in guess_digits if d in number_digits]) - num_correct_position
    
    # Format the result as "xAyB"
    result = f"{num_correct_position}A{num_correct_digit}B"
    
    return result
