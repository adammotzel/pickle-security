"""
Create sample pickle file.
"""

import os
import pickle as pkl


root = os.getcwd()

with open(f"{root}/container/sample.pkl", "wb") as file:
    pkl.dump("Hello World!", file)
    