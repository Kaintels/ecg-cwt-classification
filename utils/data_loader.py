import os, errno
from zipfile import ZipFile

path = "./data/ECG5000"

class FileLoader:
    # def __init__(self):
    #
    @staticmethod
    def unzip():
        try:
            if not (os.path.isdir(path)):
                os.makedirs(os.path.join(path))
                if os.path.exists(path):
                    data = ZipFile(path + ".zip")
                    data.extractall(path)
                    print("Unzip successfully.")
            else:
                raise OSError
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Failed to create directory!")



