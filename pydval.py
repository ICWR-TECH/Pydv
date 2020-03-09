#!/usr/bin/python

###################################
# Data Validator By R&D ICWR      #
# Copyright (c)2020 - Afrizal F.A #
###################################
import re

class validator():
    def __init__(self):
        pass
    
    def matching(self,key,data):
        valid_data=[]
        for x in key:
            array_data=re.findall(x.lower(),data.lower())
            if array_data:
                valid_data.append(array_data)
        return valid_data

    def multi_matching(self,data_key,data_input):
        valid_data=[]
        i=0
        for x in data_input:
            i=i+1
            valid_data.append({i:self.matching(data_key,x)})
        return valid_data

###################################
# Data Validator By R&D ICWR      #
# Copyright (c)2020 - Afrizal F.A #
###################################
import re

class validator():
    def __init__(self):
        pass
    
    def matching(self,key,data):
        valid_data=[]
        for x in key:
            array_data=re.findall(x.lower(),data.lower())
            if array_data:
                valid_data.append(array_data)
        return valid_data

    def multi_matching(self,data_key,data_input):
        valid_data=[]
        i=0
        for x in data_input:
            i=i+1
            valid_data.append({i:self.matching(data_key,x)})
        return valid_data
