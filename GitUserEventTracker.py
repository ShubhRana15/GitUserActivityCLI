import requests
import sys
import urllib.request
import json

def get_userevents(username):
    url=f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    response_json = response.json()
    print(response_json)



def nativejson(username):
    # Define the API endpoint
    url=f"https://api.github.com/users/{username}/events"

    eventtype = []
    repolist = []
        # Print the JSON data
    try:
        # Make the request
        with urllib.request.urlopen(url) as response:
            # Read the response
            data = response.read()
            # Decode the response
            json_data = json.loads(data.decode('utf-8'))
            for i in json_data:
                eventtype.append(i["type"])
                repolist.append(i["repo"]["url"])
    except Exception as e:
        print(f"The error is {e}\n")
        sys.exit(1)

    print(f"The latest public events for {username} are below\n")
    for i in range(0,len(eventtype)):
        print(f"{i+1} {eventtype[i]} for the repo {repolist[i]}")

def main():
    print(sys.argv[1])
    nativejson(sys.argv[1])



if __name__ == "__main__":
    main()
