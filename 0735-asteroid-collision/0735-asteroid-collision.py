class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        # st.append(asteroids[0])
        i = 0
        n = len(asteroids)
        while i < n: 
            st.append(asteroids[i])
            # print(st)
            i += 1
            while len(st) > 1:
                if st[-1] < 0 and st[-2] > 0:
                    v = st.pop()
                    a_v = st.pop()
                    if abs(v) == abs(a_v):
                        change = 0
                    if abs(v) > abs(a_v):
                        change = 0
                        st.append(v)
                    if abs(v) < abs(a_v):
                        st.append(a_v)
                else:
                    break
        return st
        