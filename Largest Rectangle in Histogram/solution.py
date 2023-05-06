class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #Nearest smaller to left
        stack=[]
        res=[]
        for i in range(len(heights)):
            if len(stack)==0:
                res.append(-1)
            elif len(stack)!=0 and stack[-1][0]<heights[i]:
                res.append(stack[-1][1])
            elif len(stack)!=0 and stack[-1][0]>=heights[i]:
                while(len(stack)!=0 and stack[-1][0]>=heights[i]):
                    stack.pop()
                if len(stack)==0:
                    res.append(-1)
                else:
                    res.append(stack[-1][1])
            stack.append([heights[i],i])

        #Nearest smaller to right
        stack=[]
        res2=[]
        for i in range(len(heights)-1,-1,-1):
            if len(stack)==0:
                res2.append(len(heights))
            elif len(stack)!=0 and stack[-1][0]<heights[i]:
                res2.append(stack[-1][1])
            elif len(stack)!=0 and stack[-1][0]>=heights[i]:
                while(len(stack)!=0 and stack[-1][0]>=heights[i]):
                    stack.pop()
                if len(stack)==0:
                    res2.append(len(heights))
                else:
                    res2.append(stack[-1][1])
            stack.append([heights[i],i])
        
        res2=res2[::-1]
        res3=[]
        for i in range(len(heights)):
            res3.append((res2[i]-res[i]-1)*heights[i])
        return max(res3)
