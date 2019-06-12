import re
import math
import logging
import numpy as np
import cv2
import glob
import os
import xml.etree.ElementTree as ET

#-------------------------------------XML路径------------------------------------------
trainxml_dir = "E:\\pythonfile\\Data\\trainxml\\"
valxml_dir   = "E:\\pythonfile\\Data\\valxml\\"

#-------------------------------------txt路径------------------------------------------
traintxt_path = "E:\\pythonfile\\Data\\labels\\train\\"
valtxt_path = "E:\\pythonfile\\Data\\labels\\val\\"

class_names = ["Pedestrian","Car"]
#  xml文件路径，train_images只需改为val_images就可以处理val_images的了
def single_xml_to_txt(xml_file,txt_path):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filepath = os.path.split(xml_file)[1]#获得文件名
    filepath = os.path.join(txt_path,filepath)
    txt_file = filepath.split('.')[0] + '.txt'
    with open(txt_file, 'w') as txt_file:
        for member in root.findall('object'):
            #print(member)
            # filename = root.find('filename').text
            picture_width = int(root.find('size')[0].text)
            picture_height = int(root.find('size')[1].text)
            class_name = member[0].text
            #  类名对应的index
            class_num = class_names.index(class_name)
            #这里需要根据具体的读到的xml文件来改正
            box_x_min = int(member[1][0].text)  # 左上角横坐标
            box_y_min = int(member[1][1].text)  # 左上角纵坐标
            box_x_max = int(member[1][2].text)  # 右下角横坐标
            box_y_max = int(member[1][3].text)  # 右下角纵坐标
            # 转成相对位置和宽高
            x_center = (box_x_min + box_x_max) / (2 * picture_width)
            y_center = (box_y_min + box_y_max) / (2 * picture_height)
            width = (box_x_max - box_x_min) / picture_width
            height = (box_y_max - box_y_min) / picture_height
            #print(class_num, x_center, y_center, width, height)
            txt_file.write(
                str(class_num) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width) + ' ' + str(height) + '\n')

#  转换文件夹下的所有xml文件为txt
def dir_xml_to_txt(pathxml,pathtxt):
	for xml_file in glob.glob(pathxml + '*.xml'):
		single_xml_to_txt(xml_file,pathtxt)

dir_xml_to_txt(valxml_dir,valtxt_path)