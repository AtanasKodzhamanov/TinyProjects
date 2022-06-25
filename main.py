import os


def GetFileSizes(path, numfiles):
    dict = {}
    for folderName, subFolders, fileNames in os.walk(path):
        # print(folderName)
        # print(fileNames)
        for file in fileNames:
            # print(file)
            fullname = folderName + "\\" + file
            size = int(os.path.getsize(fullname) / (1024 * 1024))
            dict[fullname] = size
            # print(f"{folderName}\\{file}: " + str(size))

    dict2 = {key: value for key, value in sorted(dict.items(), key=lambda item: item[1])}
    a = list(dict2.items())
    for i in range(-numfiles, 0):
        print(a[i])


GetFileSizes('D:\\', 200)
