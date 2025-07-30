# spam detection application


spam_words=["buy","sell","offer","money","sale","off","money making","otp","urgent","bank","atm"]


userInput = input("Enter the Message: ")


userInput.lower()

for i in spam_words:
    if i in userInput:
        print("Its a Spam")
        break
else:
        print("Its Real!!!")