if __name__ == '__main__':
    parenthesis = input()
    st = []
    ans = 0
    tmp = 1

    for i in range(len(parenthesis)):
        if parenthesis[i] == "(":
            st.append(parenthesis[i])
            tmp *= 2
        elif parenthesis[i] == "[":
            st.append(parenthesis[i])
            tmp *= 3
        elif parenthesis[i] == ")":
            if not st or st[-1] == "[":
                ans = 0
                break
            if parenthesis[i - 1] == "(":
                ans += tmp
            st.pop()
            tmp //= 2
        else:
            if not st or st[-1] == "(":
                ans = 0
                break
            if parenthesis[i - 1] == "[":
                ans += tmp
            st.pop()
            tmp //= 3

    if st:
        print(0)
    else:
        print(ans)
