class Solution:
    def intToRoman(self, num: int) -> str:
        
        arr = [0,0,0,0,0,0,0]
        arr[0] = num//1000
        num = num % 1000
        arr[1] = num//500
        num = num % 500
        arr[2] = num//100
        num = num % 100
        arr[3] = num//50
        num = num % 50
        arr[4] = num//10
        num = num % 10
        arr[5] = num//5
        num = num % 5
        arr[6] = num
        
        st = ""
        if arr[6]<4:
            st += "I" * arr[6]
        elif arr[5] == 0:
            st+= "VI"
        else:
            st += "XI"
       
        if arr[5] == 1 and arr[6] != 4:
            st += 'V'
            
        if arr[4]<4:
            st += "X" * arr[4]
        elif arr[3] == 0:
            st+= "LX"
        else:
            st += "CX"
            
        if arr[3] == 1 and arr[4] != 4:
            st += 'L'
        
        if arr[2]<4:
            st += "C" * arr[2]
        elif arr[1] == 0:
            st+= "DC"
        else:
            st += "MC"
            
        if arr[1] == 1 and arr[2] != 4:
            st += 'D'
        
        if arr[0]<4:
            st += "M" * arr[0]
        
        return st[::-1]
    
            
        