import os


def main():
    if option == 'dirPath':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path
