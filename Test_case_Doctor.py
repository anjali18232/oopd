
import sys
from doctor import doctor 
from patient import patient 
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


class Testdoctor(unittest.TestCase):
    
    def testdoc_phoneno(self):
        result=p.doc_phoneno(self,'p101')
        self.assertEqual(result,8950389803)
        
    def testdoc_specialization(self):
        result1=p.doc_specialization(self,'pdimple')
        self.assertEqual(result1,0)
        
    def testdoc_opd(self):
        result2=p.doc_opd(self,'pneha')
        self.assertEqual(result2,0)
    
    def testdoc_rank(self):
        result3=p.doc_ranks(self,'panjali')
        self.assertEqual(result3,0)
        
    def testdoc_deptt(self):
        result4=p.doc_deptt(self,'ppriya')
        self.assertEqual(result4,0)
        
    def testdoc_rank(self):
        result6=p.getdoc_rank(self,'pdeepti')
        self.assertEqual(result6,0)

if '__name__' == '__main__':
    unittest.main(defaultTest='Testdoctor')