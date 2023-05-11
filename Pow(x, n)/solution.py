class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(x,y):
            if(y == 0):
                return 1
            temp = solve(x, int(y / 2))
        
            if (y % 2 == 0):
                return temp * temp
            else:
                if(y > 0):
                    return x * temp * temp
                else:
                    return (temp * temp) / x
        return solve(x,n)