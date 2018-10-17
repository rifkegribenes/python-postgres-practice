import requests

number = input("Enter a number: ")
try:
    print(int(number) * 2)
except LookupError:
    print("Lookup error? This should never happen...")
except ValueError:
    print("You did not enter a base 10 number! Try again.")


r = requests.post('http://text-processing.com/api/sentiment', data={'text': 'hello world'})
try:
    label = r.json()['label']
    print(label)
except ValueError:
    print("We could not decode the JSON response")
