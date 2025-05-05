class DateCalculator:
    def __init__(self, year, month, day):
        
        self.original_year = year
        self.original_month = month
        self.day = day

        
        if month == 1 or month == 2:
            self.month = month + 12  
            self.year = year - 1  
        else:
            self.month = month
            self.year = year

    def calculate_day_of_week(self):
        
        K = self.year % 100         
        J = self.year //100      
        q = self.day
        m = self.month
        h = (q + (13 * (m + 1)) 

        
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]


date = DateCalculator(1589, 9, 15)  
print("The day was:", date.calculate_day_of_week())
