class Solution:
    # def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # count = 0
        # seng = sum(energy)
        # if initialEnergy < seng + 1:
        #     count += (seng - initialEnergy) + 1
        # print(count)
        # for i in experience:
        #     if initialExperience  <i + 1:
        #         count += i - initialExperience + 1
        #         initialExperience = i + 1
        #     else:
        #         initialExperience += i
        #     print(count,initialExperience)
        # return count 
    def minNumberOfHours(self, energy: int, experience: int, energies: List[int], experiences: List[int]) -> int:
        hours = 0

        for eng, exp in zip(energies, experiences):
            # Adding the missing amount of energy
            extra_en = max(0, eng - energy + 1)
            energy += extra_en

            # Adding the missing amount of experience
            extra_ex = max(0, exp - experience + 1)
            experience += extra_ex

            energy -= eng
            experience += exp
            hours += extra_en + extra_ex

        return hours
        