if __name__ == '__main__':
    expression = list(input().strip())
    ans = str()
    tmp = str()
    is_exist = False
    is_first = True
    op = ['+', '-']

    for elem in expression:
        if elem not in op:
            tmp += elem
        elif elem == '-':
            if not is_exist:
                ans += str(int(tmp))
                ans += elem + '('
                is_exist = True
                tmp = ""
            else:
                ans += str(int(tmp))
                ans += ')' + elem + '('
                tmp = ""
        else:
            ans += str(int(tmp))
            ans += elem
            tmp = ""

    ans += str(int(tmp))

    if is_exist:
        ans += ')'

    print(eval(ans))