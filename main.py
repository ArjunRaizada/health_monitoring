import requests
from datetime import datetime

APP_ID = [YOUR-API-ID]
API_KEY_NUTRITION = [YOUR-API-KEY]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers_nutrition = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY_NUTRITION,
}

user_params = {
    "query": input("How much did you exercise ? "),
    "gender": "male",
    "weight_kg": 81,
    "height_cm": 177,
    "age": 19,
}

response_nutrition = requests.post(url=exercise_endpoint, json=user_params, headers=headers_nutrition)
# print(response_nutrition.text)
data_nutrition = response_nutrition.json()

# Data for sheet
today = datetime.now()

date = today.strftime("%d/%m/%y")

time = today.strftime("%H:%M:%S")

exercises = [element["name"] for element in data_nutrition["exercises"]]

duration = [element["duration_min"] for element in data_nutrition["exercises"]]

calories = [element["nf_calories"] for element in data_nutrition["exercises"]]


sheets_endpoint = "https://api.sheety.co/a2f08f55241daa8479ecab4da1eb6cba/workoutTracking/workouts"
API_KEY_SHEETS = [YOUR-API-KEYS]

headers = {
    "Authorization": [YOUR KEY]
}


for i in range(len(exercises)):
    adding_rows_parameters = {
        "workout": {
            "date": str(date),
            "time": str(time),
            "exercise": str(exercises[i]).title(),
            "duration": str(duration[i]),
            "calories": str(calories[i]),
        }
    }
    response = requests.post(url=sheets_endpoint, json=adding_rows_parameters, headers=headers)
    print(response.text)
