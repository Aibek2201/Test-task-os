import os


def categorize_files_by_type(folder_path):
    res = {}


    for root, dirs, files in os.walk(folder_path):
        print(root, dirs, files)
        for file in files:
            file_extension = os.path.splitext(file)[1]
            full_path = os.path.join(root, file)

            if file_extension in res:
                res[file_extension].append(full_path)
            else:
                res[file_extension] = [full_path]

    return res



result = categorize_files_by_type(r"C:\Users\77475\Desktop\TestTask")
print(result)
