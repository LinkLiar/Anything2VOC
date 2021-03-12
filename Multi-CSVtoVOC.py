import numpy as np
import glob
import os
import string
import pandas as pd
from lxml.etree import Element, SubElement, tostring

WSI_MASK_PATH = 'E:\\Mango\\mangoes\\annotations\\' 

paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.csv'))
# paths.sort()
print(len(paths))
# Dataframe = pd.read_csv(csvpath)

def csv_xml(csv_path,img_name,xml_path):
    node_root = Element('annotation')
    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'mango'
    node_filename = SubElement(node_root, 'filename')
    #图像名称
    node_filename.text = str(img_name)+".png"
    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = "500"
    node_height = SubElement(node_size, 'height')
    node_height.text = "500"
    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '3'

    temp = pd.read_csv(csv_path)

    for i in range(len(temp.x)):
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = "mango"
        node_pose=SubElement(node_object, 'pose')
        node_pose.text="Unspecified"
        node_truncated=SubElement(node_object, 'truncated')
        node_truncated.text="truncated"
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = str(round(temp.x[i]))
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = str(round(temp.y[i]))
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = str(round(int(temp.x[i])+int(temp.dx[i])))
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = str(round(int(temp.y[i])+int(temp.dy[i])))
    xml = tostring(node_root, pretty_print=True)                    # 格式化显示，该换行的换行
    img_newxml = os.path.join(xml_path)
    file_object = open(img_newxml, 'wb')
    file_object.write(xml)
    file_object.close()
    print(img_name)

count = 1
for path in paths:

    Filename = "E:\\Mango\\mangoes\\XML\\" + str(count).rjust(4,'0')+ '.xml'
    img_name = str(count).rjust(4,'0')
    csv_xml(path,img_name,Filename)
    count = count + 1
print("Done")