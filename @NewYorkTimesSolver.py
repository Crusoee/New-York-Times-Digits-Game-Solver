operators = ["+", "-", "*", "/"]

possibilities = []

def create_list(temp_list):

    numbers = []

    for i in range(len(temp_list)):
        numbers.append(int(temp_list[i]))

    return numbers

def solve_problem(number_goal, numbers):

    def _solve(numbers, step):

        for index1 in range(len(numbers)):
            for index2 in range(len(numbers)):
                if index1 != index2:
                    for operator in operators:
                        num1 = numbers[index1]
                        num2 = numbers[index2]

                        num = solve_equation(num1, num2, operator)

                        if num == None:
                            break

                        if num == number_goal:
                            possibilities.append(step + f"({num1} {operator} {num2} = {num}) Answer -> {num}")

                        temp_numbers = []
                        temp_numbers = numbers.copy()
                        temp_numbers.remove(num1)
                        temp_numbers.remove(num2)
                        temp_numbers.append(num)

                        _solve(temp_numbers, (step + f"({num1} {operator} {num2} = {num})"))
                
    _solve(numbers, "")

    print(f"There are {len(possibilities)} possible solutions\n")

    print(f"The shortest solution: {min(possibilities, key=len)}") # prints "i"
    print(f"The longest solution: {max(possibilities, key=len)}") # prints "i"

def solve_equation(num1, num2, operator):

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
        if answer < 0:
            answer = None
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        if num2 != 0:
            answer = num1 / num2
            if not(isinstance(answer, int)):
                answer = None
        else:
            answer = None
    else:
        answer = None

    return answer

def main():

    number_goal = int(input("what is the number you need to add to... "))
    parts = input("type in all 6 of the number options, separated by commas, no spaces... ")
    temp_list = parts.split(",")

    numbers = create_list(temp_list)

    solve_problem(number_goal, numbers)

if __name__ == "__main__":
    main()