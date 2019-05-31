from PIL import Image
import glob

class Data:

	def __init__(self, datasetName):
		self.classes = ['Apple', 'Lemon', 'Orange', 'Pear']
		self.folders = {'Apple': ['Crimson Snow', 'Golden 1', 'Golden 2', 'Golden 3', 'Golden-Red', 'Granny Smith', 'Pink Lady', 'Red 1', 'Red 2', 'Red 3', 'Red Delicious'], 'Lemon':['', 'Meyer'], 'Orange': [''], 'Pear': ['', 'Abate', 'Kaiser', 'Monster', 'Red', 'Williams']}

		self.dataset = './fruits-360/Training/'
		# for filename in glob.glob(datasetName + '/*.jpg'):
		# 	self.dataset.append(Image.open(filename))

	def show(self):
		for file in self.dataset:
			print file

	def showClasses(self):
		print('\n------------CLASSES------------')
		for c in self.classes:
			print(c + ':')
			for variety in self.folders[c]:
				if len(variety) > 0:
					folderName = c + ' ' + variety
				else:
					folderName = c
				print('\t' + folderName)

	def genText(self, outputFile, dataPath):
		file = open(outputFile, 'a')
		for c in self.classes:
			for variety in self.folders[c]:
				if len(variety) > 0:
					folderName = c + ' ' + variety
				else:
					folderName = c
				for filePath in glob.glob(dataPath + folderName + '/*.jpg'):
					file.write(filePath + '\n')
		file.close()

	def genInfo(self, dataPath):
		for i, c in enumerate(self.classes):
			line = str(i) + ' 0.500000 0.500000 0.999000 0.999000'
			for variety in self.folders[c]:
				if len(variety) > 0:
					folderName = c + ' ' + variety
				else:
					folderName = c
				for filePath in glob.glob(dataPath + folderName + '/*.jpg'):
					filename = filePath.split('/')[-1].split('.')[0]
					newFilename = filename + '.txt'
					with open(dataPath + folderName + '/' + newFilename, 'w') as file:
						file.write(line + '\n')
					file.close()


