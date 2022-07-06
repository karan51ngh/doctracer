import os
import time
import getopt,sys


def func(path,tar,d0,c0):
	#print(path)
	dir_list=os.listdir(path)
	dir_list=sorted(dir_list)
	if d0==1:
		time.sleep(0.15)
		print('	' + path + ' :')
		print(dir_list)
		print('')
	for i in dir_list:
		pathx=path
		pathx=pathx+'/'+i
		if os.path.isdir(pathx):
			func(pathx,tar,d0,c0)
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
