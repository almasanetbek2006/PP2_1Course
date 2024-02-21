import json

from datetime import datetime, timedelta

today=datetime.now()
tomorow=today-timedelta(1)
yesterday=today+timedelta(1)

x=({
    "today": today.strftime("%Y-%m-%d"),
    "tomorow": tomorow.strftime("%Y-%m-%d"),
    "yesterday": yesterday.strftime("%Y-%m-%d")
}
)

print(json.dumps(x, indent= 4))