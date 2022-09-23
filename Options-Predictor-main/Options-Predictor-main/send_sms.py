from twilio.rest import Client


recipients = ["7156600424", "7158291700"]
messages = {"Panic": "A fatal error has occurred. Check immediately", "Test": "This is a test"}

account_sid = "ACdac9f9464b96401b9b8af1fec83b003f"
auth_token = "e4d096d1734b277fa51572c20ec5a160"

client = Client(account_sid, auth_token)


def send(message):
    print("Sending: ", message)
    for i in recipients:
        client.messages.create(
        to=i,
        from_="+19103381134",
        body=message
        )

def Select_Message():
    Message_Selection = input("1: Panic \n2: Test \n")
    if Message_Selection == "1":
        send(messages['Panic'])
    if Message_Selection == "2":
        send(messages['Test'])
