from patient import Patient

class ChildrenList:
    def __init__(self, list):
        self.children = list

    def addChild(self, ctr : Patient):
        self.children.append(ctr)

    def delCountry(self, ctr : Patient):
        self.children.remove(ctr)

    def create_csv_data(self):
        data = []
        for child in self.children:
            data.append({
                'child_first_name': child.child_first_name,
                'child_last_name': child.child_last_name,
                'child_middle_name': child.child_middle_name,
                'mother_first_name': child.mother_first_name,
                'mother_last_name': child.mother_last_name,
                'mother_middle_name': child.mother_middle_name,
                'father_first_name': child.father_first_name,
                'father_last_name': child.father_last_name,
                'father_middle_name': child.father_middle_name,
                'doctor_first_name': child.doctor.doctor_first_name,
                'doctor_last_name': child.doctor.doctor_last_name,
                'doctor_middle_name': child.doctor.doctor_middle_name,
                'age': child.age
            })
        return data