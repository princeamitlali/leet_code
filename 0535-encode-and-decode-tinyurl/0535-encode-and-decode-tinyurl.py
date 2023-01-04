class Codec:
    dic = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        val = longUrl.split("/")
        # print(val)
        res =""
        for i in val:
            if i != "":
                res += i[0] + str(len(i))
        count = 0
        while True:
            if res not in self.dic.keys():
                self.dic[res] = longUrl
                break
            count +=1
            res += "_" + str(count)
        return "http://tinyurl.com/" + res
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        val = shortUrl.split("/")
        return self.dic[val[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))