import csv
import patient
import doctor
from list_of_all_childrens import ChildrenList

doctors = list()

def csv_dict_reader(path):
    with open(path, 'r') as file_obj:
        childs = list()
        reader = csv.DictReader(file_obj, delimiter=',')
        for line in reader:
            tempDoc = doctor.Doctor(line["doctor_first_name"],line["doctor_last_name"],line["doctor_middle_name"])
            doctors.append(tempDoc)
            for doc in doctors:
                if doc.doctor_first_name == tempDoc.doctor_first_name and doc.doctor_last_name == tempDoc.doctor_last_name and doc.doctor_middle_name == tempDoc.doctor_middle_name and tempDoc != doc:
                    doctors.remove(tempDoc)
                    tempDoc = doc
                    break
            # print(line["child_first_name"]),
            childs.append(patient.Patient(line["mother_first_name"], line["mother_last_name"], line["mother_middle_name"],
                                  line["father_first_name"], line["father_last_name"], line["father_middle_name"],
                                  line["child_first_name"], line["child_last_name"], line["child_middle_name"],
                                  line["age"], tempDoc))
        return childs

def write_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["child_first_name","child_last_name","child_middle_name","mother_first_name","mother_last_name","mother_middle_name",
                        "father_first_name","father_last_name","father_middle_name","doctor_first_name","doctor_last_name","doctor_middle_name","age"],
            quoting=csv.QUOTE_ALL
        )
        writer.writeheader()
        writer.writerows(data)

list = csv_dict_reader("input.csv")
childs = ChildrenList(list)

write_csv("output.csv", childs.create_csv_data())

doc = input("Enter surname of doctor to find: ")

for i in doctors:
    if i.doctor_last_name == doc:
        print("List of patients of doctor" , i.doctor_last_name, i.doctor_first_name)
        for j in i.patients:
            print(j.child_last_name,j.child_first_name)

print("Enter new patient Full name, his/her parents Full name, his/her doctor and age")
info = input().split(',')
tempDoc = doctor.Doctor(info[9],info[10],info[11])
doctors.append(tempDoc)
for doc in doctors:
    if doc.doctor_first_name == tempDoc.doctor_first_name and doc.doctor_last_name == tempDoc.doctor_last_name and doc.doctor_middle_name == tempDoc.doctor_middle_name and tempDoc != doc:
        doctors.remove(tempDoc)
        tempDoc = doc
        isNewDoc = False
childs.addChild(patient.Patient(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[12],tempDoc))

write_csv("output.csv", childs.create_csv_data())