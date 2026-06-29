import requests
import geocoder

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}"
    )

    response = requests.get(url)
    return response.json()

def get_current_location():
    g = geocoder.ip("me")
    return g.city

def display_weather(weather_data):
    if weather_data.get("cod") != 200:
        print("\nError:", weather_data.get("message"))
        return

    temp = weather_data["main"]["temp"] - 273.15

    print("\n========== WEATHER REPORT ==========")
    print("City        :", weather_data["name"])
    print("Country     :", weather_data["sys"]["country"])
    print("Temperature :", round(temp, 2), "°C")
    print("Humidity    :", weather_data["main"]["humidity"], "%")
    print("Pressure    :", weather_data["main"]["pressure"], "hPa")
    print("Condition   :", weather_data["weather"][0]["description"].title())
    print("Wind Speed  :", weather_data["wind"]["speed"], "m/s")
    print("====================================")


def send_weather_alert(weather_data):
    if weather_data.get("cod") != 200:
        return

    weather_id = weather_data["weather"][0]["id"]

    print("\nWeather Alert")

    if 200 <= weather_id < 300:
        print("⚡ Thunderstorm Alert!")

    elif 300 <= weather_id < 400:
        print("🌦 Drizzle Alert!")

    elif 500 <= weather_id < 600:
        print("🌧 Rain Alert!")

    elif 600 <= weather_id < 700:
        print("❄ Snow Alert!")

    elif 700 <= weather_id < 800:
        print("🌫 Fog / Mist Alert!")

    elif weather_id == 800:
        print("☀ Clear Sky")

    elif 801 <= weather_id <= 804:
        print("☁ Cloudy Weather")

    else:
        print("No weather alerts.")


def main():
    while True:

        print("\n====== Weather App ======")
        print("1. Get Weather by City")
        print("2. Get Current Location Weather")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather = get_weather(city)
            display_weather(weather)
            send_weather_alert(weather)

        elif choice == "2":
            city = get_current_location()

            if city is None:
                print("Unable to detect your location.")
                continue

            print("\nCurrent City:", city)

            weather = get_weather(city)
            display_weather(weather)
            send_weather_alert(weather)

        elif choice == "3":
            print("Thank you for using Weather App!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
