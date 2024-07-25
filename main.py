import os


def categorize_files_by_type(folder_path):

    res = {}

    def scan_dir(dir_name):
        with os.scandir(dir_name) as it:
            for entry in it:

                if entry.is_file():
                    ext = os.path.splitext(entry.name)[1]
                    if ext not in res:
                        res[ext] = []
                    res[ext].append(entry.path)
                elif entry.is_dir():
                    scan_dir(entry.path)

    scan_dir(folder_path)
    return res


result = categorize_files_by_type(r"C:\Users\77475\Desktop\TestTask\paths")
print(result)
