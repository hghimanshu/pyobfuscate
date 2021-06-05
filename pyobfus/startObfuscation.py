import os
import subprocess


class obfus:

    def __init__(self, inputPath, outputPath, package, file):
        self.inputPath = inputPath
        self.outPath = os.path.join(outputPath, "pyobfus")
        self.__createFolder(self.outPath)
        self.pack = package
        self.filePath = file
    
    def __createFolder(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as e:
            print(str(e))

    def initializeConfig(self):
        init_comd = ["cd", self.outPath, "&&", "pyarmor", "init", "--src", self.inputPath, "--entry", self.filePath, self.pack]
        init_res = subprocess.call(init_comd)
        print("Response after Initialization {}!!".format(init_res))

