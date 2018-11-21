# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 02:03:13 2018

@author: ABH
"""
import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)
logger=logging.getLogger(__name__)
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

class hod:
    def __init__(self):
        pass
    def get_resp(self,ad_resp):
        self.ad_resp=ad_resp
        return self.ad_resp

    def get_hod_status(self,userid):
        self.userid=userid

        try:
            try:
                cursor.execute("SELECT hod FROM `shs`.`doctor` where Did = '" + self.userid + "';")
            except (pymysql.Error, pymysql.Warning) as e:
                print(e)
                logging.info(e)
                return None
            try:
                result=cursor.fetchone()
                return result
            except TypeError as e:
                print(e)
                return None
        finally:
            db.close()



