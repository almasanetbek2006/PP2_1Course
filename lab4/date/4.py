import json
from datetime import datetime, timedelta

day = str(input("AGO or AFTER: "))
b = day.lower()
a = int(input(f"How many day {day}: "))
current_date = datetime.now()
if b == "ago":
    different_date = current_date - timedelta(a)
   
elif b == "after":
    different_date = current_date + timedelta(a)
    
x = ({
        "current_date": current_date.strftime("%Y-%m-%d %H-%M:%S"),
        f"different between current_date and {a} day {b}": different_date.strftime("%Y-%m-%d %H-%M:%S")
    })
print(json.dumps(x, indent = 4))