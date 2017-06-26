import os
from D20MX_XML_Functions import d20mx_check
import xml.etree.ElementTree as et


if __name__ == '__main__':
    filename = 'HIGHLNDX.xml'
    file_dir = os.path.expanduser(os.path.join('~', 'Desktop', 'D20 XML'))
    tree = et.parse(os.path.join(file_dir, filename))
    root = tree.getroot()

    print(filename)

    # with open(os.path.join(directory, xml_filename[:-4]+'_Check.txt')) as of:
    if root[0][0].get('Device_Type') == 'D20MX':
        d20mx_check(filename, file_dir)
