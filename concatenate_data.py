# -*- coding: utf-8 -*-
"""Concatenate Data across excel sheets"""
import os,glob
import pandas as pd
import numpy as np

class concatXLS:
    def __init__(self, sheet_length):
        self.sheet_length=sheet_length #save the sheet names as a variable
        self.all_xls={}
        for u in range(self.sheet_length):
            self.all_xls[u]=pd.DataFrame()
        self.counter=0

    def add_data(self, excelfile_oh):
        # Parse filename
        try:
            base,extension=excelfile_oh.split('.')
            cage, group, animal, brainside, slide, scan, region, neuron, layer = base.split('_')
            neuronid = cage+animal+slide+scan+region+neuron+layer
            xls=pd.ExcelFile(excelfile_oh)
        except:
            print("error with filename:" + excelfile_oh)
        
        # Add the data to sheet dataframe
        for sheet in range(self.sheet_length):
            try:
                df_oh=pd.read_excel(xls,'Neuron Summary')
                
                #Add animal info to data
                df_animalinfo=pd.DataFrame({'cage':np.repeat(cage,df_oh.shape[0],0),
                                'group':np.repeat(group,df_oh.shape[0],0),
                                'animal':np.repeat(animal,df_oh.shape[0],0),
                                'neuronid':np.repeat(neuronid,df_oh.shape[0],0),
                                'layer':np.repeat(layer,df_oh.shape[0],0)})
                
                df_cat=pd.concat([df_oh,df_animalinfo],axis=1)
                self.all_xls[sheet]=pd.concat([self.all_xls[sheet],df_cat],axis=0)

            except:
                print(str(sheet)+" does not exist or something else went wrong")
                
    def output_data(self,output_directory):
        try:
            os.chdir(output_directory)
            for u in range(self.sheet_length):
                string='Neuron Summary'+".xlsx"
                self.all_xls[u].to_excel(string)
            
        except:
            print("error with saving")
        
os.chdir('F:\\LISTON_LAB\\DENDRITIC_SPINE_PROJECT\\neurolucida_anlaysis_golgi\\neurolucida_generated_data\\cellbody\\')
data=concatXLS(1)
        
for excelfile_oh in glob.glob('*xls*'):
    print(excelfile_oh)
    data.add_data(excelfile_oh)

data.output_data('F:\\LISTON_LAB\\DENDRITIC_SPINE_PROJECT\\neurolucida_anlaysis_golgi\\neurolucida_generated_data\\output\\')
        