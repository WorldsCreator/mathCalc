def mathCalc(expr):
    if '(' in expr and ')' in expr:
        beg, open_bracket, end = expr.partition('(')
        end = end[::-1]
        end, close_bracket, middle = map(lambda x: x[::-1], end.partition(')'))
        middle = str(mathCalc(middle))
        res = mathCalc(beg + middle + end)
        if '.' in str(res):
            return round(res, 3)
        else:
            return res
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
            if '.' in str(expr):
                return round(float(expr), 3)
            else:
                return int(expr)


a = "".join(x for x in input() if not x == ' ')
print(mathCalc(a))
