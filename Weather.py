import requests

city = input("Enter the name of the city: ")
print("Displaying weather report for" + city)

url = f"https://wttr.in/{city}"
res = requests.get(url)

print(res.text)