# Weather Chatbot

This Python-based chatbot helps users find current weather information and 5-day weather forecasts for desired cities. It also allows setting the preferred temperature unit (Celsius, Fahrenheit, Kelvin).

## Features

* **Current Weather:** Displays the current weather details (description, temperature, wind speed and direction, humidity, pressure) for a specified city.
* **5-Day Weather Forecast:** Provides a 5-day (with 3-hour intervals) weather forecast for a given city.
* **Temperature Unit Selection:** Users can set their preferred temperature unit to Celsius (°C), Fahrenheit (°F), or Kelvin (°K).
* **User-Friendly Interaction:** Simple text-based interface for easy retrieval of weather information.
* **Multiple City Queries:** Users can inquire about the weather or forecast for multiple cities using the `weather` or `forecast` commands.
* **Exit Command:** Safely exit the chatbot using the `OUT` command.

## How to Run

1.  **Install Required Libraries:**

    ```bash
    pip install requests
    ```

2.  **Obtain an OpenWeatherMap API Key:**

    * Sign up for a free API key at [OpenWeatherMap](https://openweathermap.org/).

3.  **Add the API Key to the Code:**

    * Open the `chatbot_wetter.py` file.
    * Replace `'YOUR_API_KEY'` in the `API_KEY = 'YOUR_API_KEY'` line with your actual API key.

4.  **Run the Chatbot:**

    ```bash
    python chatbot_wetter.py
    ```

    or

    ```bash
    python3 chatbot_wetter.py
    ```

## Usage

After running the chatbot, you can interact with it using the following commands:

* **`hi` or `hello`:** Greets the chatbot and displays the main menu.
* **`weather`:** Prompts you to enter the name of the city for current weather information. Type `done` to finish.
* **`forecast`:** Prompts you to enter the name of the city for the 5-day weather forecast. Type `done` to finish.
* **`units`:** Allows you to select your preferred temperature unit (C, F, or K). Type `done` to keep the current unit.
* **`OUT`:** Exits the chatbot.

## Example Interaction
Hello! I'm an advanced chatbot. How can I assist you today?
Type 'weather' to get current weather information for a city.
Type 'forecast' to get a 5-day/3-hour weather forecast for a city.
Type 'units' to set your preferred temperature unit (C, F, K).
Type 'OUT' to exit.

You: hi
Chatbot: Hello! How are you?

What would you like to do?
Type 'weather' to get current weather information for a city.
Type 'forecast' to get a 5-day/3-hour weather forecast for a city.
Type 'units' to set your preferred temperature unit (C, F, K).
Type 'OUT' to exit.

You: weather
Chatbot: Which city's current weather would you like to know? (Type 'done' to finish): london
Weather in london: Mist.
Temperature: 11.99°C
Wind Speed: 2.68 m/s
Humidity: %94
Pressure: 1011 hPa
Wind Direction: WSW

Chatbot: Which city's current weather would you like to know? (Type 'done' to finish): done

What else would you like to do? (weather, forecast, units, OUT)

You: forecast
Chatbot: Which city's 5-day/3-hour forecast would you like to see? (Type 'done' to finish): berlin
5-day/3-hour forecast for berlin:

2025-05-05 16:00:00: Light rain, Temp: 12.14°C
2025-05-05 19:00:00: Light rain, Temp: 10.86°C
2025-05-05 22:00:00: Clear, Temp: 9.47°C
2025-05-06 01:00:00: Clear, Temp: 8.46°C
2025-05-06 04:00:00: Clear, Temp: 7.87°C
Chatbot: Which city's 5-day/3-hour forecast would you like to see? (Type 'done' to finish): done

What else would you like to do? (weather, forecast, units, OUT)

You: units
Chatbot: Which unit would you prefer? (C for Celsius, F for Fahrenheit, K for Kelvin, 'done' to keep current): f
Chatbot: Temperature unit set to Fahrenheit.

What else would you like to do? (weather, forecast, units, OUT)

You: out
Chatbot: Always ready to help you!
