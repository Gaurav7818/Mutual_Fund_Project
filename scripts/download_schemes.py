import requests
import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("../data/raw", exist_ok=True)

scheme_codes = [
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

for code in scheme_codes:
    
    url = f"https://api.mfapi.in/mf/{code}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"../data/raw/{code}.csv"

        nav_df.to_csv(filename, index=False)

        print(f"{code} downloaded successfully")
    
    else:
        print(f"Failed to download {code}")