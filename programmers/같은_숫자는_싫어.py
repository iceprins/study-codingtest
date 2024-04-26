def solution(arr):
    st = [arr[0]]

    for elem in arr:
        if elem != st[-1]:
            st.append(elem)

    return st
