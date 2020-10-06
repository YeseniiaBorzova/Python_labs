import patient

class Doctor:
    def __init__(self,doctor_first_name, doctor_last_name,doctor_middle_name):
        self.doctor_first_name = doctor_first_name
        self.doctor_last_name = doctor_last_name
        self.doctor_middle_name = doctor_middle_name
        self.patients = list()

    def add_Patient(self, patient):
        self.patients.append(patient)

    def del_Patient(self, patient):
        self.patients.remove(patient)