import json

### This class is what my avrage payckeck for 2025 was.
### This is used to see if im making more than last year
class income:
    def __init__(self, hourlyRate, hoursBiWeek, tipsBiWeek, retirementBiWeek, taxTotalBiWeek):
        self.hourlyRate = hourlyRate
        self.hoursBiWeek = hoursBiWeek
        self.tipsBiWeek = tipsBiWeek
        self.retirementBiWeek = retirementBiWeek
        self.taxTotalBiWeek = taxTotalBiWeek

    def upDateHourly(self, update):
        self.hourlyRate = update
        return(self.hourlyRate)
    
class IncomeDB:
    def __init__(self, path = "Income_calc.json"):
        self.DB = path
        self.data = self.loadDB()
        if "config" not in self.data:
            self.data["config"] = {
                "current_year": 2026,
                "current_job": "Defualtjob",
                "current_rate_base": 20,
                "cuurent_overtime_rate": 30, 
            }

    def getCurrentYear(self):
        return self.data["config"]["current_year"]
    
    def setCurrentYear(self, year):
        self.data["config"]["current_year"] = year
        self.saveDB()

    def getCurrentJob(self):
        return self.data["config"]["current_job"]
    
    def setCurrentJob(self, job):
        self.data["config"]["current_job"] = job
        self.saveDB()

    

    def loadDB(self):
        try:
            with open(self.DB, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def saveDB(self):
        with open(self.DB, "w") as f:
            json.dump(self.data, f, indent=4)

    def ensureYear(self, year, jobName):
        if year not in self.data:
            self.data[year] = {}
        if jobName not in self.data[year]:
            self.data[year][jobName]={
                "totals": {
                    "hours_worked": 0,
                    "gross_pay": 0,
                    "taxes_paid": 0,
                    "retirement_cont": 0,
                    "take_home": 0,
                },
                "pay_rates":[],
            }

    def updatePayRate(self):
        self.data["games_played"] += 1
        self.data["games_won"] += 1
        self.saveDB()
    def updateYear(self):
        self.data["games_played"] += 1
        self.data["games_lost"] += 1
        self.saveDB()


if __name__ == "__main__":
    # payRate = income()
    while True:
        startMenu = input(
        "What would you like to do?\n" 
        "Enter a new pay check (1).\n" 
        "Change hourly pay (2).\n"
        "Change year (3).\n"
        "Change job(4).\n"
        "Quit (5).\n"
        )
        
        payPeriodStart = input("When did the pay Period Start: ")
        payPeriodEnd = input("When did the pay Period End: ")
        hoursWorked = input("How many hours did you work:")
