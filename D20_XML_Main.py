import os
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from D20MX_XML_Functions import d20mx_check
from D20MPP_XML_Functions import d20mpp_check
from D20MEII_XML_Functions import d20meII_check
import xml.etree.ElementTree as et


if __name__ == '__main__':
    file_dir = Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename(title = 'Select XML to check')  # show an "Open" dialog box and return the path to the selected file
    print(filename)
    tree = et.parse(os.path.join(file_dir, filename))
    root = tree.getroot()

    orig_stdout = sys.stdout
    f = open(filename[:-4] + ' Check.txt', 'w+')
    sys.stdout = f

    print(filename[:-4])

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

    sys.stdout = orig_stdout
    f.close()