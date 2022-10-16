# from serial.tools import list_ports
# import serial
# import time
# import csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import neurokit2 as nk

eog_signal = nk.data('eog_100hz')
eog_cleaned = nk.eog_clean(eog_signal, sampling_rate = 100, method = 'neurokit')
nk.signal_plot(eog_signal)
# ports = list_ports().comports()
# for port in ports: 
#     print(port)

