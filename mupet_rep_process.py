

import numpy as np
import pandas as pd
import os
from tkinter import *
from tkinter import filedialog

root = Tk()
rep_filename = filedialog.askopenfilename(title = 'Select the syllable sequence file')

rep_df = pd.read_csv(rep_filename)

output_df = pd.DataFrame(rep_df.groupby(['repertoire file', 'repertoire unit (RU) number']).count()['dataset'])

output_dir = filedialog.askdirectory(title = 'Select the output directory')
output_df.to_csv(os.path.join(output_dir, 'batch_rep_output.csv'))


print('All Done! You can find the processed output here:'+ output_dir + '/batch_rep_output.csv')