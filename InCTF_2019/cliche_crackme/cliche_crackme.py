with open('cliche_crackme','rb') as rb:
	rb.seek(0x1040)
	data = rb.read(666*4)
	for i in range(0x21,0x80):
		try:
			rev = chr(i)
			for j in range(0,len(data),4):
				rev += chr(data[j]-ord(rev[0+(len(rev)-1)//37]))
		except:
			a5,chk = rev[:37],0
			for j in range(len(a5)): chk += ord(a5[j])
			if chk == 3504: print('input :',a5)