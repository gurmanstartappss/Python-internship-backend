class EmailNotification:
    def send(self):
        print("Email notification sent")

class SMSNotification:
    def send(self):
        print("SMS notification sent")

class PushNotification:
    def send(self):
        print("Push notification sent")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()