# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 21:21:20 2016

@author: cwei
"""

import pandas
import numpy as np
from os import listdir

path = 'T:/courses/MsiA400/jobs/job_descriptions/'



files = [f for f in listdir(path) if f[-17:] == '_descriptions.csv']
print files

def extra_info(f):
    descriptions = pandas.read_csv(path + f, 
                    sep = ',', names = ['id','description'])
    descriptions.description = descriptions.description.str.lower()
    #print descriptions.iloc[883,1]
    descriptions['title'] = np.nan
    descriptions['job_type'] = np.nan
    
    
    print list(descriptions.columns.values)
    
    
    title = ['volunteer','engineer ','software engineer', 'director','inspector','data scientist', 'financial analyst', 'teacher', 
    'accountant', 'consultant','auditor','manager','store manager', 'project manager','driver','therapist','sales representative'
    'researcher', ' analyst ', 'sales associate','technician','developer','Nurse','instructor','professor']
    job_type = ['part-time','intern ']
    for i in title:
        c = descriptions['description'].map(lambda x: i in x.lower())
        descriptions.loc[c, 'title'] = i
    print float(len(descriptions) - descriptions['title'].count())/len(descriptions)
    #descriptiobns.head
    
    
    c = descriptions['description'].map(lambda x: 'intern ' in x.lower() or 'internship' in x.lower())
    descriptions.loc[c, 'job_type'] = 'internship'
    c = descriptions['description'].map(lambda x: 'part-time' in x.lower())
    descriptions.loc[c, 'job_type'] = 'part-time'
    
    
    descriptions['job_type'].fillna('full-time')
    print float(len(descriptions[descriptions['job_type'] == 'internship']))/len(descriptions['job_type'])


 #job types, minimum year requirement, industry, whether intern
#industry: finance, marketing, technology, insurance, university, high school, consulting
#accounting, non-profit, government, investment banking
#education: bechelor, master, phd


extra_info(files[0])
