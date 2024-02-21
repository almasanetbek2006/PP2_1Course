import json
from datetime import datetime
current_date = datetime.now()

x = ({
    "datetime with microseconds": current_date.strftime("%Y-%m-%d %H-%M:%S-%f")
})

print(json.dumps(x, indent = 5))