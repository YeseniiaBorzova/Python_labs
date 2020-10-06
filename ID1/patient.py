import doctor

class Patient:
    def __init__(self,mother_first_name, mother_last_name,mother_middle_name,
                 father_first_name, father_last_name,father_middle_name,
                 child_first_name, child_last_name,child_middle_name,age,doctor : doctor.Doctor):
        self.mother_first_name = mother_first_name
        self.mother_last_name = mother_last_name
        self.mother_middle_name = mother_middle_name
        self.father_first_name = father_first_name
        self.father_last_name = father_last_name
        self.father_middle_name = father_middle_name
        self.child_first_name = child_first_name
        self.child_last_name = child_last_name
        self.child_middle_name = child_middle_name
        self.age = age
        self.doctor = doctor
        doctor.add_Patient(self)
