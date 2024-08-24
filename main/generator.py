''' '''
import os
import csv
import json
import argparse
import cv2
import numpy as np
from colorama import init, Fore


#Initialize colorama
init()

#helper function
def write_to_csv(csv_path, w, h, class_path, image_list, index):
    #Using open(, , newline = '') will not insert extra null rows in csv file
    with open(csv_path, 'a', newline='') as file:
        writer = csv.writer(file)
        im_no = 1
        for image in image_list:
            if (image.endswith('.jpg') or image.endswith('.png'), image.endswith('.jpeg')):
                img = cv2.imread(os.path.join(class_path, image))
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                image_resized = cv2.resize(gray_image, (w, h), cv2.INTER_AREA)
                #Convert 2-D to 1-D array 
                image_resized_flatten = image_resized.reshape((w*h,))
                #Make it writable to CSV file
                image_resized_flatten = np.append(image_resized_flatten, np.array([index]))
                image_resized_flatten = np.asarray(image_resized_flatten)
                #Can be read and transformed into ndarray using
                # array = np.genfromtxt(CSV_FILE_NAME, delimiter=',')
            
                #Add label to the last of the each row
                
                #write array(row-vector) to csv row
                writer.writerow(image_resized_flatten)
                print(Fore.WHITE + f"[{im_no}]{image}" + Fore.GREEN + f"[OK]" + Fore.WHITE)
                im_no += 1





parser = argparse.ArgumentParser(description="Utility to create CSV dataset with multiclass data. \n Please use the following options")
parser.add_argument("--src", help="Source directory", required=True)
# parser.add_argument("--train", help="Enter train percent", type=int, required=True)
# parser.add_argument("--test", help="Enter test percent", type=int, required=True)
parser.add_argument("--w", help="Width of target image", type=int, required=False)
parser.add_argument("--h", help="Height of target image", type=int, required=False)

parsed = parser.parse_args()

ROOT_DIR = parsed.src
# TRAIN_RATIO = parsed.train
# TEST_RATIO = parsed.test
WIDTH = parsed.w
HEIGHT = parsed.h

#full path to dataset directory

EXT_DIR = os.getcwd()

TRAIN_FILE = "dataset_images.csv"
JSON_FILE = "mappings.json"
# TEST_FILE = "test_images.csv"

# test_path = os.path.join(EXT_DIR, '/test/')
train_path = os.path.join(EXT_DIR, '/train_dataset/')
# os.mkdir(test_path)
os.mkdir(train_path)
# TEST_FILE_PATH = os.path.join(test_path, TEST_FILE)
TRAIN_FILE_PATH = os.path.join(train_path, TRAIN_FILE)

JSON_FILE_PATH = os.path.join(train_path, JSON_FILE)

FULL_PATH = os.path.join(os.getcwd(), ROOT_DIR)
MAPPING_DICT = { }
CLASS_DIRS = os.listdir(FULL_PATH)


i = 0
for CLASS in CLASS_DIRS:
    MAPPING_DICT[i] = CLASS
    #Full path to class_i directory
    CLASS_PATH = os.path.join(FULL_PATH, CLASS)
    #List all the images
    image_list = os.listdir(CLASS_PATH)
    #partition_index = int(((TRAIN_RATIO / 100)*len(image_list)))
    #Divide list into train and test
    # train = image_list[0 : partition_index]
    # test = image_list[partition_index : len(image_list)]
    
    write_to_csv(TRAIN_FILE_PATH, WIDTH, HEIGHT, CLASS_PATH, image_list, i)
    # write_to_csv(TEST_FILE_PATH, WIDTH, HEIGHT, CLASS_PATH, test, i)
    #increment i after each class pass
    i+=1
    print(Fore.YELLOW + f"#################Class[{CLASS}] COMPLETED#############" + Fore.WHITE)
            
print(Fore.GREEN + "--------------------CSV ENTRY COMPLETED----------------------" + Fore.WHITE)

with open(JSON_FILE_PATH, 'a') as json_file:
    json.dump(MAPPING_DICT, json_file)
print(Fore.BLUE + "++++++++++++++++YOU ARE GOOD TO GO++++++++++++++++" + Fore.WHITE)
    
#Utility function to flatten images into csv file and insert 
# def convert_to_csv(dest, label_keys):
#     PATH_TO_DIR = os.path.join(os.getcwd(), dest)
#     image_file_list = os.listdir(PATH_TO_DIR)
#     for images in image_file_list:
#         image_path = os.path.join(os.getcwd(), images)
#         if image.endswith(".jpg"):
#             ld_image_obj = Image.open(image_path)
#             ld_image_obj = np.array(ld_image_obj)
        
