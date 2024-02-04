def main():
    for index in range(1,101):
        divisible_by_three = index % 3 == 0
        divible_by_five = index % 5 == 0
        if divisible_by_three and divible_by_five:
            print("Fizz_Buzz")
        elif divisible_by_three:
            print("Fizz")
        elif divible_by_five:
            print("Buzz")
        else:
            print(index)

main()
