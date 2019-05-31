from data import Data

def main():
	print('Running...')
	data = Data('./fruits-360/Training/Banana')
	# data.genText('train.txt', './fruits-360/Training/')
	# data.genText('test.txt', './fruits-360/Test/')
	data.genInfo('./fruits-360/Training/')
	data.genInfo('./fruits-360/Test/')

if __name__=="__main__":
	main()
