class Solution:
    def maxArea(self, h: List[int]) -> int:
        left = 0
        right = len(h)-1
        leftCol = h[left]
        rightCol = h[right]
        
        ans = 0
        if leftCol < rightCol:
            ans = leftCol * (right - left)
        else:
            ans = rightCol * (right - left)

        while left < right:
            if h[left] < h[right]:
                while left < right and h[left] <= leftCol:
                    left+=1
            else:
                while left < right and h[right] <= rightCol:
                    right-=1
            
            leftCol = h[left]
            rightCol = h[right]
            # print(leftCol, rightCol)
            newVol = 0       
            if leftCol < rightCol:
                newVol = leftCol * (right - left)
            else:
                newVol = rightCol * (right - left)

            if newVol > ans:
                ans = newVol
            

        
        return ans
            
