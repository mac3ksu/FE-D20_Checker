import os
from D20MPP_XML_Functions import d20mpp_check
import xml.etree.ElementTree as et

if __name__ == '__main__':
    filename = 'PLVLY_Q D20M++.xml'
    file_dir = os.path.expanduser(os.path.join('~', 'Documents', 'GitHub', 'FE-D20_Checker', 'Example D20 XML', 'D20M++'))
    tree = et.parse(os.path.join(file_dir, filename))
    root = tree.getroot()

    print(filename)

    # with open(os.path.join(directory, xml_filename[:-4]+'_Check.txt')) as of:
    if root[0][0].get('Device_Type') == 'D20':
        d20mpp_check(filename, file_dir)