import json
import os
import pandas as pd
import numpy as np
import joblib

def execute(data):
    try:
        data = json.load(data)['data']
        data = pd.DataFrame.from_dict(data)
        result = model.predict(data)
        return result.predict(data)

    except Exception as exc:
        err = str(exc)
        return err

path = os.path.join(os.getenv('AZURE_MODEL_DIR'), 'model.pkl')
model = joblib.load(path)