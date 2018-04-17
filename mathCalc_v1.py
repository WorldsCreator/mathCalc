def mathCalc(expr):
    if '(' in expr and ')' in expr:
        beg, open_bracket, end = expr.partition('(')
        end = end[::-1]
        end, close_bracket, middle = map(lambda x: x[::-1], end.partition(')'))
        middle = str(mathCalc(middle))
        return mathCalc(beg + middle + end)
    else:
        if expr.split('+')[0] != expr:
            nums = expr.split('+')
            return mathCalc(nums[0]) + mathCalc(nums[1])
        elif expr.split('-')[0] != expr:
            nums = expr.split('-')
            return mathCalc(nums[0]) - mathCalc(nums[1])
        elif expr.split('*')[0] != expr:
            nums = expr.split('*')
            return mathCalc(nums[0]) * mathCalc(nums[1])
        elif expr.split('/')[0] != expr:
            nums = expr.split('/')
            return mathCalc(nums[0]) // mathCalc(nums[1])
        else:
            return int(expr)


a = "".join(x for x in input() if not x == ' ')
print(mathCalc(a))
