import argparse
import sys


class getAllAgruments:
    def __init__(self) -> None:
        self.arguments = argparse.ArgumentParser(description="Code encrypter !!")
        self.args = self.__constructArgs()
        self.inputPath = self.args.inputFolder
        self.outputPath = self.args.outputFolder
        self.packageName = self.args.packageName
        self.file = self.args.filePath
        self.__validation()


    def __constructArgs(self):
        self.arguments.add_argument('-inputFolder',
                    required=True,
                    metavar='--input',
                    type=str,
                    help='/path/to/inputFolder/')
    
        self.arguments.add_argument('-outputFolder',
                    required=True,
                    metavar='--output',
                    type=str,
                    help='/path/to/outputFolder/')
        
        self.arguments.add_argument('-packageName',
                    metavar='--package',
                    type=str,
                    help='/path/to/package/',
                    default=None
                    )
        
        self.arguments.add_argument('-filePath',
                    metavar='--file',
                    type=str,
                    help='/path/to/file/',
                    default=None
                    )
        return self.arguments.parse_args()

    def __validation(self):
        if self.file is None and self.packageName is None:
            print("\n\n \t Atleast provide filename OR a package name to obfuscate !!")
            print("\n\n \t Exiting !!")
            sys.exit(0)
