from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    
    children = sorted(g)
    cookies = sorted(s)
    
    j = 0
    for i in range(len(cookies)):
        if (j < len(children)) and (cookies[i] >= children[j]):
            j += 1
    
    return j


if __name__ == '__main__':
    
    print(findContentChildren([1, 2, 3], [1, 1]))  # 1
    print(findContentChildren([1, 2], [1, 2, 3]))  # 2