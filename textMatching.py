'''Simple Script to Label Item Description''' 

#import libraries packages 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import string 
import re
import json 

#read from csv 
data = pd.read_csv('./item.csv')

item = data['Item Description']

#data cleaning (lowercase, remove whitespace, remove numbers, remove punctutions)
item = item.str.lower() #change to lowercase 

#keyword for each label 
medical_surgical_label = ['revision', 'replacement', 'reposition']
obstet_label = ['abortion', 'extraction', 'transplantation'] 
placement_label = ['removal', 'dressing', 'compression']
admin_label = ['irrigation', 'introduction']
osteo_label = ['osteopathic']
chiro_label = ['chiropractic']
imaging_label = ['fluoroscopy', 'ct scan', 'computerized tomography', 'ultrasonography']
mental_label = ['crisis', 'management', 'psychological']
radiation_label = ['cesium', 'radiation', 'photon', 'radiosurgery']
nuclear_label = ['nuclear']

#check string contains any keyword above and label accordingly 
for i in item.shape: 
	for row in medical_surgical_label:
		item[item.str.contains(row)] = 'Medical and Surgical'
	for row in obstet_label: 
		item[item.str.contains(row)] = 'Obstetrics'
	for row in placement_label:
		item[item.str.contains(row)] = 'Placement'
	for row in admin_label:
		item[item.str.contains(row)] = 'Administration'
	for row in osteo_label:
		item[item.str.contains(row)] = 'Osteopathic'
	for row in chiro_label:
		item[item.str.contains(row)] = 'Chiropractic'
	for row in imaging_label:
		item[item.str.contains(row)] = 'Imaging'
	for row in mental_label:
		item[item.str.contains(row)] = 'Mental Health'
	for row in radiation_label:
		item[item.str.contains(row)] = 'Radiation Therapy'
	for row in nuclear_label:
		item[item.str.contains(row)] = 'Nuclear Medicine'

print(item)