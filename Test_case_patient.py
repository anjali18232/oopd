import sys
from doctor import doctor 
from patient import patient as p
from admin import admin
from hosiptal import Hospital 
from HOD import HOD as hod
import pymysql
import unittest
from datetime import *
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


class Testpatient(unittest.TestCase):
    
    def testview_profile(self):
        result=p.view_profile(self,'p102')
        self.assertEqual(result,895789)
        
    def testview_medical_history(self):
        result1=p.view_medical_history(self,'pneha')
        self.assertEqual(result1,1)
        
    def testchange_name(self):
        result2=p.change_name(self,'panjli')
        self.assertEqual(result2,1)
    
    def testchange_address(self):
        result3=p.doc_rank(self,'pvivek')
        self.assertEqual(result3,0)
        
    def testsearch_doctor_by_id(self):
        result4=p.search_doctor_by_id(self,'ppriya')
        self.assertEqual(result4,0)
        

if '__name__' == '__main__':
    unittest.main(defaultTest='Testpatient')