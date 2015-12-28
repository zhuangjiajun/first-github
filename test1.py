str = ''
path = 'test.log'
size = 10
handle =  open('test.log','r')
while True:
	tmp_str = handle.read(size)
	if '' == tmp_str:
		break
	str += tmp_str
print str

