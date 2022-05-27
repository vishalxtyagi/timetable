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
            schedules[teacher_name] = pd.read_csv(file).to_dict('records')
        return schedules
            
    def get_all_teachers(self):
        all_teachers = [self.get_file_name_without_ext(file) for file in self.dataset_files]
        return all_teachers
    

class Adjust:
    
    def __init__(self) -> None:
        schedule = Schedule()
        self.teaches_schedule = schedule.get_all_teachers_schedule()
        
    def adjust(self, lecture):
        print(self.teaches_schedule)
    
    
    # def first_preference(slef):
    #     for i in teachers:
    #     count = 0
    #     if i[ab_lect] != 1 and i[ab_lect-1] != 1 and i[ab_lect+1] != 1:             # looks for the possible substitutes
    #         possible_sub.append(i[0])
    #         for j in i:                 # counts the total number of free periods
    #             if j == 0:
    #                 count += 1
    #         no_class.append(count)
    
    # def second_preference(slef):
    #     if possible_sub == []:
    #     for i in teachers:
    #         count = 0
    #         if i[ab_lect] == 0:
    #             possible_sub.append(i[0])
    #             for j in i:
    #                 if j == 0:
    #                     count += 1
    #             no_class.append(count)
    
    # def get_recommendations(self):
    #     suited_teacher = max(self.no_class)  # gives the teacher with the most number of free time
    #     for i in range(len(no_class)):
    #         if no_class[i] == suited_teacher:
    #             print(possible_sub[i])  # prints the teacher to that index