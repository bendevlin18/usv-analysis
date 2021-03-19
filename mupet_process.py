

import numpy as np
import pandas as pd
import os
from tkinter import *
from tkinter import filedialog

root = Tk()
direc = filedialog.askdirectory(title = 'Select a Folder')

files = [i for i in os.listdir(direc) if '.csv' in i]


final_df = pd.DataFrame(columns = ['num_calls', 'avg_duration', 'total_duration','freq_range', 'freq_band','avg_energy'])

for file in files:
    df = pd.read_csv(os.path.join(direc, file))

    data = {'num_calls' : [len(df)], 
        'avg_duration' : [np.mean(df['syllable duration (msec)'])],
        'total_duration' : [sum(df['syllable duration (msec)'])],
        'freq_range' : [np.max(df['mean frequency (kHz)']) -  np.min(df['mean frequency (kHz)'])],
        'freq_band' : [np.mean(df['frequency bandwidth (kHz)'])],
        'avg_energy' : [np.mean(df['total syllable energy (dB)'])],
        'avg_frequency' : [np.mean(df['mean frequency (kHz)'])],
        'filename' : [file.split('.csv')[0]]
           }

    final_df = final_df.append(pd.DataFrame.from_dict(data))



final_df.to_csv(os.path.join(direc, 'batch_output.csv'))


print('All Done! You can find the processed output here:'+ direc + '/batch_output.csv')