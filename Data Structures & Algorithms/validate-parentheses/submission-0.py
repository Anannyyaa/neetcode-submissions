class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        match = {')' : '(', '}' : '{', ']' : '['}
        
        for char in s:
            if char in match:
                top = stack[-1] if stack else None

                if top == match[char] :
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack)== 0
        