filename="kddcup10percent"

def _initIndexes_(filename):			# Estrae le stringhe delle variabili considerate (definite in indexDict)
	dataset = open(filename)
	currentLine = dataset.readline()
	currentLine = currentLine.replace("\"", "")
	keys = currentLine.split()
	dataset.close()
	return keys

def getDatasetSize(filename):		# Calcola le dimensioni del dataset per flessibilita
	filez = open(filename)
	count = 0
	for lines in filez: count += 1
	return count

def populateData(filename,count):		# Costruisce tabella per ogni soggetto con i valori delle variabili
	dataset = open(filename)
	dataset.readline()
	data = []
	for i in range(0,count-1):
		currentLine = dataset.readline()
		currentLine = currentLine.replace(".\n","")
#		print(currentLine)
		currentLine = currentLine.split(",")
		temp = []
		for x in currentLine:
			temp.append(x)
		data.append(temp)
	return data

def writeMappingsToFile(protocolNumerical,serviceNumerical,flagNumerical,behaviourNumerical):

	numericalRepresentationFile = open("numericalMapping", "w+")

	for j in range(0,len(protocolNumerical)-1):
		numericalRepresentationFile.write("{} = {}, ".format(protocolNumerical[j],j)),

	numericalRepresentationFile.write("{}\n".format(protocolNumerical[len(protocolNumerical)-1]))
	
	for j in range(0,len(serviceNumerical)):
		numericalRepresentationFile.write("{} = {}, ".format(serviceNumerical[j],j)),

	numericalRepresentationFile.write("{}\n".format(protocolNumerical[len(serviceNumerical)-1]))
	
	for j in range(0,len(flagNumerical)):
		numericalRepresentationFile.write("{} = {}, ".format(flagNumerical[j],j)),

	numericalRepresentationFile.write("{}\n".format(flagNumerical[len(flagNumerical)-1]))

	for j in range(0,len(behaviourNumerical)):
		numericalRepresentationFile.write("{} = {}, ".format(behaviourNumerical[j],j)),

	numericalRepresentationFile.write("{}".format(protocolNumerical[len(protocolNumerical)-1]))


def writeToRefinedFile(data):

	numericalKddcup = open("numericalKddcup", "w+")

	for i in range(0, len(data)):
		for j in range(0,len(data[i])-1):
			numericalKddcup.write("{}, ".format(data[i][j]))
		numericalKddcup.write("{}\n".format(data[i][len(data[i])-1]))


count = getDatasetSize(filename)
data = populateData(filename,count)
count -= 2

protocolNumerical = []
serviceNumerical = []
flagNumerical = []
behaviourNumerical = []

for i in range(0, count):
	if (data[i][1] not in protocolNumerical):
		protocolNumerical.append(data[i][1])

	if (data[i][2] not in serviceNumerical):
		serviceNumerical.append(data[i][2])

	if (data[i][3] not in flagNumerical):
		flagNumerical.append(data[i][3])
	
	if (data[i][len(data[i])-1] not in behaviourNumerical):
		behaviourNumerical.append(data[i][len(data[i])-1])


for i in range(0,count):
	for j in range(0,len(protocolNumerical)):
		if (data[i][1] == protocolNumerical[j]):
			data[i][1] = str(j)

	for j in range(0,len(serviceNumerical)):
		if (data[i][2] == serviceNumerical[j]):
			data[i][2] = str(j)
	

	for j in range(0,len(flagNumerical)):
		if (data[i][3] == flagNumerical[j]):
			data[i][3] = str(j)
	

	for j in range(0,len(behaviourNumerical)):
		if (data[i][len(data[i])-1] == behaviourNumerical[j]):
			data[i][len(data[i])-1] = (j)


#	CONTINUARE DA QUI: DEVO CONVERTIRE TUTTO IN NUMERI IN VIRGOLA PER STANDARDIZZARE

for i in range(0,len(data[0])):
	if (data[0][i].find(".") != -1)

print("{}".format(data[0][0].find(".")))
print("{}".format(len(data[0])))

