from math import fabs
import os
import pandas as pd
import pathlib
from xlsxwriter.utility import xl_rowcol_to_cell

# Purpose: to find and list files that eat up your storage

def GetFileSizes(path, output, minsize, top):
    paths = []
    files = []
    sizes = []
    extensions = []
    folders =[]
    folderSizes = []
    folderDepth = []

    # Parse root folder and extract the relevant information
    for folderName, subFolders, fileNames in os.walk(path):
        # print(folderName)
        # print(fileNames)
        for file in fileNames:
            # print(file)
            fullname = folderName + "\\" + file
            size = round(os.path.getsize(fullname) / (1024 * 1024*1024),1)
            extension = pathlib.Path(file).suffix.lower()
            # print(f"{folderName}\\{file}: " + str(size))
            if(size >= minsize):
                paths.append(folderName + "\\" + file)
                files.append(file)
                extensions.append(extension)
                sizes.append(size)


    # Put results in a dataframe
    dict = {"File Path": paths, 
            "File Name": files,
            "File Extension": extensions, 
            "Size (GB)": sizes}
    if(type(top) == "numeric"):
        df = pd.DataFrame(data=dict).sort_values(
            by="Size (GB)", ascending=False).head(top)
    else:
        df = pd.DataFrame(data=dict).sort_values(
            by="Size (GB)", ascending=False)

    # Additional analysis
    df_ext = df.groupby(by='File Extension', sort=False)["Size (GB)"].agg(['sum', 'count', 'mean'])
    df_ext['mean'] = df_ext['mean'].map(lambda mean: int(mean))
    #df_ext['sum'] = df_ext['sum'].map(lambda sum: sum/1024)
    df_ext.rename(columns={'sum': 'Sum (GB)', 'count': 'Count','mean': 'Mean (GB)'}, inplace=True)

    # By folders (for any sneaky leakage caused by numerous small files)

    # ScotlandFreedomReport
    output_path = output + "ScotlandFreedomReport.xlsx"
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name="Kill List", index=False)
    df_ext.to_excel(writer, sheet_name="Analysis")
    writer.save()


# Folder tree to be parsed | Location of the output report | Minimum size of file to be shown (GB) | Top x results to be shown
GetFileSizes(path="D:\\Torrents", output="D:\\", minsize=0.5, top=100)

# To get all of the files in the root folder
# GetFileSizes(path="D:\\", output="D:\\", minsize=0, top="All")


#To add:
# List all folders: Folder name, folder depth - total size (separate sheet)
# Format excel output