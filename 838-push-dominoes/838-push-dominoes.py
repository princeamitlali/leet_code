class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
            dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
            dominoes = dominoes.replace('.L', 'LL')         # <-- 2)
            # print(dominoes)
        return  dominoes.replace('xxx', 'R.L')
        # n=len(dominoes)
        # dominoes=list(dominoes)
        # flag=0
        # for i in range(n-1,-1,-1):
        #     if dominoes[i]=="L":
        #         ct=1
        #         flag=1
        #     elif dominoes[i]=="." and flag==1:
        #         dominoes[i]=ct
        #         ct+=1
        #     elif dominoes[i]=="R":
        #         flag=0
        #     else:
        #         dominoes[i]=0
        # flagr=0
        # print(dominoes)
        # for i in range(n):
        #     if dominoes[i]=="R":
        #         ctr=1
        #         flagr=1
        #     elif str(dominoes[i]).isdigit() and flagr==1 and abs(ctr)<abs(dominoes[i]) or dominoes[i]==".":
        #         dominoes[i]="R"
        #         ctr+=1
        #     elif str(dominoes[i]).isdigit() and flagr==1 and abs(ctr)==abs(dominoes[i]):
        #         dominoes[i]="."
        #     elif flagr==1 and dominoes[i]==0:
        #         dominoes[i]="R"
        #     elif dominoes[i]=="L":
        #         flagr=0
        #     elif dominoes[i]==0:
        #         dominoes[i]="."
        #     else:
        #         dominoes[i]="L"
        # print(dominoes)
        # return "".join(dominoes)
                