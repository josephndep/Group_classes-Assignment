#### Version Final Project ####
#### JOSEPH NDEPUH #####
import os
import math

class Doctor:
    doctors_files = []
    def _init_(self, id, name, specilist, timing, qualification, roomNB):
        self.id = id
        self.name = name
        self.specilist = specilist
        self.timing = timing
        self.qualification = qualification
        self.roomNB = roomNB
        
    #####Getters@#####   
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_specilist(self):
        return self.specilist
    
    def get_timing(self):
        return self.timing
    
    def get_qualification(self):
        return self.qualification
    
    def get_roomNB(self):
        return self.roomNB
    
    #######Setters#########
    def set_id(self, id):
        self.id = id
    
    def set_name(self, name):
        self.name = name
    
    def set_specilist(self, specilist):
        self.specilist = specilist
    
    def set_timing(self, timing):
        self.timing = timing
        
    def set_qualification(self, qualification):
        self.qualification = qualification
    
    def set_roomNB(self, roomNB):
        self.roomNB = roomNB   
    
    def enterDrInfo(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        specilist = input("Enter specialization: ")
        timing = input("Enter working period: ")
        qualification = input("Enter Qualifications: ")
        roomNB = input("Enter Room Number: ")
        
        doctors_info = Doctor(id, name, specilist, timing, qualification, roomNB)
        return doctors_info
    
    def readDoctorsFile(self):
        myfile = open("Project_class individual assignment\doctors.txt", 'r')
        read_file = myfile.readlines()
        
        for everyline in read_file:
            self.doctors_files = everyline.split("_")
            doctors = Doctor(self.doctors_files[0],self.doctors_files[1],self.doctors_files[2],
                             self.doctors_files[3],self.doctors_files[4],self.doctors_files[5],)
            self.doctors_files.append(doctors)
            print(f'  {self.doctors_files[0]}, {self.doctors_files[1]}, {self.doctors_files[2]}, {self.doctors_files[3]}, {self.doctors_files[4]},{self.doctors_files[5]}')
            
    # def doctorMenu(self):
    #     print("1 - Display doctors list")
    #     print("2 - Search for doctor by ID")
    #     print("3 - Search for doctor by name")
    #     print("4 - Add doctor")
    #     print("5 - Edit doctor Info")
    #     print("6 - Back to main Menu") 
    #     doctor_menu = int(input("Enter Menu: "))
    #     return doctor_menu       
    
    def searchDoctorbyID(self):
        doctors_name = input("Enter name: ")
        id_readfile = open("doctors.txt", "r")
        find_doctor = id_readfile.read()
        
        for everyline in find_doctor:
            self.doctors_files = everyline.split("_")
            if doctors_name not in Doctor(self.name):
                print(f'{doctors_name} not found in Query')
            else:
                if doctors_name in Doctor(self.name):
                    print(f'{self.doctors_files[0]}')
                    
    def displayDrInfo(self):
        doctors_select = input("Select an Option")
        print("1 - Display doctors list")
        print("2 - Search for doctor by ID")
        print("3 - Search for doctor by name")
        print("4 - Add doctor")
        print("5 - Edit doctor Info")
        print("6 - Back to main Menu")
        return doctors_select
                         
    # def displayDrInfo(self):
    #     mydoctors_file = open("Project_class individual assignment\doctors.txt", "r")
    #     display_info = mydoctors_file.readlines()
        
    #     for everyline in display_info:
    #         self.doctors_files = everyline.split("_")
    #         doctors = Doctor(self.doctors_files[0],self.doctors_files[1],self.doctors_files[2],
    #                          self.doctors_files[3],self.doctors_files[4],self.doctors_files[5],)
    #         self.doctors_files.append(doctors)
    #         print(f' {self.doctors_files[0]}, {self.doctors_files[1]}, {self.doctors_files[2]}, {self.doctors_files[3]}, {self.doctors_files[4]},{self.doctors_files[5]}')
            
class Faculty:
    facilities = []
    def _init_(self, ambulance, admitFacility, canteen, emergency):
        self.ambulance = ambulance
        self.admitFacility = admitFacility
        self.canteen = canteen
        self.emergency = emergency
    
    def get_ambulance(self):
        return self.ambulance
    
    def get_admitFacility(self):
        return self.admitFacility
    
    def get_canteen(self):
        return self.canteen
    
    def get_emergency(self):
        return self.emergency
    
    def set_ambulance(self, ambulance):
        self.ambulance = ambulance
    
    def set_admitFacility(self, admitFacility):
        self.admitFacility = admitFacility
    
    def set_canteen(self, canteen):
        self.canteen = canteen
        
    def set_emergency(self, emergency):
        self.emergency = emergency
    
    def addFacility(self):
        new_facility = input("Enter new facility: ")
        facilities = Faculty(new_facility)
        return facilities
    
    def displayFacilities(self):
        myfile2 = open("Project_class individual assignment\facilities.txt",'r')
        file_content2 = myfile2.readlines()
         #print file content
        for eachline in file_content2:
            self.facilities = eachline.split("_")
            toys = Faculty(self.facilities[0],self.facilities[1],self.facilities[2])
            self.facilities.append(toys)
            print(f'  {self.facilities[0]}, {self.facilities[1]}')
    
    def writeListOfFacilitiesToFile(self):
        myfile2 = open("Project_class individual assignment\facilities.txt",'r')
        for i in range(len(Faculty.facilities)):
            myfile2.write(self.facilities[i])

class Laboratory:
    list_lab = []
    def _init_(self, facility, cost):
        self.facility = facility
        self.cost = cost
        
    def get_facility(self):
        return self.facility
    
    def get_cost(self):
        return self.cost
    
    def set_facility(self, facility):
        self.facility = facility
    
    def set_cost(self, cost):
        self.cost = cost
    
    def enterLaboratoryInfo(self):
        facility = input("Enter new Lab name: ")
        cost = input("Enter cost: ")
        lab_info = Laboratory(facility, cost)
        return lab_info
               
    def addLabToFile(self):
        myfile3 = open("C:\MC216\Project_class individual assignment\laboratories.txt", 'a') 
        new_labinfo = self.enterLaboratoryInfo()
        myfile3.write(new_labinfo)
        myfile3.close()
    
    def displayLabsList(self):
        myfile3 = open("C:\MC216\Project_class individual assignment\laboratories.txt", 'r') 
        lab_display = myfile3.readlines()
        
        for eachline in lab_display:
            self.list_lab = eachline.split("_")  
            labs = Laboratory(self.list_lab[0], self.list_lab[1], self.list_lab[2], self.list_lab[3] )
            self.list_lab.append(labs) 
            print(f' {self.list_lab[0],self.list_lab[1] }') 
    
    def writeListOfLabsToFile(self):
        myfile3 = open("C:\MC216\Project_class individual assignment\laboratories.txt", 'w') 
        for i in range(len(Laboratory.list_lab)):
            myfile3.write(self.list_lab[i])
    
    def readLaboratoryInfo(self):
        myfile3 = open("C:\MC216\Project_class individual assignment\laboratories.txt", 'r')
        lab_read = myfile3.readlines()
        
        for eachline in lab_read:
            self.list_lab = eachline.split("_")  
            labs = Laboratory(self.list_lab[0], self.list_lab[1], self.list_lab[2], self.list_lab[3] )
            self.list_lab.append(labs) 
            print(f' {self.list_lab[0],self.list_lab[1] }') 
    
    def formatFileInfo(self):
        myfile3 = open("Project_class individual assignment\laboratories.txt",'r')
        format_file = myfile3.readlines()
        
        for eachline in format_file:
            self.list_lab = eachline.split("_") 
            labs = Laboratory(self.list_lab[0], self.list_lab[1], self.list_lab[2], self.list_lab[3] )
            self.list_lab.append(labs) 
            print(f' {self.list_lab[0],self.list_lab[1] }') 

class Patient:
    patients_list = []
    def _init(self, id, Name, Disease, Gender, Age):
        self.id = id
        self.Name = Name
        self.Disease = Disease
        self.Gender = Gender
        self.Age = Age
    
    def get_id(self):
        return self.id
    
    def get_Name(self):
        return self.Name
    
    def get_Disease(self):
        return self.Disease
    
    def get_Gender(self):
        return self.Gender
    
    def get_Age(self):
        return self.Age
    
    def set_id(self, id):
        self.id = id
    
    def set_Name(self, Name):
        self.Name = Name
    
    def set_Disease(self, Disease):
        self.Disease = Disease
    
    def set_Gender(self, Gender):
        self.Gender = Gender
    
    def set_Age(self, Age):
        self.Age = Age
    
    def enterPatientInfo(self):
        id = input("Enter ID info: ")
        Name = input("Enter name: ")
        Disease = input("Enter type of disease: ")
        Gender = input("Enter gender: ")
        Age = input("Enter age: ") 
        patient_info = Patient(self, id, Name, Disease, Gender, Age)
        return patient_info
               
    def addPatientToFile(self):
        myfile4 = open("C:\MC216\Project_class individual assignment\patients.txt", 'a') 
        new_patientInfo = self.enterPatientInfo()
        myfile4.write(new_patientInfo)
        myfile4.close()
    def displayPatientsList(self):
        return
        
        
    # def displayPatientsList(self):
    #     myfile4 = open("C:\MC216\Project_class individual assignment\patients.txt", 'r') 
    #     patient_display = myfile4.readlines()
        
    #     for eachline in patient_display:
    #         self.list_lab = eachline.split("_")  
    #         patient = Laboratory(self.patients_list[0], self.patients_list[1], self.patients_list[2], self.patients_list[3] )
    #         self.patients_list.append(patient) 
    #         print(f' {self.patients_list[0],self.patients_list[1] }') 
    
    def writeListOfPatientsToFile(self):
        myfile4 = open("C:\MC216\Project_class individual assignment\patients.txt", 'w') 
        for i in range(len(Patient.patients_list)):
            myfile4.write(self.patients_list[i])
    
    def readPatientsFile(self):
        myfile4 = open("C:\MC216\Project_class individual assignment\patients.txt", 'r')
        patients_read = myfile4.readlines()
        
        for eachline in patients_read:
            self.patients_list = eachline.split("_")  
            patient = Laboratory(self.patients_list[0], self.patients_list[1], self.patients_list[2], self.patients_list[3] )
            self.patients_list.append(patient) 
            print(f' {self.patients_list[0],self.patients_list[1] }') 
    
    def formatFileInfo(self):
        myfile3 = open("Project_class individual assignment\laboratories.txt",'r')
        format_file = myfile3.readlines()
        
        for eachline in format_file:
            self.list_lab = eachline.split("_") 
            labs = Laboratory(self.list_lab[0], self.list_lab[1], self.list_lab[2], self.list_lab[3] )
            self.list_lab.append(labs) 
            print(f' {self.list_lab[0],self.list_lab[1] }') 

# class Management(Doctor, Faculty, Laboratory, Patient):
    print("Welcome to Alberta Hospital (AH) Managment system ")
    print("Select from the following options, or select 0 to stop:")
    print("1 - 	Doctors")
    print("2 - 	Facilities")
    print("3 - 	Laboratories")
    print("4 - 	Patients")
    menu_select = input("Select an Option: ")
    if menu_select == 0:
        pass
    elif menu_select == 1:
        display_DrInfo = Doctor.displayDrInfo()
        print(display_DrInfo)
    
Doctor.displayDrInfo()
        
