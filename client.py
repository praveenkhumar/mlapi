import requests

url = "http://127.0.0.1:5000/predict"

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

response = requests.post(
    url,
    json={
        "marks": marks,
        "attendance": attendance
    }
)

print(response.json())