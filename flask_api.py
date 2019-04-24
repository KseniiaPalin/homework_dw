import sys
import os
import shutil
import time
import traceback
import json

from flask import Flask, request, jsonify

import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/predict', methods=['POST']) # Create http://host:port/predict POST end point
def predict():
    
    try:
        json_ = request.json #capture the json from POST
        data = pd.DataFrame.from_dict(json_)
        # Loading the data
        #data = pd.read_excel('data/data_DWF.xlsx', index_col='index')
        start_lag = 10
        corrcoeff = [data.value.autocorr(lag) for lag in range(start_lag,int(len(data)/2))]
        period = np.argmax(corrcoeff)+start_lag

        return jsonify({'period': str(period)})

    except Exception as e:

        return jsonify({'error': str(e), 'trace': traceback.format_exc()})

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except Exception as e:
        port = 80

    app.run(host='0.0.0.0', port=port, debug=False)
