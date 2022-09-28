# This script was used to create train, test and validation datasets

from fileinput import filename
import os
import subprocess
import glob

dir_list = ['train', 'test', 'val']


image_dir = "/home/jaydeep/pictor-ppe/data/CHV_dataset/resized_images/images"
image_fps = glob.glob(os.path.join(image_dir, "*.jpg"))


# for image_fp in image_fps:

#     image_name = image_fp.split('/')[-1]
#     label_name = image_name.strip().replace('jpg','txt')
#     labels_fp = os.path.join(labelFilepath,label_name)
#     subprocess.call(["cp", labels_fp, destinationFilePath])


# destinationImageFilePath = "/home/jaydeep/pictor-ppe/data/Images_test"

sourceImageFilePath = "/home/jaydeep/pictor-ppe/data/CHV_dataset/resized_images/total/images"
labelFilepath = "/home/jaydeep/pictor-ppe/data/CHV_dataset/resized_images/total/kitti_labels"
destinationFilePath = "/home/jaydeep/pictor-ppe/data/CHV_dataset/resized_images/"

trainImageFp = "/home/jaydeep/pictor-ppe/data/CHV_dataset/data_split/train.txt"
testImageFp = "/home/jaydeep/pictor-ppe/data/CHV_dataset/data_split/test.txt"
validImageFp = "/home/jaydeep/pictor-ppe/data/CHV_dataset/data_split/valid.txt"

# # for dr in dir_list:
# #     print("/home/jaydeep/pictor-ppe/data/CHV_dataset/data_split/"+dr+"_data")
# #     if not os.path.exists("/home/jaydeep/pictor-ppe/data/CHV_dataset/data_split/"+dr+"_data"):
# #         os.mkdir(dr+"_data")
# #     if not os.path.exists("/home/jaydeep/pictor-ppe/data/CHV_dataset/data_split/"+dr+"_data/images/"):
# #         os.mkdir(dr+"_data/images")
# #     if not os.path.exists("/home/jaydeep/pictor-ppe/data/CHV_dataset/data_split/"+dr+"_data/labels"):
# #         os.mkdir(dr+"_data/lables")

with open(testImageFp, "r") as fh:
    data=fh.readlines()

    for cc,line in enumerate(data):
        line = line.split("/")
        image_name = line[-1].strip()
        label_name = line[-1].strip().replace('jpg','txt')
        image_fp = os.path.join(sourceImageFilePath,image_name)
        labels_fp = os.path.join(labelFilepath,label_name)
        # print(image_name)
        # print(labels_fp)
        
        subprocess.call(["cp", image_fp, os.path.join(destinationFilePath, "test/images")])
        subprocess.call(["cp", labels_fp, os.path.join(destinationFilePath, "test/labels")])
        
