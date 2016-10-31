from twilio.rest import TwilioRestClient
import requests

account_sid = " <Your sid> "
auth_token = " <Your auth_token> "
client = TwilioRestClient(account_sid, auth_token)
ourNumber = " <Your number> "
requestParams = {
    "method": "getQuote",
    "key": "457653",
    "format": "json",
    "lang": "en"    
    }
url = "http://api.forismatic.com/api/1.0/"
arrayOfPeople = []

print("Hello. Welcome to the daily inspirational quote machine!")
print("Who do you want to send this to?\nType 'done' when finished.")

answer = ""

while(answer != "done" and answer != "Done"): # While they dont answer done, add the phone number to the list
    answer = input(">")
    if(answer == "done" or answer == "Done"):
        break
    
    arrayOfPeople.append(answer)


requestToApi = requests.post(url, params=requestParams) # Requests the qoute from the API
json = requestToApi.json() # This grabs the data from the response from API
finishedQuote = json['quoteText'] + " -" + json['quoteAuthor'] # The finished quote!

for person in arrayOfPeople: # For every person we want to text, send the quote
    client.messages.create(to=person, from_=ourNumber,
                                     body=finishedQuote)
    


print("You sent quotes to: ")

for person in arrayOfPeople:
    print(person)
