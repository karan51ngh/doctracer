import os
import streamlit as st

li=[]

def func(path,tar, print=print):
	
	dir_list=os.listdir(path)
	for i in dir_list:
		pathx=path
		pathx=pathx+'/'+i
		if os.path.isdir(pathx):
			func(pathx,tar,print=print)
		if os.path.isfile(pathx):
			if i == tar:
				print("FOUND!")
				print("location:"+pathx)
				li.append(pathx)
			else:
				continue

	

#path=st.text_input("enter the location of the root folder",value='/home/osboxes/defenceForces/army/1.officers')
#tar=st.text_input("enter the name of the file",value='ltKaran.txt')
path=st.text_input("enter the location of the root folder")
tar=st.text_input("enter the name of the file")


#flag = func(path,tar,print=st.write)

func(path,tar,print=st.write)

if not li:
	st.warning("File not found!")
