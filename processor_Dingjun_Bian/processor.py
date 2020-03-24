
def processor(time,pulse,blood_pressure,blood_oxygen):
	if pulse>100 or pulse<60:
		alert("pulse",pulse)
	if blood_pressure>120 or blood_pressure<80:
		alert("blood_pressure",blood_pressure)
	if blood_oxygen<75 or blood_oxygen>100:
		alert("blood_oxygen",blood_oxygen)
	if blood_oxygen<=0 or blood_oxygen<=0 or pulse<=0:
		print("sytem error!")
	storage(time,pulse,blood_oxygen,blood_pressure)
	return

def alert(alertType,Value):
	print("Warning your ",alertType,"is:",Value,"!\nWhich is not in the noraml range!")
	return

def storage(time,pulse,blood_pressure,blood_oxygen):  
	pass



if __name__ == '__main__':
	processor("10:30",87,96,87)
	processor("10:45",87,126,87)

