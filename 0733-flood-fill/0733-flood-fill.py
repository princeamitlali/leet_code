class Solution:
    m,n,img,clr = 0,0,[],0
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color :
            return image
        self.dfs(image,sr,sc,color,image[sr][sc])
        return image
    def dfs(self,image,sr,sc,color,current) :
        if sc<0 or sr<0 or sr>=len(image) or sc>=len(image[0]) :
            return
        if current!=image[sr][sc] :
            return 
        image[sr][sc] = color
        self.dfs(image,sr+1,sc,color,current) 
        self.dfs(image,sr-1,sc,color,current) 
        self.dfs(image,sr,sc+1,color,current) 
        self.dfs(image,sr,sc-1,color,current) 
                
        