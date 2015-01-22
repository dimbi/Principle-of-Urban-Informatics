# download assignment 3 data files using
import urllib

# download input and output files for problems 1-8
fileNamePrefix = "sample_data_problem_"

filePath = "http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/"
inputFilePrefix = "sample_data_problem_"
outputFilePrefix = "sample_output_problem_"


for x in range(1, 9):
	open('problem%s' %x + '.py', 'w+')
	if x != 3:
		inputFileName = inputFilePrefix + str(x) + ".txt"
		inputFileURL = filePath + inputFileName

		outputFileName = outputFilePrefix + str(x) + ".txt"
		outputFileURL = filePath + outputFileName

		testfile = urllib.URLopener()
		testfile.retrieve(inputFileURL, inputFileName)
		testfile = urllib.URLopener()
		testfile.retrieve(outputFileURL, outputFileName)
	if x == 3:
		for i in range(1,3):
			inputFileName = inputFilePrefix + str(x) + '_' + str(i) + ".txt"
			inputFileURL = filePath + inputFileName

			outputFileName = outputFilePrefix + str(x) + ".txt"
			outputFileURL = filePath + outputFileName

			testfile = urllib.URLopener()
			testfile.retrieve(inputFileURL, inputFileName)
			testfile = urllib.URLopener()
			testfile.retrieve(outputFileURL, outputFileName)
