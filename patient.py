import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)


import pymysql
import datetime

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
from doctor import Doctor
class patient:
    def __init__(self):
        pass
    def view_profile(self,pid):
        self.pid=pid
        cursor.execute("SELECT pid,pname,paddress,location,assigneddoctor, critical, Department_id FROM `shs`.`patient` where pid = '" + self.pid + "';")
        return cursor.fetchone()
    def view_medical_history(self,pid):
        self.pid=pid
        cursor.execute("SELECT pid,medical_history FROM `shs`.`patient_medical_history` where pid = '" + self.pid + "';")
        return cursor.fetchone()
    def change_name(self,pid,name):
        self.pid=pid
        self.name=name
        cursor.execute("UPDATE `shs`.`patient` Set `pname` = '" + self.name + "' where `pid` = '" + self.pid + "';")
        db.commit()
    def change_address(self,new_address,pid):
        self.new_address=new_address
        self.pid=pid
        cursor.execute("UPDATE `shs`.`patient` Set `paddress` = '" + self.new_address + "' where `pid` = '" + self.pid + "';")
        db.commit()

    def search_doctor_by_id(self, did):
        self.did = did
        cursor.execute(
            "SELECT Did,Dname,phoneno,specialization,type, opdtime, dept FROM `shs`.`doctor` where did = '" + self.did + "';")
        return (cursor.fetchone())

    def doctor_by_name(self, dname):
        self.dname = dname
        cursor.execute(
            "SELECT Did,Dname,specialization,type, opdtime, dept FROM `shs`.`doctor` where Dname = '" + self.dname + "';")
        return cursor.fetchall()

    def doctor_by_address(self, address):
        self.address = address
        cursor.execute(
            "SELECT Did,Dname,specialization,type, opdtime, dept,address FROM `shs`.`doctor` where address = '" + self.address + "';")
        return (cursor.fetchall())

    def doctor_by_specialization(self, specialization):
        self.specialization = specialization
        cursor.execute(
            "SELECT Did,Dname,specialization,type, opdtime, dept,address FROM `shs`.`doctor` where specialization = '" + self.specialization + "';")
        return (cursor.fetchall())

    def get_appointment(self, did, pid, timeslot, deptt_id):
        self.did = did
        self.pid = pid
        self.timeslot = timeslot
        self.deptt_id = deptt_id
        now = datetime.now()
        # print(now.strftime("%d/%m/%Y"))
        date = now.strftime("%d/%m/%Y")
        sql = "INSERT INTO `shs`.`appointment`(Pid,Did,Time_slot,Date) VALUES('%s','%s','%s','%s')"
        val = (self.pid, self.did, self.timeslot, date)
        cursor.execute(sql % val)
        db.commit()
        cursor.execute("UPDATE `shs`.`patient` Set `assigneddoctor` = '" + self.did + "',`Department_id` = '" + str(
            self.deptt_id) + "' where `pid` = '" + self.pid + "';")
        db.commit()
        print("Appointment Successfully created")

    def get_sort_by_name(self, did):
        self.did = did
        cursor.execute(
            "SELECT pname,pid,paddress,critical FROM `shs`.`patient` WHERE pid IN (SELECT Pid FROM `shs`.`appointed_patients` WHERE Did='" + str(
                self.did) + "' AND Pid IS NOT NULL) ORDER BY pname")
        return cursor.fetchall()

    def get_sort_by_id(self, did):
        self.did = did
        cursor.execute(
            "SELECT pname,pid,paddress,critical FROM `shs`.`patient` WHERE pid IN (SELECT Pid FROM `shs`.`appointed_patients` WHERE Did='" + str(
                self.did) + "' AND Pid IS NOT NULL) ORDER BY pid")
        return cursor.fetchall()

    def get_sort_by_type(self, did):
        self.did = did
        cursor.execute(
            "SELECT pname,pid,paddress,critical FROM `shs`.`patient` WHERE pid IN (SELECT Pid FROM `shs`.`appointed_patients` WHERE Did='" + str(
                self.did) + "' AND Pid IS NOT NULL) ORDER BY critical")
        return cursor.fetchall()

    def book_ward(self,userid):
        self.userid = userid
        c='1'
        cursor.execute("SELECT count FROM `shs`.`rooms_available` where uid = '" + c + "';")
        rooms = cursor.fetchone()
        rooms = rooms[0]

        if rooms > 0:
            rooms = rooms-1
            cursor.execute("UPDATE `shs`.`rooms_available` SET `count`  = '" + str(rooms) + "' where `uid` = '" + c + "';")
            cursor.execute("SELECT assigneddoctor FROM `shs`.`patient` where pid = '" + self.userid + "';")
            did = cursor.fetchone()
            did=did[0]
            cursor.execute("SELECT dept FROM `shs`.`Doctor` where did = '" + did + "';")
            deptt = cursor.fetchone()
            now=datetime.datetime.now()
            now=str(now)
            rooms=str(rooms)
            sql = "INSERT INTO SHS.local (pid,did,dept,Room_no,admit_date_time) VALUES (%s,%s,%s,%s,%s)"
            val = (self.userid, did, deptt,rooms,now)
            cursor.execute(sql, val)
            db.commit()
        else:
            print("Sorry no rooms are available!")

    def setpatientdetails(self, pid, p_name, p_add, p_location, critical):
        self.pid=pid
        self.p_name=p_name
        self.p_add=p_add
        self.p_location=p_location
        self.critical=critical
        sql = "INSERT INTO SHS.patient (pid,pname,paddress,location,critical) VALUES (%s,%s,%s,%s,%s)"
        val = (self.pid,self.p_name, self.p_add, self.p_location, self.critical)
        cursor.execute(sql, val)
        db.commit()

    def doctor_profile(self):
        print("Enter the name of the doctor whose profile you want to view")
        name=input()
        cursor.execute("SELECT Did FROM `shs`.`doctor` where Dname = '" + name + "';")
        userid= cursor.fetchall()
        userid=userid[0]
        l1=Doctor()
        l1.view_profile(userid[0])
        logging.info("executed")

    def doctor_contact_info(self):
        print("Enter the name of the doctor whose profile you want to view")
        name = input()
        name = str(name)
        cursor.execute("SELECT Did FROM `shs`.`doctor` where Dname = '" + name + "';")
        userid = cursor.fetchall()
        userid = userid[0]
        l1 = Doctor()
        l1.contact_info(userid[0])

    def view_doctors_schedule(self, userid):
        self.userid = userid
        cursor.execute("SELECT Time_slot FROM `shs`.`appointment` where did = '" + self.userid + "';")
        time = cursor.fetchall()
        cursor.execute("SELECT Pid FROM `shs`.`appointment` where did = '" + self.userid + "';")
        pid = cursor.fetchall()
        cursor.execute("SELECT Date FROM `shs`.`appointment` where did = '" + self.userid + "';")
        date = cursor.fetchall()
        for t in time:
            for y in t:
                print(y)
        for t in pid:
            for y in t:
                print(y)
        for t in date:
            for y in t:
                print(y)

    def change_medical_history(self, user_id, data):
        self.data = data
        self.user_id = user_id
        cursor.execute(
            "UPDATE `shs`.`patient_medical_history` Set `medical_history` = '" + self.data + "' where `pid` = '" + self.user_id + "';")
        db.commit()















