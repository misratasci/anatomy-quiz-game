import os.path, random, openpyxl

class MQuestion():
    def __init__(self, muscle, ozellik):
            self.muscle = muscle
            self.ozellik = ozellik
            if self.ozellik == "location":
                self.answer = muscle.location
            if self.ozellik == "insertion":
                self.answer = muscle.insertion
            if self.ozellik == "origin":
                self.answer = muscle.origin
            if self.ozellik == "function":
                self.answer = muscle.function
            if self.ozellik == "nerve":
                self.answer = muscle.nerve

class Question():
    def __init__(self, quality_asked):
        self.quality_asked = quality_asked
        self.text = f"{self.structure.name} {self.quality_asked}?"

class Muscle(Question):
    def __init__(self, name, location, origin, insertion, nerve, function):
        self.name = name
        self.location = location
        self.origin = origin
        self.insertion = insertion
        self.nerve = nerve
        self.function = function
        if os.path.exists(f"muscles\{self.name}.jpg"):
            self.imgpath = f"muscles\{self.name}.jpg"
        else:
            self.imgpath = f"muscles\{self.name}.png"
    def get_info_text(self):
        texts = []
        texts.append(f"{self.name}")
        texts.append(f"O: {self.origin}")
        texts.append(f"I: {self.insertion}")
        texts.append(f"N: {self.nerve}")
        texts.append(f"F: {self.function}")
        return texts

def read_xl_data(file):
    wb = openpyxl.load_workbook(file)
    ws = wb.active
    data = []
    for row in ws.iter_rows(values_only=True):
        data.append(row)
    return data
"""
def get_column_list(file, columntitle):
    wb = openpyxl.load_workbook(file)
    ws = wb.active
    column_titles = ws[1]
    for title in column_titles:
        if columntitle == title.value:
            column_list = ws[title].values
            column_list.pop(0)
    return column_list
"""
def get_rand_list_member(list):
    if len(list) == 0:
        return []
    i = random.randint(0,len(list)-1)
    return list[i]