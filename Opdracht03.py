import requests
import pandas as pd

req = requests.get("https://catfact.ninja/breeds")

data = req.json()["data"]
data = pd.DataFrame(data=data)

print(data["breed"])
data.to_csv("CatBreedData.csv")
