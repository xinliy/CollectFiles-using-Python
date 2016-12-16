import os,shutil

#The code is used to find any files like '.txt','.jpg',and print these files



def findFile(yourpath):   #input a origin path
	try:
		filelist = os.listdir(yourpath)

	except:
		print('Cannot open the dir!')
		filelist = []     #without this the function will fail when error happened.
		pass

	for i in filelist:
		#print("2222")
										#Read everything in this path
		d=i.find('.avi')
		d1=i.find('.mp4')
		d3=i.find('.mkv')
		d2=i.find('.rmvb')



		#print(d)


		if d != -1 or d1 != -1 or d2 != -1 or d3 != -1:
			print("the target file is "+i)
			truepath = yourpath+"\\"+i
			try:
				shutil.move(truepath,'G:\\Videos')      #the destination path

			except:
				print('error!')
				pass
			print(i)
	                                            #print needed files.
		path2 = yourpath +"\\" +i
		                                        #go into sub path
		                                        #print ('path2 is:' + path2)
		if os.path.isdir(path2):                #If the sub path is a dir, call the function again.
			                                    #print("I find a dir path!It's:")
			                                    #print(path2)
			findFile(path2)





path ='G:\\'     #the target main path



findFile(path)
