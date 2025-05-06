import os
import pandas as pd
from django.conf import settings

class FileCache:
    def __init__(self, path):
        self.path = path
        self.filedata = {}
        self.last_modified_times = {}
    
    def read_file(self, file_path, file_name):
        current_modified_time = os.path.getmtime(file_path)
        if file_name in self.last_modified_times:
            last_modified_time = self.last_modified_times[file_name]
        else:
            last_modified_time = 0
        
        if current_modified_time > last_modified_time:
            filepath = os.path.join(settings.MEDIA_ROOT, file_name )
            if filepath.find("xlsx") != -1:
                df = pd.read_excel(filepath, sheet_name=None)
                self.filedata[file_name] = df
            else:
                df = pd.read_csv(filepath)
                self.filedata[file_name] = df
            self.last_modified_times[file_name] = current_modified_time
        else:
            return self.filedata[file_name]
        
    def read_from_directory(self):
        files = os.listdir(self.path)

        for file in files:
            path = os.path.join(self.path, file)
            if os.path.isfile(path):
                self.read_file(path, file)

    def construct_prompt(self,question):
        prompt = f"Given the following information:\n\n"
        for file, file_data in self.filedata.items():
            prompt += f"File: {file}\n"
            if isinstance(file_data, dict):  # Excel file with multiple sheets
                for sheet, df in file_data.items():
                    prompt += f"Sheet: {sheet}\n"
                    prompt += df.to_string(index=False) + "\n\n"
            else:  # CSV file
                prompt += file_data.to_string(index=False) + "\n\n"
        prompt += f"Answer the following question: {question}. Don't give any technical information about the data to user"
        print(prompt)
        return prompt

            
            
