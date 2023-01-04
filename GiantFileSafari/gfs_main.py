from math import fabs
import os
import pandas as pd
import pathlib
from xlsxwriter.utility import xl_rowcol_to_cell
from gfs_report import CreateExcelReport


def GetFileSizes(path, output, minsize, top):
    paths = []
    files = []
    sizes = []
    extensions = []
    folders = []
    folderSizes = []
    folderDepth = []

    # Parse root folder and extract the relevant information about files and folders
    for folderName, subFolders, fileNames in os.walk(path):
        for file in fileNames:
            fullname = folderName + "\\" + file
            size = round(os.path.getsize(fullname) / (1024 * 1024*1024), 1)
            extension = pathlib.Path(file).suffix.lower()
            if (size >= minsize):
                paths.append(folderName + "\\" + file)
                files.append(file)
                extensions.append(extension)
                sizes.append(size)

    # Put results in a dataframe
    dict = {"File Path": paths,
            "File Name": files,
            "File Extension": extensions,
            "Size (GB)": sizes}
    if (type(top) == "numeric"):
        df = pd.DataFrame(data=dict).sort_values(
            by="Size (GB)", ascending=False).head(top)
    else:
        df = pd.DataFrame(data=dict).sort_values(
            by="Size (GB)", ascending=False)

    # Additional analysis
    df_ext = df.groupby(by='File Extension', sort=False)[
        "Size (GB)"].agg(['sum', 'count', 'mean'])
    df_ext['mean'] = df_ext['mean'].map(lambda mean: int(mean))
    # df_ext['sum'] = df_ext['sum'].map(lambda sum: sum/1024)
    df_ext.rename(columns={'sum': 'Sum (GB)',
                  'count': 'Count', 'mean': 'Mean (GB)'}, inplace=True)

    # By folders - output total size of files in the folder and folder depth (number of subfolders)
    for folderName, subFolders, fileNames in os.walk(path):
        folderSize = 0
        for file in fileNames:
            fullname = folderName + "\\" + file
            size = round(os.path.getsize(fullname) / (1024 * 1024 * 1024), 1)
            folderSize += size
        if (folderSize >= minsize):
            folders.append(folderName)
            folderSizes.append(folderSize)
            folderDepth.append(folderName.count("\\"))

    dict = {"Folder Path": folders,
            "Folder Depth": folderDepth,
            "Folder Size (GB)": folderSizes}
    df_folders = pd.DataFrame(data=dict).sort_values(
        by="Folder Size (GB)", ascending=False)

    CreateExcelReport(output, df, df_ext, df_folders)


# Folder tree to be parsed | Location of the output report | Minimum size of file to be shown (GB) | Top x results to be shown
GetFileSizes(path="D:\\Torrents", output="D:\\", minsize=0.5, top=100)

# To get all of the files in the root folder
# GetFileSizes(path="D:\\", output="D:\\", minsize=0, top="All")
