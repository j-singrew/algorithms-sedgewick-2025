from collections import deque
sum = "( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )"





def Two_Stack_Alg(expr):
    operand = deque()
    number = deque()
    tokens = sum.split()
    for token in tokens:
        if token == '(':
            continue
        if token in ['+','*','-','/']:
            operand.append(token)
        elif token == ')':
            op = operand.pop()
            val1 = number.pop()
            val2 =number.pop()
            if op == '+':
                 number.append(val1+val2)
            if op == '*':
                number.append(val1*val2)
            if op == '-':
                number.append(val1-val2)
            if op == '/':
                number.append(val1/val2)
        else:
            number.append(float(token))
    return number.pop()





sum = "( 1 + ( ( 2 + 3 ) * ( 4 * 90 ) ) )"
result = Two_Stack_Alg(sum)
print(result)



        


