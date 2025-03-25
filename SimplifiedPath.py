# Leetcode :71 Simplified Path
def simplifyPath(path: str) -> str:
    pathList = path.split('/')
    stack = []
    for dir in pathList:
        if  dir == "..":
            if stack:
                stack.pop()
        elif dir and dir!='.':
            stack.append(dir)
    ans = '/' + '/'.join(stack)
    return ans

print(simplifyPath("/home/user/Documents/../Pictures"))