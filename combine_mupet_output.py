
import numpy as np
import pandas as pd
import os
from tkinter import *
from tkinter import filedialog, simpledialog

root = Tk()

## gathering files
meta_filename = filedialog.askopenfilename(title = 'Select the metadata file')
df_filename = filedialog.askopenfilename(title = 'Select the batch output file')

## opening files
meta = pd.read_csv(meta_filename)[['Pup Number', 'File legend', 'Sex', 'Genotype', 'litter_size']]
df = pd.read_csv(df_filename)

## cleaning output dataframe
age = ['P8'] * len(df)
file_legend = df['filename'].copy()

for i in range(len(df['filename'])):
    if 'P15' in df['filename'][i]:
        age[i] = 'P15'
        file_legend[i] = '_'.join(df['filename'][i].split('_')[0:-2] + [df['filename'][i].split('_')[-1]])
        
df['age'] = age
df['file_legend'] = file_legend

## making sure the keys are case-consistent
meta['File legend'] = meta['File legend'].str.lower()
df['file_legend'] = df['file_legend'].str.lower()

## merging the files together
output = df.set_index('file_legend').join(meta.set_index('File legend'))

## asking for output directory and outputting the combined file
output_dir = filedialog.askdirectory(title = 'Select the output directory')

## get a suffix for the filenaming
suffix = simpledialog.askstring('', 'Suffix for the filename?')


## write out the final csv
output.to_csv(os.path.join(output_dir, 'combined_data_' + suffix + '.csv'))

print('All Done! You can find the processed output here: '+ output_dir + '/combined_data' + suffix + '.csv')
