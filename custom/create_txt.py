import glob, os

dataset_path = 'fruits/'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*/*/*.jpg")):
    print(pathAndFilename)
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print("Title",ext)

    if counter == index_test+1:
        counter = 1
        # file_test.write(dataset_path + "/" + title + '.jpg' + "\n")
        file_test.write(pathAndFilename + "\n")

    else:
        # file_train.write(dataset_path + "/" + title + '.jpg' + "\n")
        file_train.write(pathAndFilename + "\n")
        counter = counter + 1
