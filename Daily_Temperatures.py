# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days 
# you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# 
# Example 1:
# 
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# 
# Example 2:
# 
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# 
# Example 3:
# 
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
# 
# 
# Approach 1: Monotonic Stack
# 
# A monotonic stack is simply a stack where the elements are always in sorted order. How does this help us? We can use a monotonic decreasing stack to hold temperatures.
# Monotonic decreasing means that the stack will always be sorted in descending order. Because the problem is asking for the number of days,
# instead of storing the temperatures themselves, we should store the indices of the days, and use temperatures[i] to find the temperature of the ith day.
# 
# Monotonic stacks are a good option when a problem involves comparing the size of numeric elements, with their order being relevant.
# 
# On each day, there are two possibilities. If the current day's temperature is not warmer than the temperature on the top of the stack, we can just push the current day onto the stack
# since it is not as warm (equal or smaller), this will maintain the sorted property.
# 
# If the current day's temperature is warmer than the temperature on top of the stack, this is significant. It means that the current day is the first day with a warmer temperature than the day
# associated with the temperature on top of the stack. When we find a warmer temperature, the number of days is the difference between the current index and the index on the top of the stack. 
# We can declare an answer array before iterating through the input and populate answer as we go along.


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=len(temperatures)
        ans = [0] * l
        stack = []
        for index, value in enumerate(temperatures):
            # check weather the current temp is greater than the last appended stack value
            # if it is, then we will pop all the temps in the stack that are lesser than the current temp
            while stack and stack[-1][1] < value:
                prev_index, prev_temp = stack.pop()
                ans[prev_index] = index - prev_index
            # since, we are comparing the temps before appending and popping all the lower ones
            # the stack will be left with only temps that are greater than the current temp
            # hence, the stack will be sorted in a decending order of temps
            stack.append([index, value])
        return ans
