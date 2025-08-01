class Solution:
    MOD = 10**9 + 7
    def countGoodNumbers(self, n: int) -> int:

        def mod_pow(base, exp, mod):
            result = 1
            base %= mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        evens = (n + 1) // 2
        odds = n // 2
        return (mod_pow(5, evens, self.MOD) * mod_pow(4, odds, self.MOD)) % self.MOD
        