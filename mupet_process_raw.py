

## importing the necessary packages
import numpy as np
import pandas as pd
import os
from tkinter import *
from tkinter import filedialog

## asking for the folder with the csv output files
root = Tk()
direc = filedialog.askdirectory(title = 'Select a Folder')

## grabbing only the csvs
files = [i for i in os.listdir(direc) if '.csv' in i]

## initializing output dataframe
final_df = pd.DataFrame(columns = pd.read_csv(os.path.join(direc, files[0])).columns)

## looping through the files, extracting all the info, and appending to output dataframe
for i in range(len(files)):
    ds = pd.read_csv(os.path.join(direc, files[i]))
    ds['file'] = files[i]
    final_df = final_df.append(ds)
    
## writing output dataframe to original directory
final_df.to_csv(os.path.join(direc, 'batch_output_raw.csv'))

print('All Done! You can find the processed output here:'+ direc + '/batch_output_raw.csv')