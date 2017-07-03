import os
from D20MX_XML_Functions import d20mx_check
from D20MPP_XML_Functions import d20mpp_check
from D20MEII_XML_Functions import d20meII_check
import xml.etree.ElementTree as et


if __name__ == '__main__':
    filename = 'OAKDAL2G D20ME.xml'
    file_dir = os.path.expanduser(os.path.join('~', 'Documents', 'GitHub', 'FE-D20_Checker', 'Example D20 XML', 'D20MEII'))
    tree = et.parse(os.path.join(file_dir, filename))
    root = tree.getroot()

    # filename = 'MAYFIEAO D20ME.xml'
    # file_dir = os.path.expanduser(os.path.join('~', 'Documents', 'GitHub', 'FE-D20_Checker', 'Example D20 XML', 'D20MEII'))
    # tree = et.parse(os.path.join(file_dir, filename))
    # root = tree.getroot()

    # filename = 'PLVLY_Q D20M++.xml'
    # file_dir = os.path.expanduser(os.path.join('~', 'Documents', 'GitHub', 'FE-D20_Checker', 'Example D20 XML', 'D20M++'))
    # tree = et.parse(os.path.join(file_dir, filename))
    # root = tree.getroot()

    # filename = 'LORAIN_H.xml'
    # file_dir = os.path.expanduser(os.path.join('~', 'Documents', 'GitHub', 'FE-D20_Checker', 'Example D20 XML', 'D20MX'))
    # tree = et.parse(os.path.join(file_dir, filename))
    # root = tree.getroot()

    print(filename)

    if root[0][0][1][0].get('Part_Number') == '526-1006':
        # This is a D20M++
        d20mpp_check(filename, file_dir)
    elif root[0][0][1][0].get('Part_Number') == '526-3001':
        # This is a D20MX
        d20mx_check(filename, file_dir)
    elif root[0][0][1][0].get('Part_Number') == '526-2007 CCU':
        # This is a D20MEII
        d20meII_check(filename, file_dir)

    #if root[0][0].get('Device_Type') == 'D20MX':
    #    d20mx_check(filename, file_dir)


