with open("status1.txt",'a') as f:
	for i in range(10):
		print(i,sep='\n', file=f)
		f.write("check\n")
	f.close()
print("status",f.closed)