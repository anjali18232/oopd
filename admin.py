# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 01:20:37 2018

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

class admin:
    def __init__(self):
        pass

    def add_doc(self,doctor_name,address,phoneno,specialization,type,opdtime,dept,hod,dept_id,doc_rank,rank_id,password):
        self.doctor_name=doctor_name
        self.address=address
        self.phoneno=phoneno
        self.specialization=specialization
        self.type=type
        self.opdtime=opdtime
        self.dept=dept
        self.hod=hod
        self.dept_id=dept_id
        self.doc_rank=doc_rank
        self.did='d'+ self.doctor_name
        self.rank_id=rank_id
        self.password=password
        login_role=2
        # cursor.execute("INSERT INTO `shs`.`doctor`(`Did`,`Dname`,`address`,`phoneno`,`specialization`,`type`,`opdtime`,`dept`,`hod`,`dept_id`,`doc_rank`,`rank_id`)VALUES(self.did, self.doctor_name,self.address,self.phoneno,self.specialization,self.type,self.opdtime,self.dept,self.hod,self.dept_id,self.doc_rank,self.rank_id);")
        # cursor.execute("INSERT INTO `shs`.`login`(`username`,`password`,`roleid`)VALUES(self.did, self.password,login_role);")
        #cursor.commit()
        sql="INSERT INTO `shs`.`doctor`(Did,Dname,address,phoneno,specialization,type,opdtime,dept,hod,dept_id,doc_rank,rank_id) VALUES('%s','%s','%s',%s,'%s','%s','%s','%s',%s,%s,'%s',%s)"
        val=(self.did, self.doctor_name,self.address,self.phoneno,self.specialization,self.type,self.opdtime,self.dept,self.hod,self.dept_id,self.doc_rank,self.rank_id)
        cursor.execute(sql%val)
        self.role_id=2
        sql="INSERT INTO `shs`.`login`(username,password,role_id) VALUES('%s','%s',%s)"
        val=(self.did,self.password,self.role_id)
        cursor.execute(sql%val)
        db.commit()

    def change_doctor(self,pid,did):
        self.pid=pid
        self.did=did
        cursor.execute("UPDATE `shs`.`patient` Set `assigneddoctor` = '" + self.did + "' where `pid` = '" + pid + "';")
        db.commit()