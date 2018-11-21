import pymysql
import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)
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

class Algo:
    def __init__(self):
        pass
    def get_availabe_deptt(self):
        cursor.execute("SELECT dept_id,name FROM `shs`.`department`;")
        return cursor.fetchall()
    def get_availabe_doctor(self):
        cursor.execute("SELECT ")
        return



