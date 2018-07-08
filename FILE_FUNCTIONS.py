def append_to_file(file,data):
	f=open(file,'a+')
	f.write(data)
	close(f)

def write_to_file(file,data_list):
	with open(file,"w") as f:
		for data in data_list:
			f.write(data)
		
def read_from_file(file):
	data_list = []
	with open(file) as f:
		for line in f:
			data_list.append(line)
	return data_list