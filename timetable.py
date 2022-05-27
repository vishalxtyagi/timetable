from pathlib import Path
import pandas as pd
import os
import glob

class Schedule:
    
    def __init__(self) -> None:
        self.base_dir = Path(__file__).parent.resolve()
        self.dataset_files = glob.glob(
            os.path.join(self.base_dir, 'dataset', '*.csv'),
            recursive=True
        )
        
    def get_file_name_without_ext(self, filepath):
        return "".join(os.path.basename(filepath).split('.')[:-1])
    
    def get_all_teachers_schedule(self):
        schedules = dict()
        for file in self.dataset_files:
            teacher_name = self.get_file_name_without_ext(file)
            schedules[teacher_name] = pd.read_csv(file).to_dict('list')
        return schedules
            
    def get_all_teachers(self):
        all_teachers = [self.get_file_name_without_ext(file) for file in self.dataset_files]
        return all_teachers
    

class Adjuster:
    
    def __init__(self) -> None:
        schedule = Schedule()
        self.teachers_schedule = schedule.get_all_teachers_schedule()
        self.possible_substitutes = []
        self.no_class = []
        
    def adjust(self, teacher_name, lecture, day):
        self.first_preference(lecture)
        self.second_preference(lecture)
        recommendations = self.get_recommendations()
        return recommendations
    
    def first_preference(self, lecture):
        for ts in self.teachers_schedule:
            count = 0
            if ts[lecture] != 1 and ts[lecture-1] != 1 and ts[lecture+1] != 1:  # looks for the possible substitutes
                self.possible_substitutes.append(ts[0])
                for j in ts:                 # counts the total number of free periods
                    if j == 0:
                        count += 1
                self.no_class.append(count)
    
    def second_preference(self, lecture):
        if self.possible_substitutes == []:
            for ts in self.teachers_schedule:
                count = 0
                if ts[lecture] == 0:
                    self.possible_substitutes.append(ts[0])
                    for j in ts:
                        if j == 0:
                            count += 1
                    self.no_class.append(count)
    
    def get_recommendations(self):
        recommended = []
        suited_teacher = max(self.no_class)  # gives the teacher with the most number of free time
        for i in range(len(self.no_class)):
            if self.no_class[i] == suited_teacher:
                recommended.append(self.possible_substitutes[i])  # appends the teacher to that index
        return recommended