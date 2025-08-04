class Solution:
    def is_prime(self,n):
        for i in range(2,int(sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        if n <2:
            return 0
        sol = [1] * n
        sol[0] = 0
        sol[1] = 0
        for i in range(2,int(sqrt(n))+1):
            if sol[i] == True:
                if self.is_prime(i):
                    for j in range(i+i,n,i):
                        sol[j] = 0
        return sum(sol)
        