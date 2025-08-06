class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids: 
            st.append(i)
            # print(st)
            while len(st) > 1:
               
                if st[-1] < 0 and st[-2] > 0:

                    if abs(st[-1]) == abs(st[-2]):
                        st = st[:-2]
                        continue
                    if abs(st[-1]) > abs(st[-2]):
                        st.pop(-2)
                    else:
                        st.pop(-1)
                else:
                    break
        return st
        