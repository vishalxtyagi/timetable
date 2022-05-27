from pathlib import Path
import glob
import os

base_dir = Path(__file__).parent.resolve()

def get_all_csv_dataset():
    return glob.glob('D:\appathon\flask\dataset\*.csv',
            recursive=True
        )
    
datasets = get_all_csv_dataset()
print(datasets)