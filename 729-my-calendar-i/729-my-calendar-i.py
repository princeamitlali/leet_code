class MyCalendar:
    def __init__(self):
        self.booking_history = []

    def book(self, start: int, end: int) -> bool:
        for start_date,end_date in self.booking_history:
            if start_date < end and start < end_date: 
                return False 
        self.booking_history.append((start,end))
        return True
            
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)