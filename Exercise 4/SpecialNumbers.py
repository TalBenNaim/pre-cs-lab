def main():
    limit = int(input("etner the limit to check"))

    for num in range(1, limit + 1):
        if (check_special(num) == True):
            print(f"{num} is special!")

def check_special(num):
    digits = get_digits_list(num)
    sum = 0

    for digit in digits:
        sum += int(digit) ** 3
    if sum == num:
        return True
    
def get_digits_list(num):
    digits = []

    for digit in str(num):
        digits.append(digit)
    return digits

if __name__ == "__main__":
    main()