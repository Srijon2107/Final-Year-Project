import os
import pickle
import sys
from config import Config

def test_load():
    print("Testing ML Model Loading...")
    
    # Test Crime Model
    print(f"Checking Crime Model at: {Config.CRIME_MODEL_PATH}")
    if os.path.exists(Config.CRIME_MODEL_PATH):
        try:
            with open(Config.CRIME_MODEL_PATH, 'rb') as f:
                model = pickle.load(f)
            print(f"SUCCESS: Crime model loaded. Type: {type(model)}")
        except Exception as e:
            print(f"FAILURE: Could not load crime model. Error: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("FAILURE: Crime model file does not exist.")

    # Test BNS Assets
    print(f"Checking BNS Assets at: {Config.BNS_ASSETS_PATH}")
    if os.path.exists(Config.BNS_ASSETS_PATH):
        try:
            with open(Config.BNS_ASSETS_PATH, 'rb') as f:
                assets = pickle.load(f)
            print(f"SUCCESS: BNS assets loaded. Keys: {assets.keys()}")
        except Exception as e:
            print(f"FAILURE: Could not load BNS assets. Error: {e}")
            import traceback
            traceback.print_exc()
    else:
        print("FAILURE: BNS assets file does not exist.")

if __name__ == "__main__":
    test_load()
