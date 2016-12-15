import os,shutil

#The code is used to find any files like '.txt','.jpg',and print these files	



def findFile(yourpath):   #input a origin path
	try:
		filelist = os.listdir(yourpath)
		
	except:
		print('one')
		filelist = []     #without this the function will fail when error happened.
		pass

	for i in filelist: 
		print("2222")
										#Read everything in this path
		d=i.find('txt')
		print(d)
        		
		
		if d != -1:
			truepath = yourpath+"\\"+i
			try:
				shutil.move(truepath,'D:\\test\\test1')      #the destination path
			
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
		
			
			

			
path ='E:\\迅雷下载'     #the target main path



findFile(path)
