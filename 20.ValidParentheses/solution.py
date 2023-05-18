class Solution:
    def isValid(self, s: str) -> bool:
        rules = {
            '(': ')',
            '{': '}',
            '[': ']',
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        stack_len = 0
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                stack_len += 1
            else:
                if stack_len == 0:
                    return False
                target_in_stack = rules[i]
                in_stack = stack.pop()
                if stack_len == 0 or target_in_stack != in_stack:
                    return False
                stack_len -= 1
                
        return stack_len == 0
                
print(Solution().isValid('()'))