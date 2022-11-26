import datetime as dt

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = dt.datetime(year,month,day).strftime("%A")
        
        return d