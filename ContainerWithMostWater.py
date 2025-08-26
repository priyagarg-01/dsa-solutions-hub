class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxwater=0
        while i<j:
            x=min(height[i], height[j])
            y=j-i
            maxwater=max(maxwater, x*y)
            
            if x==height[i]:
                i+=1
            else:
                j-=1
        
        return maxwater
