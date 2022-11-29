from email import message
from operator import iconcat
from socket import timeout
from plyer import notification
import time

if __name__ == '__main__':

    while True:

        notification.notify (

            title = "Please Drink Water now..",
            message = "Drinking water is good for health.",
            timeout = 10
        )

        time.sleep(60*60)