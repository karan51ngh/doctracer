import os
import time
import getopt
import sys


def checkFolder(x):
    if os.path.isfile(x):
        return 'FILE'
    else:
        return 'DIRECTORY'


def func(path, tar, d0, c0):
    # print(path)
    dir_list = os.listdir(path)
    dir_list = sorted(dir_list)
    if d0 == 1:
        time.sleep(0.01)
        print('	' + path + ' :')
        # print(f'Files/Directories in the Current Directory:\n {dir_list}')
        print(f'Files/Directories in the Current Directory:')
        if dir_list == []:
            print('**NONE**')
        else:
            for i in range(0, len(dir_list)):
                type = checkFolder(path+'/'+dir_list[i])
                print(f'{dir_list[i]}  type: {type}')
        print('')
    for i in dir_list:
        pathx = path
        pathx = pathx+'/'+i
        if os.path.isdir(pathx):
            func(pathx, tar, d0, c0)
        if os.path.isfile(pathx):
            if i == tar:
                print("FOUND!")
                print("location:"+pathx)
                if c0 == 1:
                    print("")
                    os.system('cat '+pathx)
                    print("")
                print("")
                exit()
            else:
                continue
