import json
from datetime import datetime, timedelta

current_date= datetime.now()

new_date =current_date-timedelta(5)

x = ({
    "current_date": current_date.strftime("%Y-%m-%d"),  # Казиргі датаны жыл-ай-күн форматында айналдыру
    "new_date": new_date.strftime("%Y-%m-%d")  # Новый датаны жыл-ай-күн форматында айналдыру
})

print(json.dumps(x, indent = 4))