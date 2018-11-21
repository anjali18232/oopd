# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 04:02:10 2018

@author: ABH
"""
import pymysql
from hod import hod
from deptt import deptt
import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)
#########For Connecting to the Database###########################
db = pymysql.connect(

    host="127.0.0.1",  ## Local Host
    # host="192.168.51.210",  ## Local Host
    user="root",  ## UserName
    passwd="password",  ## Password
    db="shs"  ##Database Name
)

#####For creating the Cursor object for Read/Write##################
cursor = db.cursor()


class Doctor(hod):
    def __init__(self):
        pass

    def doc_name(self, userid):
        self.userid = userid
        cursor.execute("SELECT Dname FROM `shs`.`doctor` where `Did` = '" + self.userid + "';")
        return (cursor.fetchone())

    def doc_address(self, userid):
        self.userid = userid
        cursor.execute("SELECT address FROM `shs`.`doctor` where Did = '" + self.userid + "';")
        return (cursor.fetchone())

    def doc_phoneno(self, userid):
        self.userid = userid
        cursor.execute("SELECT phoneno FROM `shs`.`doctor` where Did = '" + self.userid + "';")
        return (cursor.fetchone())

    def doc_specialization(self, userid):
        self.userid = userid
        cursor.execute("SELECT specialization FROM `shs`.`doctor` where Did = '" + self.userid + "';")
        return (cursor.fetchone())

    def doc_opd(self, userid):
        self.userid = userid
        cursor.execute("SELECT opdtime FROM `shs`.`doctor` where Did = '" + self.userid + "';")
        return (cursor.fetchone())

    def doc_hod_status(self,userid):
        h=hod()
        self.userid=userid
        usernm=self.userid
        status = h.get_hod_status(usernm)
        return (status)

    def doc_rank(self, userid):
        self.userid = userid
        cursor.execute("SELECT rank FROM `shs`.`doctor` where Did = '" + self.userid + "';")
        return (cursor.fetchone())



    def doc_rank(self, userid):
        self.userid = userid
        cursor.execute("SELECT rank_id FROM `shs`.`doctor` where Did = '" + self.userid + "';")
        return cursor.fetchone()

    def refer_doctor(self, patient_ID, doctor_id):
        self.patient_ID = patient_ID
        self.doctor_id = doctor_id
        cursor.execute(
            "UPDATE `shs`.`patient` Set `assigneddoctor` = '" + doctor_id + "' where `pid` = '" + patient_ID + "';")
        db.commit()

    def doc_list(self, doctor_level, dept_id):
        self.doctor_level = doctor_level
        self.dept_id = dept_id
        cursor.execute("SELECT Dname , Did , doc_rank FROM `shs`.`doctor` where rank_id >  '" + str(
            self.doctor_level) + "' and dept_id='" + str(self.dept_id) + "';")
        return (cursor.fetchall())

    def doc_list(self, dept_id):
        self.dept_id = dept_id
        cursor.execute(
            "SELECT Did,Dname,phoneno,specialization,type,opdtime FROM `shs`.`doctor` where dept = '" + self.dept_id + "';")
        return cursor.fetchall()

    def doc_deptt(self,userid):
        d = deptt()
        self.userid=userid
        usernm=self.userid
        dept=d.doc_deptt(usernm)
        return dept
    def doc_deptt_id(self,userid):
        d = deptt()
        self.userid=userid
        usernm=self.userid
        dept=d.doc_deptt_id(usernm)
        return dept

    def view_patient_name(self, pid):
        self.pid = pid
        cursor.execute("SELECT pname FROM `shs`.`patient` where pid = '" + self.pid + "';")
        return (cursor.fetchone())

    def view_patient_history(self, pid):
        self.pid = pid
        cursor.execute("SELECT medical_history FROM `shs`.`patient_medical_history` where pid = '" + self.pid + "';")
        return (cursor.fetchone())

    def set_doc_name(self, new_name, user_name):
        self.user_name = user_name
        self.new_name = new_name
        cursor.execute("UPDATE `shs`.`doctor` Set `Dname` = '" + new_name + "' where `Did` = '" + user_name + "';")
        db.commit()

    def set_doc_phoneno(self, new_phone, user_name):
        self.user_name = user_name
        self.new_phone = new_phone
        cursor.execute("UPDATE `shs`.`doctor` Set `phoneno` = '" + new_phone + "' where `Did` = '" + user_name + "';")
        db.commit()

    def set_doc_address(self, new_address, user_name):
        self.user_name = user_name
        self.new_address = new_address
        cursor.execute("UPDATE `shs`.`doctor` Set `address` = '" + new_address + "' where `Did` = '" + user_name + "';")
        db.commit()

    def set_doc_opd_timing(self, new_timing, user_name):
        self.new_timing = new_timing
        self.user_name = user_name
        cursor.execute("UPDATE `shs`.`doctor` Set `opdtime` = '" + new_timing + "' where `Did` = '" + user_name + "';")
        db.commit()

    def get_doc_list(self, dept_id):
        self.dept_id = dept_id
        cursor.execute(
            "SELECT Did,Dname,specialization,type, opdtime, doc_rank FROM `shs`.`doctor` where dept_id = '" + str(
                self.dept_id) + "';")
        return cursor.fetchall()

    def doctor_refer_patient(self, doc_id, patient_id, dept_Id):
        self.doc_id = doc_id
        self.patient_id = patient_id
        self.dept_id = dept_Id
        cursor.execute("UPDATE `shs`.`patient` Set `Department_id` = '" + dept_Id + "',assigneddoctor='" + str(
            self.doc_id) + "' where `pid` = '" + patient_id + "';")

    def patient_need_help(self, user_id):
        self.user_id = user_id
        crc = True
        cursor.execute(
            "SELECT pid,pname,critical FROM `shs`.`patient` where assigneddoctor = '" + self.user_id + "' and critical=True;")
        return (cursor.fetchall())

    def doc_detail(self, did):
        self.did = did
        cursor.execute(
            "SELECT Did,Dname,phoneno,specialization,type, opdtime, dept FROM `shs`.`doctor` where did = '" + self.did + "';")
        return (cursor.fetchall())

    def patient_profile(self, val):
        self.val = val
        cursor.execute(
            "SELECT pid, pname, paddress,location,assigneddoctor FROM `shs`.`patient` where pid = '" + self.val + "';")
        return cursor.fetchone()

    def view_profile(self,Did):
        d=Doctor()
        self.Did=Did
        id=self.Did
        d_name=d.doc_name(id)
        print("Welcome to SHS \n", d_name[0])
        d_spl=d.doc_specialization(id)
        print("Specialization", d_spl[0])
        d_opd=d.doc_opd(id)
        print("OPD timing", d_opd[0])
        d_dept=d.doc_deptt(id)
        print("Department", d_dept[0])

    def contact_info(self,Did):
        d = Doctor()
        self.Did = Did
        id = self.Did
        d_add = d.doc_address(id)
        print("Address ", d_add[0])
        d_cno = d.doc_phoneno(id)
        print("Contact no:", d_cno[0])

    def algorithm(self, doctor_deptt, time_slot):
        self.doctor_deptt = doctor_deptt
        self.time_slot = time_slot
        cursor.execute(
            "SELECT * FROM `shs`.`appointment`,`shs`.`doctor` WHERE appointment.Did IN (SELECT Did from `shs`.`doctor` WHERE  dept_id='" + str(
                self.doctor_deptt) + "') AND appointment.Did=doctor.Did AND appointment.Time_Slot!='" + self.time_slot + "';")
        return cursor.fetchall()

    def get_doctor_time_slot(self, doctor_id):
        self.doctor_id = doctor_id
        cursor.execute("SELECT Time_Slot from `shs`.`appointment` WHERE  Did='" + self.doctor_id + "';")
        return cursor.fetchall()
        # cursor.execute("SELECT Did FROM `shs`.`department` where dept_id = '" + self.doctor_deptt + "';")

    def assign_random(self, pid):
        self.pid = pid
        cursor.execute(
            "UPDATE `shs`.`appointed_patients` SET Pid='" + self.pid + "' WHERE Pid IS NULL ORDER BY Date LIMIT 1;")
        db.commit()




#    def view_patient_history(self):
#    def view_patients_appointed(self):
#    def check_critical_patients(self):
#    def sort_patients(self):
#    def refer_patient(self):
