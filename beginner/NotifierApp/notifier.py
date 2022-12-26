import time
from plyer import notification

while True:
    notification.notify(
       title = 'Hello User!'
       message = 'Wake up and drink a cup of Water'
       timeout = 10
    )
time.sleep(10)