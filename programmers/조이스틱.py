def solution(name):
    ans = 0
    
    move_cnt = len(name) - 1
    
    for i, alphabet in enumerate(name):
        ans += min(ord(alphabet) - ord('A'), ord('Z') - ord(alphabet) + 1)
                
        following = i + 1
        while following < len(name) and name[following] == 'A':
            following += 1
        
        move_cnt = min([move_cnt, 2 *i + len(name) - following, i + 2 * (len(name) -following)])
    
    ans += move_cnt
    
    return ans
