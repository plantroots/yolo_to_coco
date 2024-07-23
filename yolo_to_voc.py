import cv2
import pprint

from xml.dom.minidom import parseString
from xml.dom.minidom import Document
from lxml.etree import Element, SubElement, tostring


class XmlMaker:

    def __init__(self, txtpath, xmlpath):
        self.txtPath = txtpath
        self.xmlPath = xmlpath
        self.txtList = []

    def readtxt(self):
        jpg = []
        txtfile = open(self.txtPath, "r", encoding="gbk", errors="ignore")
        self.txtList = txtfile.readlines()
        for i in self.txtList:
            jpg = i.strip().split(" ")[0]
            xys = i.strip().split(" ")[1:]

            node_root = Element("annotation")
            node_folder = SubElement(node_root, "folder")
            node_folder.text = "VOC2012"
            node_filename = SubElement(node_root, "filename")
            node_filename.text = jpg
            img = cv2.imread(jpg)
            shape = img.shape

            node_size = SubElement(node_root, "size")
            node_width = SubElement(node_size, "width")

            node_width.text = str(shape[1])

            node_height = SubElement(node_size, "height")
            node_height.text = str(shape[0])

            node_depth = SubElement(node_size, "depth")
            node_depth.text = "3"

            for xy in xys:
                list_xy = xy.split(",")

                x_min = list_xy[0]
                y_min = list_xy[1]
                x_max = list_xy[2]
                y_max = list_xy[3]
                classes = list_xy[4]
                node_object = SubElement(node_root, "object")
                node_name = SubElement(node_object, "name")
                node_name.text = "person"
                node_difficult = SubElement(node_object, "difficult")
                node_difficult.text = "0"
                node_bndbox = SubElement(node_object, "bndbox")
                node_xmin = SubElement(node_bndbox, "xmin")
                node_xmin.text = str(x_min)
                node_ymin = SubElement(node_bndbox, "ymin")
                node_ymin.text = str(y_min)
                node_xmax = SubElement(node_bndbox, "xmax")
                node_xmax.text = str(x_max)
                node_ymax = SubElement(node_bndbox, "ymax")
                node_ymax.text = str(y_max)

            xml = tostring(node_root, pretty_print=True)
            xml_name = jpg.split("/")[-1][:-4] + ".xml"
            print(xml_name)
            with open(self.xmlPath + "/" + xml_name, "wb") as f:
                f.write(xml)
                f.close()


if __name__ == "__main__":
    read = XmlMaker("train.txt", "Annotations")
    read.readtxt()
