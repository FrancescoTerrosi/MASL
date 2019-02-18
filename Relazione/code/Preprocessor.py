import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz


filename="kddcup10percent"
filenameExtended="kddcup"
refinedFilename="numericalKddcup10percent"
refinedFilenameExtended="numericalKddcup"

features = [
'duration',
'protocol_type',
'service',
'flag',
'src_bytes',
'dst_bytes',
'land',
'wrong_fragment',
'urgent',
'hot',
'num_failed_logins',
'logged_in',
'num_compromised',
'root_shell',
'su_attempted',
'num_root',
'num_file_creations',
'num_shells',
'num_access_files',
'num_outbound_cmds',
'is_host_login',
'is_guest_login',
'count',
'srv_count',
'serror_rate',
'srv_serror_rate',
'rerror_rate',
'srv_rerror_rate',
'same_srv_rate',
'diff_srv_rate',
'srv_diff_host_rate',
'dst_host_count',
'dst_host_srv_count',
'dst_host_same_srv_rate',
'dst_host_diff_srv_rate',
'dst_host_same_src_port_rate',
'dst_host_srv_diff_host_rate',
'dst_host_serror_rate',
'dst_host_srv_serror_rate',
'dst_host_rerror_rate',
'dst_host_srv_rerror_rate',
'behaviour'
]


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

def populateData(filename,count,replace=""):		# Costruisce tabella per ogni soggetto con i valori delle variabili
	dataset = open(filename)
	data = []
	for i in range(0,count-1):
		currentLine = dataset.readline()
		currentLine = currentLine.replace(replace,"")
#		print(currentLine)
		currentLine = currentLine.split(",")
		temp = []
		for x in currentLine:
			temp.append(x)
		data.append(temp)
	return data

def writeMappingsToFile(protocolNumerical,serviceNumerical,flagNumerical):

	numericalRepresentationFile = open("numericalMapping", "w+")

	numericalRepresentationFile.write("Protocols:\n")
	for j in range(0,len(protocolNumerical)-1):
		numericalRepresentationFile.write("{} = {}, ".format(protocolNumerical[j],j)),

	numericalRepresentationFile.write("{} = {}\n".format(protocolNumerical[len(protocolNumerical)-1],j+1))
	
	numericalRepresentationFile.write("Services:\n")
	for j in range(0,len(serviceNumerical)-1):
		numericalRepresentationFile.write("{} = {}, ".format(serviceNumerical[j],j)),

	numericalRepresentationFile.write("{} = {}\n".format(serviceNumerical[len(serviceNumerical)-1],j+1))
	
	numericalRepresentationFile.write("Flags:\n")
	for j in range(0,len(flagNumerical)-1):
		numericalRepresentationFile.write("{} = {}, ".format(flagNumerical[j],j)),

	numericalRepresentationFile.write("{} = {}\n".format(flagNumerical[len(flagNumerical)-1],j+1))


def writeToFile(filename,data):

	numericalKddcup = open(filename, "w+")

	for i in range(0, len(data)):
		for j in range(0,len(data[i])-1):
			numericalKddcup.write("{}, ".format(data[i][j]))
		numericalKddcup.write("{}\n".format(data[i][len(data[i])-1]))

def principalComponentAnalysis(filename,components):
	namesy = []
	columnsy = []

	for i in range(0,20):
		columnsy.append(i)

	for i in range(1,42):
		namesy.append('V{}'.format(i))

	namesy.append('target')

#	behaviours = []
#	index = []

#	for i in range(0, len(filename)):
#		behaviours.append(filename[i][-1])
#		del filename[i][-1]
#		index.append(i)

#	

	df = pd.read_csv(filename, names=namesy)

#	df1 = pd.read_csv("preprocessedKddcup", names=namesy)

	del namesy[-1]

	# Separating out the features
	x = df.loc[:, namesy].values
#	x1 = df1.loc[:, namesy].values

	# Separating out the target
	y = df.loc[:,['target']].values


	scaler = StandardScaler()

	scaler.fit(x)

	# Standardizing the features
	x = scaler.transform(x)

	pca = PCA(.95)

	pca.fit(x)

	principalComponents = pca.transform(x)

#	print("{}".format(principalComponents))

	principalDf = pd.DataFrame(data = principalComponents)

	finalDf = pd.concat([principalDf, df[['target']]], axis = 1)

	print("{}".format(finalDf))

	featureSelect = pd.DataFrame(pca.components_)
	
	matrix = featureSelect.values

	featuresIndex = []

	for i in range(0,len(matrix)):
		max = -1
		index = -1
		for j in range(0,len(matrix[i])):
			if abs(matrix[i][j]) > max:
				max = abs(matrix[i][j])
				index = j
		featuresIndex.append(index)

	print("{}".format(featuresIndex))

	result = pd.DataFrame(data=x)

	finalDf.to_csv("train_set_principalComponents", sep='\t', encoding='utf-8')

	return(featuresIndex,pd.concat([result, df[['target']]], axis=1))


#count = getDatasetSize(filenameExtended)
#count -= 2
#data = populateData(filenameExtended,count,".\n")



#protocolNumerical = []
#serviceNumerical = []
#flagNumerical = []

#for i in range(0, len(data)):
#	if (data[i][1] not in protocolNumerical):
#		protocolNumerical.append(data[i][1])

#	if (data[i][2] not in serviceNumerical):
#		serviceNumerical.append(data[i][2])

#	if (data[i][3] not in flagNumerical):
#		flagNumerical.append(data[i][3])
#	
#for i in range(0,len(data)):
#	for j in range(0,len(protocolNumerical)):
#		if (data[i][1] == protocolNumerical[j]):
#			data[i][1] = float(j)

#	for j in range(0,len(serviceNumerical)):
#		if (data[i][2] == serviceNumerical[j]):
#			data[i][2] = float(j)
#	

#	for j in range(0,len(flagNumerical)):
#		if (data[i][3] == flagNumerical[j]):
#			data[i][3] = float(j)

###	CONTINUARE DA QUI: DEVO CONVERTIRE TUTTO IN NUMERI IN VIRGOLA PER STANDARDIZZARE

##for i in range(0,len(data[0])-1):
##	if (data[0][i].find(".") == -1):
##		for j in range(0,len(data)):
##			data[j][i] = float(data[j][i])

#writeToFile("preprocessedKddcupExtended", data)

result = principalComponentAnalysis("preprocessedKddcup",5)

#featuresIndex = result[0]
#dataFrame = result.values
#featuresIndex.sort()


#f = open("standardizedKddcupExtended", "w+")
#for i in range(0,len(features)-1):
#	f.write("{}\t".format(features[i]))
#f.write("{}\n".format(features[len(features)-1]))

#for i in range(0,len(dataFrame)):
#	for j in range(0,len(dataFrame[0])-1):
#		f.write("{}\t".format(dataFrame[i][j]))
#	f.write("{}\n".format(dataFrame[i][len(dataFrame[0])-1]))

##for j in range(0, len(data[0])-1):
##	min = 99999
##	max = -1
##	for i in range(0,len(data)):
##		if float(data[i][j]) < min:
##			min = float(data[i][j])
##		elif float(data[i][j]) > max:
##			max = float(data[i][j])
##	if max > 0:
##		for i in range(0,len(data)):
##			data[i][j] = (float(data[i][j])-min)/(max-min)

