import os
import numpy as np
import pandas as pd


def load_file(path):
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            print(os.path.join(dirname, filename))


load_file('../files/titanic')
