import os,shutil

#The code is used to find any files like '.txt','.jpg',and print these files			

def findFile(yourpath):   #input a origin path
	
	filelist = os.listdir(yourpath)
	
	for i in filelist:                          #Read everything in this path
		d=i.find('txt')                         #In this case I want to find '.txt'files, you can change it to 'jpg',etc
		if d != -1 : 
			truepath = yourpath+"\\"+i
			shutil.copy(truepath,'D:\\test1')
			print(i)
	                                            #print needed files.
		path2 = yourpath +"\\" +i
	
		                                        #go into sub path
		                                        #print ('path2 is:' + path2)
		if os.path.isdir(path2):                #If the sub path is a dir, call the function again.
			                                    #print("I find a dir path!It's:")
			                                    #print(path2)
			findFile(path2)
		
			
path ='D:\\'


findFile(path)


