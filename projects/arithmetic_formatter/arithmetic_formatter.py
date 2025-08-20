def arithmetic_arranger(problems, show_answers=False):

    values = [problem.split(' ') for problem in problems]

    if len(values) > 5:
        return "Error: Too many problems."
    
    elif [operator for operator in [value[1] for value in values] if operator not in ['+', '-']]:
        return "Error: Operator must be '+' or '-'."

    elif [operand for value in values for operand in (value[0], value[2]) if not operand.isdigit()]:
        return "Error: Numbers must only contain digits."

    
    elif [operand for operand in [value[0:3:2] for value in values] if (len(operand[0]) > 4 or len(operand[1]) > 4)]:
        return "Error: Numbers cannot be more than four digits."
    else:
        first_operand = []
        operator = []
        second_operand = []
        for value in values:
            first_operand.append(value[0])
            operator.append(value[1])
            second_operand.append(value[2])

        top_row = []
        second_row = []
        line = []
        solution = []
        for n in range(len(values)):
            width = max(len(first_operand[n]), len(second_operand[n])) + 2
            top_row.append(first_operand[n].rjust(width))
            second_row.append(operator[n] + second_operand[n].rjust(width-1))
            line.append("-" * width)
            solution.append(f"{eval(first_operand[n]+operator[n]+second_operand[n])}".rjust(width))
        
        one = '    '.join(top_row)
        two = '    '.join(second_row)
        th = '    '.join(line)
        f = '    '.join(solution)

        if show_answers:
            final = one+"\n" + two+"\n" + th+"\n" + f
            return final
        else:
            final = one+"\n" + two+"\n" + th
            return final
       
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
