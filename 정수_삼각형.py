
#참고: https://codedrive.tistory.com/49
def solution(triangle):
    for h in range(1, len(triangle)):
        upper_level = triangle[h - 1]        
        for i, v in enumerate(triangle[h]):
            if i == 0:
                triangle[h][i] = v + upper_level[0]
            elif i == len(triangle[h]) - 1:
                triangle[h][i] = v + upper_level[-1]
            else:
                left = i - 1
                right = i

                triangle[h][i] = v + max(upper_level[left], upper_level[right])

    return max(triangle[-1])
