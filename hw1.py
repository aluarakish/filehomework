def calculate_expression(expression):
    def get_priority(operator):
        if operator in ('+', '-'):
            return 1
        if operator in ('*', '/'):
            return 2
        return 0
    
    def do_math(num1, num2, operator):
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/':
            return num1 / num2

    def solve(parts):
        numbers = []
        ops = []
        i = 0
        
        while i < len(parts):
            if parts[i] == ' ':
                i += 1
                continue
            elif parts[i] == '(':
                ops.append(parts[i])
            elif parts[i].isdigit():
                current_num = 0
                while i < len(parts) and parts[i].isdigit():
                    current_num = current_num * 10 + int(parts[i])
                    i += 1
                numbers.append(current_num)
                i -= 1
            elif parts[i] == ')':
                while ops and ops[-1] != '(':
                    second = numbers.pop()
                    first = numbers.pop()
                    operator = ops.pop()
                    numbers.append(do_math(first, second, operator))
                ops.pop()
            else:
                while ops and get_priority(ops[-1]) >= get_priority(parts[i]):
                    second = numbers.pop()
                    first = numbers.pop()
                    operator = ops.pop()
                    numbers.append(do_math(first, second, operator))
                ops.append(parts[i])
            i += 1
        
        while ops:
            second = numbers.pop()
            first = numbers.pop()
            operator = ops.pop()
            numbers.append(do_math(first, second, operator))
        
        return numbers[0]
    
    return solve(expression)

expr = "2 + (3 * 4) - 5 / (1 + 1)"
answer = calculate_expression(expr)
print("Ответ:", answer)
