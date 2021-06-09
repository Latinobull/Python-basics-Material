import os
import time
import pandas as pd

""" Prepare for importing errors and debugging with settings.json"""

while True:
    if os.path.exists("temps_today.csv"):
        data = pd.read_csv("temps_today.csv")
        print(data.mean())
    else:
        print("File does not exist")
    time.sleep(10)
