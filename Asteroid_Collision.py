# We are given an array asteroids of integers representing asteroids in a row.
# 
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, 
# negative meaning left). Each asteroid moves at the same speed.
# 
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
# 
#  
# 
# Example 1:
# 
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# 
# Example 2:
# 
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# 
# Example 3:
# 
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# 
# Example 4:
# 
# Input: asteroids = [-2,-1,1,2]
# Output: [-2,-1,1,2]
# Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.
# 
# Approach 1: Stack
# 
# A row of asteroids is stable if no further collisions will occur. After adding a new asteroid to the right, some more 
# collisions may happen before it becomes stable again, and all of those collisions (if they happen) must occur right to left. 
# This is the perfect situation for using a stack.
# 
# Say we have our answer as a stack with rightmost asteroid top, and a new asteroid comes in. If new is moving right (new > 0),
# or if top is moving left (top < 0), no collision occurs.
# 
# Otherwise, if abs(new) < abs(top), then the new asteroid will blow up; if abs(new) == abs(top) then both asteroids will blow up; 
# and if abs(new) > abs(top), then the top asteroid will blow up (and possibly more asteroids will, so we should continue checking.)
# 

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for ast in asteroids:
            while ans and ast<0<ans[-1]: # new is -ve i.e. moving left and top_of_stack is +ve i.e. moving right
                if -ast>ans[-1]: # compare size
                    ans.pop()
                    continue # continue with the while loop w/o going further
                elif -ast==ans[-1]:
                    ans.pop()
                break # cause both ast and ans[-1] ll be destroyed
            else:
                ans.append(ast) # if they are not heading for each other
        return ans
