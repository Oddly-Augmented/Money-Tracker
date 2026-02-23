import json

### Paycheck calculator for estimating tips and comparing pay cycles
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
# ----- JSON load/save -----       
    def loadDB(self):
        try:
            with open(self.DB, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def saveDB(self):
        with open(self.DB, "w") as f:
            json.dump(self.data, f, indent=4)

# ----- Ensure year + job -----
### TODO use something to get the curent year not from user input 
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

# ----- Config: current year/job/rates -----
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

    def getCurrentBaseRate(self):
        return self.data["config"]["current_rate"]
    
    def setCurrentBaseRate(self, rate):
        self.data["config"]["current_rate"] = rate
        self.data["config"]["cuurent_overtime_rate"] = rate * 1.5
        self.saveDB()

    def getCurrentOvertimeRate(self):
        return self.data["config"]["cuurent_overtime_rate"] 
    
 # ----- Update totals and pay_rates -----
    def updateTotals(self, year, jobName, hours, gross, taxes, retirement, takeHome):
        year = str(year)
        self.ensureYear(year, jobName)
        t = self.data[year][jobName]["totals"]
        t["hours_worked"]  += hours
        t["gross_pay"] += gross
        t["taxes_paid"] += taxes
        t["retirement_cont"] += retirement
        t["take_home"] += takeHome
        self.saveDB()

if __name__ == "__main__":
    # payRate = income()
    db = IncomeDB()


    while True:
        startMenu = input(
        "What would you like to do?\n" 
        "Enter a new pay check (1).\n" 
        "Change hourly pay (2).\n"
        "Change year (3).\n"
        "Change job(4).\n"
        "Quit (5).\n"
        )

        if startMenu == "1":
            db.updateTotals(
                year=db.getCurrentYear(),
                jobName=db.getCurrentJob(),
                hours=float(input("How many hours did you work?: ")),
                gross=float(input("What was your gross pay?: ")),
                taxes=float(input("What are the taxes?: ")),
                retirement=float(input("What is the retremnet?: ")),
                takeHome=float(input("What is your take home?: "))
            )
            break
        break
            
        
    
