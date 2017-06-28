import xml.etree.ElementTree as ET
import os


def d20meII_check(xml_filename, directory):
    tree = ET.parse(os.path.join(directory, xml_filename))
    root = tree.getroot()

    # with open(os.path.join(directory, xml_filename[:-4]+'_Check.txt')) as of:
    print(root[0][0].get('Device_Type'))