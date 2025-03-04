from fastapi import FastAPI
from datetime import datetime
import json

app = FastAPI()

# Load tortoise facts from JSON file
with open("facts.json", "r") as file:
    tortoise_facts = json.load(file)

@app.get("/api/fact")
def get_tortoise_fact():
    today = datetime.now().strftime("%m-%d")
    fact = tortoise_facts.get(today, "No fact available for today!")
    return {"date": today, "fact": fact}

# Run with: uvicorn main:app --reload
