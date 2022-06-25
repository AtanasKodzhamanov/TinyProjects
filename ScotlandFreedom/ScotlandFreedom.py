from math import fabs
import os
import pandas as pd
import pathlib


def GetFileSizes(path, output, minsize, top):
    paths = []
    files = []
    sizes = []
    extensions = []

    # Parse root folder and extract the relevant information
    for folderName, subFolders, fileNames in os.walk(path):
        # print(folderName)
        # print(fileNames)
        for file in fileNames:
            # print(file)
            fullname = folderName + "\\" + file
            size = int(os.path.getsize(fullname) / (1024 * 1024))
            extension = pathlib.Path(file).suffix.lower()
            # print(f"{folderName}\\{file}: " + str(size))
            if(size >= minsize):
                paths.append(folderName + "\\" + file)
                files.append(file)
                extensions.append(extension)
                sizes.append(int(os.path.getsize(fullname) / (1024 * 1024)))

    # Put results in a dataframe
    dict = {"File Path": paths, 
            "File Name": files,
            "File Extension": extensions, 
            "Size (MB)": sizes}
    if(type(top) == "numeric"):
        df = pd.DataFrame(data=dict).sort_values(
            by="Size (MB)", ascending=False).head(top)
    else:
        df = pd.DataFrame(data=dict).sort_values(
            by="Size (MB)", ascending=False)

    # Additional analysis
    df_ext = df.groupby(by='File Extension', sort=False)["Size (MB)"].agg(['sum', 'count', 'mean'])
    df_ext['mean'] = df_ext['mean'].map(lambda mean: int(mean))
    df_ext['sum'] = df_ext['sum'].map(lambda sum: sum/1000)
    df_ext.rename(columns={'sum': 'Sum (GB)', 'count': 'Count','mean': 'Mean (MB)'}, inplace=True)

    # ScotlandFreedomReport
    output_path = output + "ScotlandFreedomReport.xlsx"
    df.to_excel(output_path, sheet_name="Kill List", index=False)
    #df_ext.to_excel(output_path, sheet_name="Analysis")


# Folder tree to be parsed | Location of the output report | Minimum size of file to be shown (MB) | Top x results to be shown
GetFileSizes(path="D:\\Torrents", output="D:\\", minsize=1000, top=100)

# To get all of the files in the root folder
# GetFileSizes(path="D:\\", output="D:\\", minsize=0, top="All")


#To add:
# Fix excel overwriting bug
# List all folders: Folder name, folder depth - total size (separate sheet)