import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#######################################################################################################################
# Get a list of all the images (all the directories)
#######################################################################################################################

data_folder = os.path.join(os.getcwd(), '..', 'chapter_14', 'data_flat')
images = os.listdir(data_folder)
print('Found {} images'.format(images))

#######################################################################################################################
# Interactive labelling
#######################################################################################################################

""" Show an image and allow the user to specify 'y' or 'n' for the class.
Save the results in a a text file with the file names.
"""

classifications = []
for i, image in enumerate(images):
    image_full_path = os.path.join(data_folder, image)
    plt.imshow(mpimg.imread(image_full_path))
    plt.draw()
    plt.pause(1)
    plt.close()

    input_valid = False
    while not input_valid:
        classification = input('Image {}/{}\nPlease classify image as \'y\' or \'n\':\n'.format(i, len(images)))
        if classification not in ['y', 'n']:
            print('Input not valid')
        else:
            input_valid = True
            classifications.append(classification)

label_filepath = os.path.join(data_folder, '..', 'image_labels.txt')
label_file = open(label_filepath, "w")

for image, classification in zip(images, classifications):
    label_file.write(image + ',' + classification + '\n')

label_file.close()
