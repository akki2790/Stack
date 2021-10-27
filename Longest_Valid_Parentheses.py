# 32. Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# 
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Input: s = ""
# Output: 0

# Using Stack:
# For every "(" encountered, we push its index into the stack
# For every ")" encountered, we pop the stack. If the stack is not empty, we subtract the new top-of-stack from the current closing index. This is the length of the currently encountered valid parantheses.
# If the stack is empty after the pop, we push the current closing index onto the stack. This way we keep on calculating the lenghts of the valid substrings.
# The stack is initiated with a value of -1; incase our sting starts with a opening bracket

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack != []:
                    valid_p_len = i - stack[-1]
                    res = max(res, valid_p_len)
                else:
                    stack.append(i)
        return res 
