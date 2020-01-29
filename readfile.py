import os
import fnmatch

def main():
    with os.scandir('schemas/') as entries:
        for entry in entries:
            foundfiles=findschema(entry.name)
            for item in foundfiles:
                nombreschema=entry.name
                print("Esquema --> {}".format(entry.name))
                with open(item) as fp:
                    line = fp.readline()
                    print("Contenido --> {}".format(item))
                    while line:
                        print("Line: {}".format(line))
                        line = fp.readline()

def findschema(name):
    schemaname = name[:-4] + ".txt"
    matches=[]
    for root, dirs, files in os.walk('data/'):
        for filename in fnmatch.filter(files, schemaname):
            if (os.path.join(root,filename)):
                matches.append(os.path.join(root,filename))
    return matches



if __name__ == '__main__':
    main()