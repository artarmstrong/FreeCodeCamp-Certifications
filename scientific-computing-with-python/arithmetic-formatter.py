def maximum(x, y):
    list = [x, y]
    return max(list)


def arithmetic_arranger(problems, show_answers=False):
    output = ''

    # Check for limit of problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        first = []
        second = []
        third = []
        fourth = []
        for problem in problems:

            problem_list = problem.split()
            answer = 0

            # Check len of number <= 4
            if len(problem_list[0]) > 4 or len(problem_list[2]) > 4:
                return 'Error: Numbers cannot be more than four digits.'

            # Check for only numbers
            if not problem_list[0].isnumeric() or not problem_list[2].isnumeric():
                return 'Error: Numbers must only contain digits.'

            # Check for only addition or subtraition
            if problem_list[1] == '+':
                answer = int(problem_list[0]) + int(problem_list[2])
            elif problem_list[1] == '-':
                answer = int(problem_list[0]) - int(problem_list[2])
            else:
                return "Error: Operator must be '+' or '-'."

            # Fix spacing
            longest = max(len(problem_list[0]), len(problem_list[2])) + 2
            temp_str = ''
            diff = 0
            

            # Fix spacing on first
            if len(problem_list[0]) < longest:
                diff = longest - len(problem_list[0])
                for i in range(diff):
                    temp_str += ' '
                problem_list[0] = temp_str + problem_list[0]
            
            # Fix spacing on second
            if len(problem_list[2]) + 2 < longest:
                diff = longest - (len(problem_list[2]) + 2)
                temp_str = ''
                for i in range(diff):
                    temp_str += ' '
                problem_list[2] = temp_str + problem_list[2]

            # Fix spacing on answer
            if len(str(answer)) < longest:
                diff = longest - len(str(answer))
                temp_str = ''
                for i in range(diff):
                    temp_str += ' '
                answer = temp_str + str(answer)

            # Fix spacing on separator
            separator = ''
            for j in range(longest):
                separator += '-'
            
            first.append(problem_list[0])
            second.append(problem_list[1] + ' ' + problem_list[2])
            third.append(separator)
            fourth.append(str(answer))

        # Print output
        first_line = ''
        second_line = ''
        third_line = ''
        fourth_line = ''
        for k in range(len(first)):
            if k != 0:
                first_line += '    '
                second_line += '    '
                third_line += '    '
                fourth_line += '    '
            first_line += first[k]
            second_line += second[k]
            third_line += third[k]
            fourth_line += fourth[k]
            if k == len(first) - 1:
                first_line += '\n'
                second_line += '\n'

        output = first_line + second_line + third_line
        if show_answers:
            output += '\n' + fourth_line

        #print(output)
        #print(repr(output))
        return output

#arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
