import pickle
import pandas as pd
import os
from backend.config import Config

try:
    path = "backend/assets/bns_assets.pkl" # direct relative path to be safe
    if not os.path.exists(path):
        from backend.config import Config
        path = Config.BNS_ASSETS_PATH

    print(f"Loading from {path}")
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = pickle.load(f)
            df = data['df']
            print("---COLUMNS---")
            for col in df.columns:
                print(col)
            print("---END COLUMNS---")
            item = df.iloc[0]
            print(f"Sample: Section={item.get('Section')}, Simplified={item.get('Simplified Description', 'N/A')}")
    else:
        print("File not found")
except Exception as e:
    print(f"Error: {e}")
