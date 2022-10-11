import requests
import json

def return_skipped_value():
    #response = requests.get('link')
    response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

    skipped = 0

    for data in response.json()['items']:
        if data['answer_count'] == 4:
            print(data['title'])
            print(data['link'])
            print()
            skipped = skipped + 1
        else:
            print("skipped")
        print()
        print("{:.d}".format(skipped))
        

    return skipped