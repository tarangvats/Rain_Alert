from twilio.rest import Client
account_sid ="AC9b23734b449aa9d1975f69d4a3fb5f09"
auth_token = "22c6e11b5109d9e82c69a6d2dce8f787"


api_key = "e0e02416cec31758e23040e283e697d8"
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
import requests
weather = {
    "lat" : 25.317644,
    "lon" : 82.973915,
    "appid" : api_key,
    "exclude":"current,minutely,daily"
}
response = requests.get(OWN_Endpoint,params=weather)
response.raise_for_status()

weather_data = response.json()
hourly_data = weather_data['hourly']
# print(weather_data)
# print(hourly_data)

will_rain =False
for h in range(12):
    condition = (hourly_data[h]['weather'][0]['id'])
    if condition<800:
        will_rain =True
        # print("it will rain today\n Bring umbrella")

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Tarang You Are Brilliant, Baaris Hogi, Umbrella Lelo",
        from_='+14243560646',
        to='+919928445102'
    )
    print(message.status)
