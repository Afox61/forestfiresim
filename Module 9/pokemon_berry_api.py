import requests
response = requests.get('http://www.google.com')
print(response.status_code)

from pydantic import BaseModel

class Berry(BaseModel):
    id: int
    name: str
    flavor: str
    effect: str

berries = [
    {"id": 1, "name": "Oran Berry", "flavor": "Sweet", "effect": "restores 10 HP"},
    {"id": 2, "name": "Sitrus Berry", "flavor": "Bitter", "effect": "restores 25% HP"},
    {"id": 3, "name": "Lum Berry", "flavor": "Neutral", "effect": "cures all status condition"},
    {"id": 4, "name": "Cheri Berry", "flavor": "Spicy", "effect": "cures paralysis"},
    {"id": 5, "name": "Chesto Berry", "flavor": "Dry", "effect": "awakens sleeping Pokémon"},
]

from fastapi import FastAPI, HTTPException
from data import berries
from models import Berry

app= FastAPI()

@app.getd("/")
def home():
    return {"measage": "Welcome to the Pokémon Berry API!"}

@app.get("/berries", response_model=List[Berry])
def get_all_berries():
    return berries

@app.get("/berries/{berry_id}", response_model=Berry) 
def get_berry(berry_id: int):
    berry = next((b for b in berries if berry["id"] == berry_id), None)
    if berry is None:
        raise HTTPException(status_code=404, detail="Berry not found")
    return berry

@app.post("/berries", response_model=Berry)  
def add_berry(berry: Berry):
    berries.append(berry.dict())
    return berry  
@app.delete("/berries/{berry_id}")
def delete_berry(berry_id: int):
    global berries
    berries = [b for b in berries if b["id"] != berry_id]
    return {"message": "Berry deleted successfully"}