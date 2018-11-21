# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 03:30:03 2018

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
class deptt:
    def __init__(self):
        pass

    def doc_deptt(self, userid):
        self.userid = userid
        cursor.execute("SELECT dept FROM `shs`.`doctor` where Did = '" + self.userid + "';")
        return (cursor.fetchone())

    def doc_deptt_id(self, userid):
        self.userid = userid
        cursor.execute("SELECT dept_id FROM `shs`.`doctor` where Did = '" + self.userid + "';")
        return (cursor.fetchone())
    def get_dept_details(self,dept_id):
        self.dept_id=dept_id
        cursor.execute("SELECT dept_id,name FROM `shs`.`department` where dept_id != '" + str(self.dept_id) + "';")
        return cursor.fetchall()
    def get_dept_list(self):
        cursor.execute("SELECT dept_id,name FROM `shs`.`department`;")
        return cursor.fetchall()

