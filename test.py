import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from alpha_vantage.timeseries import TimeSeries 

print("All libraries loaded")


from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key="04UOYCJDWQCOGUO1")

data, meta = ts.get_daily(
    symbol="AAPL",
    outputsize="compact"
)

print(list(data.items())[:2])