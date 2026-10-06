# A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits. For example, 153 is a narcissistic number because it has 3 digits and 1^3 + 5^3 + 3^3 = 153.
# This program will check if the inputted number is a narcissistic number.

print("Hello! This program will check if your number is a narcisstic number.\nA narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits.")

running = True

while running == True:
    if __name__ == "__main__":
        number = int(input("What number would you like to check? "))
        num_list = list(str(number))
        power = len(num_list)
        answer = 0
        for num in num_list:
            num = int(num)
            answer += num**power
        if answer == number:
            print(f"{number} is a narcisstic number!")
        else:
            print(f"{number} is not a narcisstic number.\nThis is the answer: {answer}.")
        
        program_running = input("Would you like to try another number? ").lower()
        
        if program_running == "yes":
            running = True
        else:
            print("Understood! Thank you for trying this program!")
            running = False