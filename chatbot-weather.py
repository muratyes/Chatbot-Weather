import requests

# OpenWeatherMap API Anahtarınızı buraya yazın
API_KEY = '3a8b4aa7382b21e4e16f5f89acbfa3af'

def get_weather(city, units='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={API_KEY}&q={city}&units={units}&lang=en"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == 200:
            main = data["main"]
            weather = data.get("weather")
            wind = data.get("wind")
            pressure = main.get("pressure")
            humidity = main.get("humidity")

            if weather and len(weather) > 0:
                weather_description = weather[0].get("description", "No description available")
            else:
                weather_description = "Weather information not available"
            temperature = main.get("temp", "Temperature information not available")
            wind_speed = wind.get("speed", "Wind speed not available") if wind else "Wind information not available"
            wind_deg = wind.get("deg", "Wind direction not available") if wind else "" # Rüzgar yönü derece cinsinden
            pressure_hpa = f"{pressure} hPa" if pressure is not None else "Pressure not available"
            humidity_percent = f"%{humidity}" if humidity is not None else "Humidity not available"

            weather_report = (f"Weather in {city}: {weather_description}.\n"
                            f"Temperature: {temperature}°{get_unit_symbol(units)}\n"
                            f"Wind Speed: {wind_speed} m/s\n"
                            f"Humidity: {humidity_percent}\n"
                            f"Pressure: {pressure_hpa}")
            if wind and wind_deg is not None:
                weather_report += f"\nWind Direction: {get_wind_direction(wind_deg)}"
        elif data["cod"] == "404":
            weather_report = f"City '{city}' not found. Please enter a valid city name."
        else:
            weather_report = f"Could not retrieve weather information. Error code: {data.get('cod', 'Unknown')}, Message: {data.get('message', 'No message')}"

    except requests.exceptions.RequestException as e:
        weather_report = f"An error occurred during the request: {e}"
    except (KeyError, IndexError) as e:
        weather_report = f"An unexpected data format error occurred: {e}"

    return weather_report

def get_forecast(city, units='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = f"{base_url}appid={API_KEY}&q={city}&units={units}&lang=en"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == "200":
            forecast_list = data.get("list", [])
            if forecast_list:
                forecast_report = f"5-day/3-hour forecast for {city}:\n"
                for item in forecast_list[:5]: # İlk 5 tahmini gösterelim
                    timestamp = item.get("dt_txt", "Date/Time not available")
                    main = item.get("main", {})
                    weather = item.get("weather", [])
                    temp = main.get("temp", "N/A")
                    description = weather[0].get("description", "N/A") if weather else "N/A"
                    forecast_report += f"- {timestamp}: {description}, Temp: {temp}°{get_unit_symbol(units)}\n"
            else:
                forecast_report = f"No forecast data available for {city}."
        elif data["cod"] == "404":
            forecast_report = f"City '{city}' not found."
        else:
            forecast_report = f"Could not retrieve forecast information. Error code: {data.get('cod', 'Unknown')}, Message: {data.get('message', 'No message')}"

    except requests.exceptions.RequestException as e:
        forecast_report = f"An error occurred during the forecast request: {e}"
    except (KeyError, IndexError) as e:
        forecast_report = f"An unexpected data format error occurred during forecast retrieval: {e}"

    return forecast_report

def get_unit_symbol(unit):
    if unit == 'metric':
        return 'C'
    elif unit == 'imperial':
        return 'F'
    elif unit == 'standard':
        return 'K'
    return ''

def get_wind_direction(degrees):
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = round(degrees / 22.5) % 16
    return directions[index]

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
def show_menu():
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'*' * 30}{Colors.RESET}")
    print(f"{Colors.BOLD}  What would you like to do?{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'*' * 30}{Colors.RESET}")
    print(f"Type {Colors.GREEN}'weather'{Colors.RESET} for current weather.")
    print(f"Type {Colors.GREEN}'forecast'{Colors.RESET} for 5-day forecast.")
    print(f"Type {Colors.GREEN}'units'{Colors.RESET} to set temperature units.")
    print(f"Type {Colors.RED}'OUT'{Colors.RESET} to exit.")

def chatbot():
    print(f"Hello! {Colors.BLUE}'I'm an advanced chatbot'{Colors.RESET}. How can I assist you today?")

    preferred_units = 'metric' # Default unit is Celsius

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi"]:
            print(f"Chatbot: {Colors.BOLD}'Hello!'{Colors.RESET}")
            show_menu()
        elif "how are you" in user_input:
            print("Chatbot: I'm doing well, thank you for asking! How can I help you today?")
            show_menu()
        elif user_input == "units":
            while True:
                unit_choice = input(f"Chatbot: {Colors.BOLD}Which {Colors.GREEN}'unit'{Colors.RESET} would you prefer? (C for Celsius, F for Fahrenheit, K for Kelvin, 'done' to keep current): ").lower().strip()
                if unit_choice == 'c':
                    preferred_units = 'metric'
                    print("Chatbot: Temperature unit set to Celsius.")
                    break
                elif unit_choice == 'f':
                    preferred_units = 'imperial'
                    print(f"Chatbot: {Colors.BOLD}Temperature unit set to Fahrenheit.")
                    break
                elif unit_choice == 'k':
                    preferred_units = 'standard'
                    print(f"Chatbot: {Colors.BOLD}Temperature unit set to Kelvin.")
                    break
                elif unit_choice == 'done':
                    print(f"Chatbot: {Colors.BOLD}Temperature unit remains {get_unit_symbol(preferred_units)}.")
                    break
                else:
                    print("Chatbot: Invalid unit choice. Please enter C, F, or K.")
            show_menu()
        elif user_input == "weather":
            while True:
                city = input(f"Chatbot: {Colors.BOLD}Which city's {Colors.GREEN}'current weather' {Colors.RESET}would you like to know? (Type 'done' to finish): ").lower().strip()
                if city == "done":
                    show_menu()
                    break
                if city == "out":
                    print("Chatbot: Always ready to help you!")
                    return
                weather_info = get_weather(city, preferred_units)
                print(f"Chatbot: {weather_info}\n")
        elif user_input == "forecast":
            while True:
                city = input(f"Chatbot: {Colors.BOLD}Which city's {Colors.GREEN}'5-day/3-hour forecast' {Colors.RESET} would you like to see? (Type 'done' to finish): ").lower().strip()
                if city == "done":
                    show_menu()
                    break
                if city == "out":
                    print("Chatbot: Always ready to help you!")
                    return
                forecast_info = get_forecast(city, preferred_units)
                print(f"Chatbot: {forecast_info}\n")
        elif user_input in ["thank you", "thanks"]:
            print(f"Chatbot: {Colors.BLUE}You're welcome! How else can I help you?")
            show_menu()
        elif user_input == "out":
            print(f"{Colors.RED}Chatbot: Always ready to help you!")
            break
        else:
            print("Chatbot: I'm not sure about that, but I'm always learning!")
            show_menu()

# Run the chatbot
chatbot()
