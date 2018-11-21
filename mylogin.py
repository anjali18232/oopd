# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:34:58 2018

@author: ABH
"""
import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)
import pymysql
db = pymysql.connect(

    host="127.0.0.1",  ## Local Host
    #host="192.168.51.210",  ## Local Host
    user="root",  ## UserName
    passwd="password",  ## Password
    db="shs"        ##Database Name
)

#####For creating the Cursor object for Read/Write##################
cursor = db.cursor()
class mylogin:
    def __init__(self,user_name,password,role):
        self.user_name=user_name
        self.password=password
        self.role=role
    def confirmuser(self,user_name,password,role):
        cursor.execute("SELECT * FROM `shs`.`login` where username = '" + user_name + "'and password='"+ password +"'and role_id='"+ role +"';")
        #print(cursor.fetchall())
        return(cursor.fetchone())