class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 1:
            return ["1"]
        if n == 2:
            return ["1","2"]
        res = ["1","2"]
        for i in range(3,n+1):
            if i %15 == 0:
                res.append("FizzBuzz" )
            elif i % 5 == 0:
                res.append("Buzz" )
            elif i % 3 == 0:
                res.append("Fizz" )
            else:
                res.append(str(i))
        return res
                
                
        