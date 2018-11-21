# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 02:08:56 2018

@author: ABH
"""
import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)
import pymysql

#########For Connecting to the Database###########################
db = pymysql.connect(

    host="127.0.0.1",  ## Local Host
    #host="192.168.51.210",  ## Local Host
    user="root",  ## UserName
    passwd="password",  ## Password
    db="shs"        ##Database Name
)

#####For creating the Cursor object for Read/Write##################
cursor = db.cursor()

#class hospital has composition relationship with doctor,department and patient

from doctor import Doctor
from deptt import deptt
from patient import patient

class Hospital:
    def __init__(self):
        self.deptt=deptt()
        self.Doctor=Doctor()
        self.patient=patient()
        
    def get_deptt(self):
        for d in self.deptt:
            print(d)
    def get_doc(self):
        for d in self.doc:
            print(d)
    def get_patient(self):
        for p in self.paitent:
            print(p)