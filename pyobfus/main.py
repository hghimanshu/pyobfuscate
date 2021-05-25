import os
import sys
from getArguments import getAllAgruments

class pyobfus(getAllAgruments):
    def __init__(self):
        super().__init__()
    

if __name__ == "__main__":

    obj = pyobfus()

    print("Input path is {} ".format(obj.inputPath))
    print("Output path is {} ".format(obj.outputPath))
    print("Package Name is {} ".format(obj.packageName))
    print("File path is {} ".format(obj.file))