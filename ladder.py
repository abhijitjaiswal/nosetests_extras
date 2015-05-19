import os
import sys

def ladder(path):
        '''
        | Usage: This functions is a wrapper over Nosetest which would find
                 all the folders within a parent folder which contains test scripts
        | :param str path: Absolute Path of parent directory
        | :param list fin: Return the list of folders, which has with test scripts
        '''
        print path
        list1 = [os.path.join(path,name) for name in os.listdir(path) if os.path.isdir(os.path.join(path,name))]
        fin = []
        for l in list1:
            for name in os.listdir(l):
                if name.endswith(".py") and name.startswith("test"):
                    fin.append(l)
                    break
        for n in os.listdir(path):
            if n.endswith(".py") and n.startswith("test"):
                    fin.append(path)
                    break
        return fin
