import os
from openpyxl import Workbook



def categorize_files_by_type(folder_path):
    if not os.path.exists(folder_path):
        raise ValueError("Folder does not exist")
    if not os.path.isdir(folder_path):
        raise ValueError("Not a directory")

    res = {}

    def scan_dir(dir_name):
        try:
            with os.scandir(dir_name) as it:
                for entry in it:
                    if entry.is_file():
                        if os.path.getsize(entry.path) > 1024:
                            ext = os.path.splitext(entry.name)[1]
                            if ext not in res:
                                res[ext] = []
                            res[ext].append(entry.path)
                        else:
                            pass

                    elif entry.is_dir():
                        scan_dir(entry.path)  # Recursion
        except PermissionError:
            print(f"Permission denied: {dir_name}")

    scan_dir(folder_path)
    return res


result = categorize_files_by_type(r"C:\Users\77475\Desktop\job\python\TestTask_os.walk\paths")
print(result)

wb = Workbook()
ws = wb.active

headers = ['Extension', 'path']
ws.append(headers)

for k, v in result.items():

    for v1 in v:
        print(v1)
        ws.append([k] + [v1])


wb.save('employees.xlsx')
