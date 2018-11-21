
import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)
import sys
import pymysql
from Hospital import Hospital
from admin import admin
from hod import hod
from doctor import Doctor
from mylogin import mylogin
from deptt import deptt
from patient import patient
#from patient import patient

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
options_left = 3
# login
if __name__ == '__main__':
    logging.info("execution started")
    while (True):
        print("*******************************************")
        print("*---------Smart Health System-------------*")
        print("*******************************************")
        print("************Choose Login Details***********")
        print("*            1. Doctor Login              *")
        print("*            2. Patient Login             *")
        print("*            3. Admin Login               *")
        print("*******************************************")
        choice = int(input("your choice is"))
        if (choice == 1):
            user_name = input("Enter username")
            Password = input("Enter Password")
            role = '101'
            l1 = mylogin(user_name, Password, role)
            confirm = l1.confirmuser(user_name, Password, role)
            if (confirm == None):
                print("your credential are wrong please retry?")
                if options_left <= 1:
                    sys.exit()
                else:
                    options_left -= 1

            else:
                print("You are logged in")
                #            confirmuser(self,user_name,Password)
                #                cursor.execute("SELECT * FROM `shs`.`login` where username = '" + user_name + "'and password='"+ Password +"'and role_id='101';")
                #                print(cursor.fetchall())
                #                print(cursor.fetchone())
                # check into database
                print("***************************************************")
                print("*---------You have logged in as Doctor -----------*")
                print("***************************************************")
                while True:
                    print("*-------------------------------------------------------------*")
                    print("*     1. View Profile                                         *")
                    print("*     2. Edit Profile                                         *")
                    print("*     3. Check patients History/Profile                       *")
                    print("*     4. patients Appointed Today(sorted order)               *")
                    print("*     5. Check Emergency/Critical condition patients(need help)")
                    print("*     6. Refer patient to senior doctor                       *")
                    print("*     7. logout                                               *")
                    print("*-------------------------------------------------------------*")
                    value = int(input("Enter Choice"))
                    if (value == 1):
                        print("*-------------------------------------------*")
                        print("*    #####Your Profile######                *")
                        print("*-------------------------------------------*")
                        print(" ###########################################")
                        l1 = Doctor()
                        confirm = l1.doc_name(user_name)
                        address = l1.doc_address(user_name)
                        phoneno = l1.doc_phoneno(user_name)
                        specialization = l1.doc_specialization(user_name)
                        opd_timing = l1.doc_opd(user_name)
                        deptt = l1.doc_deptt(user_name)
                        deptt_id = l1.doc_deptt_id(user_name)
                        hod_status = l1.doc_hod_status(user_name)
                        #                        deptt_rank= l1.doc_rank(user_name)
                        print("Your Name is " + ', '.join(confirm))
                        print("Your Address is " + ', '.join(address))
                        for element in phoneno:
                            print("Your Phone Number is", element)
                        print("Your Specialization is " + ', '.join(specialization))
                        print("Your OPD Timeings is" + ', '.join(opd_timing))
                        print("Your Department is " + ', '.join(deptt))
                        if(hod_status==1):
                            print("You are HOD")

                        else:

                            print("You are not HOD")

                        for element in deptt_id:
                            print("Your Department ID is", element)
                    #                        print("Your Rank is"+', '.join(deptt_rank))
                    elif (value == 2):
                        print("*------------------------------------------*")
                        print("*    #####Options you want to edit######      *")
                        print("*------------------------------------------*")
                        print("############################################")
                        print("1. Edit your Name")
                        print("2. Edit your phoneno")
                        print("3. Edit your Address")
                        print("4. Edit your OPD  timings")
                        val = int(input("Select your choice"))
                        if (val == 1):
                            l1 = Doctor()
                            name = l1.doc_name(user_name)
                            nn = name[0]
                            print("Your Current Name is ", nn)
                            new_name = input("Enter your new name")
                            l1.set_doc_name(new_name, nn)
                            print("Your name has been modified")
                        elif (val == 2):
                            l1 = Doctor()
                            phone_no = l1.doc_phoneno(user_name)
                            for element in phone_no:
                                print("Your Current Phone Number is ", element)
                            new_name = input("Enter your new phone number")
                            l1.set_doc_phoneno(new_name, user_name)
                            print("Your phone Number has been modified")
                        elif (val == 3):
                            l1 = Doctor()
                            address = l1.doc_address(user_name)
                            print("Your Current address is " + ', '.join(address))
                            new_name = input("Enter your new address")
                            l1.set_doc_address(new_name, user_name)
                            print("Your address has been modified")
                        elif (val == 4):
                            l1 = Doctor()
                            opd_timings = l1.doc_opd(user_name)
                            print("Your Current opd timings are " + ', '.join(opd_timings))
                            new_timing = input("Enter new opd timings")
                            l1.set_doc_opd_timing(new_timing, user_name)
                            print("Your opd-timing has been modified")
                        else:
                            print("Your option is Incorrect")
                    elif (value == 3):
                        print("*-------------------------------------------*")
                        print("*    #####patients History/Profile######    *")
                        print("*-------------------------------------------*")
                        print(" ########################################### ")
                        ###access from database
                        pid = input("Enter the Patient id you want search")
                        l1 = Doctor()
                        name = l1.view_patient_name(pid)
                        history = l1.view_patient_history(pid)
                        print("Patient Name is", name)
                        #                        for element in history:
                        print("Patient Medical History is", history)
                        val = int(input("1. choose to edit medical history"))
                        user_id = input("Enter Patient ID")
                        if (val == 1):
                            p1 = patient()
                            data = p1.view_medical_history(user_id)
                            print("Current Medical History", data)
                            new_data = input("Enter New Data")
                            p1.change_medical_history(user_id, new_data)

                    elif (value == 4):
                        print("*---------------------------------------------------------*")
                        print("*    #####patients Appointed Today in sorted order######  *")
                        print("*---------------------------------------------------------*")
                        print("*        1. sort patients by ID                           *")
                        print("*        2. sort by name                                  *")
                        print("*        3. sort by type                                  *")
                        print("*---------------------------------------------------------*")
                        sort = int(input("#####Select an option based on which you want to search#####"))
                        if (sort == 1):
                            p1 = patient()
                            val = p1.get_sort_by_id(user_name)
                            for x in val:
                                print(x)
                        elif (sort == 2):
                            p1 = patient()
                            val = p1.get_sort_by_name(user_name)
                            for x in val:
                                print(x)
                        elif (sort == 3):
                            p1 = patient()
                            val = p1.get_sort_by_type(user_name)
                            for x in val:
                                print(x)
                        else:
                            print("Choose a correct option")
                    elif (value == 5):
                        print("*-------------------------------------------------------------------*")
                        print("*    ####List of parents which are in need of help/Emergency####    *")
                        print("*-------------------------------------------------------------------*")
                        print(" ###########################################")
                        p1 = Doctor()
                        patient_list = p1.patient_need_help(user_name)
                        print("List of Critical Patients")
                        for element in patient_list:
                            print("The Patient Id is '%s' Patient Name is %s Patient condition is '%s'" % (
                            element[0], element[1], element[2]))
                    elif (value == 6):
                        print("*-------------------------------------------------------------------*")
                        print("*     #####Refer patient ######                     *")
                        print("*-------------------------------------------------------------------*")
                        l1 = Doctor()
                        doc_level = l1.doc_rank(user_name)
                        doctor_level = doc_level[0]
                        deptt_id = l1.doc_deptt_id(user_name)
                        dept_id = deptt_id[0]
                        print(dept_id)
                        if (doctor_level == 1 or doctor_level == 2):
                            print("1. Refer to senior doctor ")
                            print("2. View List of Senior Doctor, their ID and Specialization")
                            value = int(input("Select your option"))
                            if (value == 1):
                                patient_ID = input("Enter ID of patient you want to refer ")
                                doctor_id = input("Enter ID of Senior doctor you want to refer")
                                l1 = Doctor()
                                l1.refer_doctor(patient_ID, doctor_id)
                                print(
                                    "You refered the patient '%s' to the '%s' senior doctor " % (patient_ID, doctor_id))
                            if (value == 2):
                                docs_list = l1.doc_list(doctor_level, dept_id)
                                print("List of Doctors")
                                for element in docs_list:
                                    print("Doctor Name '%s' Specialization '%s', Doctor ID '%s'" % (
                                    element[0], element[1], element[2]))
                        elif (doctor_level == 3):
                            print("1. Refer to another department")
                            print("2. Refer to senior Doctor")
                            val = int(input("Enter a choice"))
                            if val == 1:
                                print("1. view list of department")
                                print("2. view list of doctor in a deptt")
                                print("3. Refer Patient to another department")
                                val = int(input("Choose one option"))
                                if (val == 1):
                                    d1 = deptt()
                                    l1 = Doctor()
                                    deptt = l1.doc_deptt_id(user_name)
                                    print(deptt[0])
                                    dept_id = deptt[0]
                                    dept_list = d1.get_dept_details(dept_id)
                                    print("List of all Departments in Hospital is:")
                                    for element in dept_list:
                                        print("Department Name %s and department ID '%s' is" % (element[0], element[1]))
                                elif (val == 2):
                                    print("List of Doctors in the Department you want to search")
                                    dept_id = input("Enter the Department Id To find Doctors in Department")
                                    l1 = Doctor()
                                    doc_list = l1.get_doc_list(dept_id)
                                    for element in doc_list:
                                        print(
                                            "Department Name '%s' and department ID '%s' is" % (element[0], element[1]))
                                elif (val == 3):
                                    doc_id = input("Enter the Id of New Doctor")
                                    patient_id = input("Enter the id of patient you want to Refer")
                                    dept_Id = input("New Department Patient to be referred")
                                    l1 = Doctor()
                                    l1.doctor_refer_patient(doc_id, patient_id, dept_Id)
                            elif val == 2:
                                print("1. Refer to senior doctor ")
                                print("2. View List of Senior Doctor, their ID and Specialization")
                                value = int(input("Select your option"))
                                if (value == 1):
                                    patient_ID = input("Enter ID of patient you want to refer ")
                                    doctor_id = input("Enter ID of Senior doctor you want to refer")
                                    l1 = Doctor()
                                    l1.refer_doctor(patient_ID, doctor_id)
                                    print("You refered the patient '%s' to the '%s' senior doctor " % (
                                    patient_ID, doctor_id))
                                elif (value == 2):
                                    docs_list = l1.doc_list(doctor_level, dept_id)
                                    print("List of Doctors")
                                    for element in docs_list:
                                        print("Doctor Name '%s' Specialization '%s', Doctor ID '%s'" % (
                                        element[0], element[1], element[2]))

                        else:
                            print("1. Enter the De to another department")

                    elif (value == 7):
                        logging.info("execution completed")
                        sys.exit()
                    else:
                        print("*-------------------------------------------------------------------*")
                        print("     ####Choose correct/valid option####")
                        print("*-------------------------------------------------------------------*")
                        print(" ###########################################")
        elif (choice == 2):
            print("*---------------------------------------------------------------------------*")
            print("*    ######patient######")
            print("*---------------------------------------------------------------------------*")
            print("*    1.login already existing account                                       *")
            print("*    2.create a new account                                                 *")
            print("*---------------------------------------------------------------------------*")
            choice = int(input("Enter choice"))
            if (choice == 1):
                user_name = input("Enter username")
                Password = input("Enter Password")
                role = '102'
                l1 = mylogin(user_name, Password, role)
                confirm = l1.confirmuser(user_name, Password, role)
                if (confirm == None):
                    print("your credential are wrong please retry?")
                    if options_left <= 1:
                        sys.exit()
                    else:
                        options_left -= 1
                else:
                    print("You are logged in")
                    # print("----------You have logged in as User ------------")
                    while True:
                        print("*--------------------------------------------*")
                        print("*     1. View/ History Profile               *")
                        print("*     2. Edit profile                        *")
                        print("*     3. View Doctor categories              *")
                        print("*     4. Search doctor                       *")
                        print("*     5. Book Appointment                    *")
                        print("*     6. View Doctor Profile                 *")
                        print("*     7. view doctor schedule                *")
                        print("*     8. Doctor's contact information        *")
                        print("*     9. Logout                              *")
                        print("*--------------------------------------------*")
                        value = int(input("input your choice"))
                        if (value == 1):
                            while True:
                                print("*--------------------------------------------*")
                                print("*   #####View your profile######             *")
                                print("*--------------------------------------------*")
                                p1 = patient()
                                print("1. View your Personal Profile")
                                print("2. View your Medical History")
                                print("3. View your Main Profile")
                                val = int(input("Choose one option"))
                                if (val == 1):
                                    val = p1.view_profile(user_name)
                                    print("*--------------------------------------------*")
                                    print("            Your Personal Profile             ")
                                    print("*--------------------------------------------*")
                                    print("PID:         ", val[0])
                                    print("Name:        ", val[1])
                                    print("Address:     ", val[2])
                                    print("Location:    ", val[3])
                                    print("Doctor ID:   ", val[4])
                                    print("Condition:   ", val[5])
                                elif (val == 2):
                                    val = p1.view_medical_history(user_name)
                                    print("*-------------------------------------------*")
                                    print("            Your Medical History             ")
                                    print("---------------------------------------------")
                                    val = p1.view_medical_history(user_name)
                                    print("PID:                       ", val[0])
                                    print("Your Medical History:      ", val[1])
                                elif (val == 3):
                                    print("Go To back menu")
                                    break
                                else:
                                    print("Choose Correct Value")
                        elif (value == 2):
                            print("--------------------------------------------*")
                            print("*   #####Edit your Personal Profile######            *")
                            print("*-------------------------------------------*")
                            print("----------Your Current Profile---------------")
                            p1 = patient()
                            val = p1.view_profile(user_name)
                            print("PID:         ", val[0])
                            print("Name:        ", val[1])
                            print("Address:     ", val[2])
                            print("Location:    ", val[3])
                            print("Doctor ID:   ", val[4])
                            print("Condition:   ", val[5])
                            print("*----Choose One Edit Option----*")
                            print("1. Edit Your Name")
                            print("2. Edit Your Address")
                            print("*------------------------------*")
                            value = int(input("Choose an Option"))
                            if (value == 1):
                                current_name = user_name
                                print("Your Current Name is:", val[1])
                                value = input("Enter New Name")
                                p1.change_name(current_name, value)
                                print("Your Name Changed Successfully")
                            elif (value == 2):
                                print("Your Current address:", val[2])
                                address = input("Enter New Address")
                                p1.change_address(address, user_name)
                                print("Your Address Changed Successfully")
                        elif (value == 3):
                            print("*-------------------------------------------*")
                            print("*   #####List of Categories of Doctors###### *")
                            print("*-------------------------------------------*")

                            # result from database
                        elif (value == 4):
                            print("*------------------------------------------*")
                            print("*     ####search doctors###                *")
                            print("*------------------------------------------*")
                            print("*    1. search doctor by ID                *")
                            print("*    2. search doctor by Name              *")
                            print("*    3. search doctor by Address           *")
                            print("*    4. search doctor by specialization   *")
                            print("*------------------------------------------*")
                            search = input("Enter option by which you want to search")

                            if (value == 1):
                                print("*------------------------------------------*")
                                print("*   ### you are searching doctor by        *")
                                print("*------------------------------------------*")
                                doctor_id = input("Enter ID of Doctor you want to search")
                                d1 = patient()
                                val = d1.search_doctor_by_id(doctor_id)
                                print("Doctor ID:", val[0])
                                print("Doctor Name:", val[1])
                                print("Doctor Specialization:", val[2])
                                print("Doctor Type", val[3])
                                print("OPD Time", val[4])
                                print(" Doctor Department", val[5])
                                print("---------------------------------------------")
                                # result from database
                            if (value == 2):
                                print("*------------------------------------------*")
                                print("*    ### you are searching doctor by Name  *")
                                print("*------------------------------------------*")
                                Doctors = input("Enter Name of Doctor you want to search")
                                print("*------------------------------------------*")

                                d1 = patient()
                                val = d1.doctor_by_name(Doctors)
                                count = 1
                                for y in val:
                                    print("Doctor", count, ":")
                                    print("--------------------------------------")
                                    print("Doctor Department:               ", y[5])
                                    print("DID:                             ", y[0])
                                    print("Doctor Name:                     ", y[1])
                                    print("Specialization:                  ", y[2])
                                    print("Doctor Type:                     ", y[3])
                                    print("Doctor OPD Time                  ", y[4])
                                    print("--------------------------------------")
                                    count += 1
                                # result from database
                            if (value == 3):
                                print("*------------------------------------------*")
                                print("*   ### you are searching doctor by ID     *")
                                print("*------------------------------------------*")
                                Doctors = input("Enter Name of Doctor you want to search")
                                d1 = patient()
                                val = d1.doctor_by_address(Doctors)
                                count = 1
                                for y in val:
                                    print("Doctor", count, ":")
                                    print("--------------------------------------")
                                    print("Doctor Department:               ", y[5])
                                    print("DID:                             ", y[0])
                                    print("Doctor Name:                     ", y[1])
                                    print("Address:                         ", y[6])
                                    print("Specialization:                  ", y[2])
                                    print("Doctor Type:                     ", y[3])
                                    print("Doctor OPD Time                  ", y[4])
                                    print("--------------------------------------")
                                    count += 1
                                # result from database
                            if (value == 4):
                                print("--------------------------------------------")
                                print("     ### you are searching doctor by Specailzation")
                                print("--------------------------------------------")
                                ###provide list of Spatialization of Doctor
                                Doctors = input("Enter Specialization of Doctor you want to search")
                                d1 = patient()
                                val = d1.doctor_by_specialization(Doctors)
                                count = 1
                                for y in val:
                                    print("Doctor", count, ":")
                                    print("--------------------------------------")
                                    print("Doctor Department:               ", y[5])
                                    print("DID:                             ", y[0])
                                    print("Doctor Name:                     ", y[1])
                                    print("Doctor Address:                  ", y[6])
                                    print("Specialization:                  ", y[2])
                                    print("Doctor Type:                     ", y[3])
                                    print("Doctor OPD Time                  ", y[4])
                                    print("--------------------------------------")
                                    count += 1
                            else:
                                print("You have entered wrong option")
                        elif (value == 5):
                            print("--------------------------------------------")
                            print("    #####Book appointment######")
                            print("--------------------------------------------")
                            val = int(input("Enter 1 for random allotment and 2 for your own choice"))
                            if (val == 1):
                                doctor_deptt = input("Select Department ID")
                                print("1. Emergency")
                                print("2. Not Emergency")
                                inn = int(input("Enter the choice"))
                                if inn == 1:
                                    print("Doctor Fee Would be Rs. 2000/-...")
                                    print("Do you wish to continue")
                                    innn = input("Y/N")
                                    if innn == 'Y':
                                        d1 = Doctor()
                                        d1.assign_random(user_name)
                                    elif innn == 'N':
                                        pass

                                elif inn == 2:
                                    pass

                                # Intelligent algo and search for doctors by admin based on catogries and all other option

                            elif (val == 2):
                                d1 = patient()
                                doctor_deptt = int(input("Select an Department"))
                                print("1. Allocation based on Fixed Doctor")
                                print("2. Allocation Based on Time Slot")
                                x = int(input("Enter Choice"))
                                if (x == 1):
                                    count = 1
                                    select_doctor_id = input("Select an Doctor ID")
                                    print("Already Booked Slots:")
                                    d1 = Doctor()
                                    val = d1.get_doctor_time_slot(select_doctor_id)
                                    for app in val:
                                        print(count, ":  ", app[0])
                                        count += 1
                                    time_slot = input("Enter the time slot")
                                    p1 = patient()
                                    p1.get_appointment(select_doctor_id, user_name, time_slot, doctor_deptt)
                                elif (x == 2):
                                    time_slot = input("Enter the time slot")
                                    d1 = Doctor()
                                    val = d1.algorithm(doctor_deptt, time_slot)
                                    count = 1
                                    for y in val:
                                        print("Doctor", count, ":")
                                        print("--------------------------------------")
                                        print("Doctor Department:               ", y[5])
                                        print("DID:                             ", y[2])
                                        print("Doctor Name:                     ", y[7])
                                        print("Specialization:                  ", y[10])
                                        print("Doctor Type:                     ", y[11])
                                        print("--------------------------------------")
                                        count += 1
                                    select_doc = input("Select One Doctor ID out of list")
                                    p1 = patient()
                                    cursor.execute(
                                        "SELECT location FROM `shs`.`patient` where pid = '" + user_name + "';")
                                    loc = cursor.fetchone()
                                    loc = loc[0]

                                    l1 = patient()
                                    if loc == '1':
                                        # l1.book_appointment()
                                        p1.get_appointment(select_doc, user_name, time_slot, doctor_deptt)

                                        l1.book_ward(user_name)
                                    else:
                                        p1.get_appointment(select_doc, user_name, time_slot, doctor_deptt)

                                        # l1.book_appointment()

                                # Intelligent algo search for doctors by user based on catogries and all other option
                            else:
                                print("--------------------------------------------")
                                print("Enter a valid input")
                                print("--------------------------------------------")
                                print("--------------------------------------------")
                                print(" ###########################################")



                                # Intelligent algo search for doctors by user based on catogries and all other option

                        elif (value == 6):
                            print("--------------------------------------------")
                            print("     #####View Doctor's Profile######")
                            print("--------------------------------------------")
                            print(" ###########################################")
                            l1=patient()
                            l1.doctor_profile()
                            # from database using classes
                        elif (value == 7):
                            print("--------------------------------------------")
                            print("     #####View Doctor's schedule#####")
                            print("--------------------------------------------")
                            print(" ###########################################")
                            print("Enter the name of doctor whose schedule you want to view")
                            dnam=input()
                            cursor.execute("SELECT did FROM `shs`.`doctor` where Dname = '" + dnam + "';")
                            did = cursor.fetchone()
                            did=did[0]
                            l=patient()
                            l.view_doctors_schedule(did)
                            # from database using classes
                        elif (value == 8):
                            print("--------------------------------------------")
                            print("     ######doctor's contact information#####")
                            print("--------------------------------------------")
                            print(" ###########################################")
                            l=patient()
                            l.doctor_contact_info()
                            # from database using classes
                        elif (value == 9):
                            sys.exit()
                        else:
                            print("--------------------------------------------")
                            print("     ###Choose correct/valid option###")
                            print("--------------------------------------------")
                            print(" ###########################################")

            elif (choice == 2):
                print("--------------------------------------------")
                print("    ######Enter your Details######")
                print("--------------------------------------------")
                name = input("Enter your Name")
                username = input("Enter your username")
                password = input("Enter your password")
                age = input("enter your age")
                sex = input("Enter your gender")
                phoneno = input("Enter your phone number")
                address = input("Enter your address")
                location = input("Enter 1 for local and 2 for opd")
                critical = input("Enter 0 for critical and 1 for not critical")
                print("--------------------------------------------")
                print("--------------------------------------------")
                ### insert into database in usertalbe genrating unique id and display it to user
                pid = 'p' + name
                p=patient()
                p.setpatientdetails(pid, name, address, location, critical)



                ### insert into database in usertalbe genrating unique id and display it to user
                print("-------------------------------------------------------")
                print("###Your account has been created you can login Now#####")
                print("-------------------------------------------------------")
                sys.exit()
        elif (choice == 3):
            user_name = input("Enter username")
            password = input("Enter Password")
            # check from database
            role = '103'
            l1 = mylogin(user_name, password, role)
            confirm = l1.confirmuser(user_name, password, role)
            if (confirm == None):
                print("your credential are wrong please retry?")
                if options_left <= 1:
                    sys.exit()
                else:
                    options_left -= 1
            else:
                print("You are logged in")
                print("----------You have logged in as User ------------")
                while True:
                    print("------------------------------------------------")
                    print("      1. View Doctors Profile(Details)          ")
                    print("      2. View patient's Profile(Details)        ")
                    print("      3. Add a Doctor                           ")
                    print("      4. Re-assign an doctor to patient         ")
                    print("------------------------------------------------")
                    value = int(input("Choose an option"))
                    if (value == 1):
                        while True:
                            print("--------------------------------------------")
                            print("   ######View Doctors Profile(Details)######")
                            print("--------------------------------------------")
                            print("1. View list of Department")
                            print("2. View list of Doctor,DoctorID in a department")
                            print("3. View Doctor Profile ")
                            print("4. Go to main loop")
                            value = int(input("Choose an option"))
                            if (value == 1):
                                count = 1
                                print("-------------------------------------------------------------------")
                                print("List of all Departments is ")
                                print("-------------------------------------------------------------------")
                                d = deptt()
                                v = d.get_dept_list()
                                for element in v:
                                    print("%s :Department id '%s'          Department Name '%s'" % (
                                    count, element[0], element[1]))
                                    count += 1
                            elif value == 2:
                                dept_id = input("Enter Department Id to see list")
                                count = 1
                                print("------------------------------------------------------------------")
                                print("List of Doctors in selected Department is")
                                print("-------------------------------------------------------------------")
                                d = Doctor()
                                v = d.doc_list(dept_id)
                                for element in v:
                                    print("%s: Doctor Id: '%s' ,Doctor Name: '%s'" % (count, element[0], element[1]))
                                    count += 1
                            elif value == 3:
                                print("------------------------------------------------------------------")
                                print("View Doctor Profile")
                                print("------------------------------------------------------------------")
                                doc_id = input("Enter the Doctor id ")
                                d = Doctor()
                                v = d.doc_detail(doc_id)
                                for element in v:
                                    print(" Doctor Id:                                       ", (element[0]))
                                    print("Doctor Name:                                      ", (element[1]))
                                    print("Phone No:                                         ", (element[2]))
                                    print("Specialization:                                   ", (element[3]))
                                    print("Doctor Type:                                      ", (element[4]))
                                    print("OPD Timings:                                      ", (element[5]))
                            elif value == 4:
                                break
                            else:
                                print("Enter a valid choice")

                    elif (value == 2):
                        print("--------------------------------------------")
                        print("   ######View Patient's Profile#####        ")
                        print("--------------------------------------------")
                        val = input("Enter pid of patient")
                        l1 = Doctor()
                        patient_profile = l1.patient_profile(val)
                        print("Patient ID", patient_profile[0])
                        print("Name:", patient_profile[1])
                        print("Address:", patient_profile[2])
                        print("OPD Type:", patient_profile[3])
                        print("Assigned Doctor's ID:", patient_profile[4])
                        # print("The Patient with PID '%s' has Name '%s' ,his address is '%s' has opd type '%s' and the doctor has Did '%s'"%(patient_profile[0],patient_profile[1],patient_profile[2],patient_profile[3],patient_profile[4]))
                    elif (value == 3):
                        print("--------------------------------------------")
                        print("   ######Add a doctor######                 ")
                        print("--------------------------------------------")
                        doctor_name = input("Name of New Doctor")
                        doctor_password = input("Enter Password")
                        address = input("Enter the address of doctor")
                        phoneno = int(input("Enter Phone Number"))
                        specialization = input("Enter Doctor Specialization")
                        type = input("Doctor Type")
                        opdtime = input("input OPD Time")
                        dept = input("Enter Dept Name")
                        hod = input("Enter Hod in Boolean")
                        dept_id = int(input("Enter Department ID"))
                        doc_rank = input("Enter Specialization")
                        rank_id = int(input("Input Rank ID"))
                        doc = admin()
                        doc.add_doc(doctor_name, address, phoneno, specialization, type, opdtime, dept, hod, dept_id,
                                    doc_rank, rank_id, password)
                    elif (value == 4):
                        print("--------------------------------------------")
                        print("   #####Re-assign a doctor to patient###### ")
                        print("--------------------------------------------")
                        patient_id = input("Enter ID of patient")
                        did = input("Enter New Doctor Id")
                        d1 = admin()
                        d1.change_doctor(patient_id, did)
                        print("changed")

                    else:
                        print("--------------------------------------------")
                        print("   ###Choose correct/valid option###        ")
                        print("--------------------------------------------")

        else:
            print("--------------------------------------------")
            print("Choose an correct/valid option?")
            print("--------------------------------------------")
