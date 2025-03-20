# Leetcode 20: valid parentheses
def isValid(s: str) -> bool:
        stack = []
        bracket_map={')':'(','}':'{',']':'['}
        for ch in s:
            if ch in '{[(':
                stack.append(ch)
            else:
                if not stack or stack[-1]!= bracket_map[ch]:
                    # focus on use of or in condition check
                    return False
                stack.pop()
        return not stack

print(isValid("()[]{}"))
print(isValid("()[]{}}"))