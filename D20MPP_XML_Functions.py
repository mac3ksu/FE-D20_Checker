import xml.etree.ElementTree as ET
import os

def d20mpp_check(xml_filename, directory):
    tree = ET.parse(os.path.join(directory, xml_filename))
    root = tree.getroot()

    # with open(os.path.join(directory, xml_filename[:-4]+'_Check.txt')) as of:
    print(root[0][0].get('Device_Type'))
    for app in root[0][0][1][0]:
        #print(app.get('Application_Name'), app.get('Application_Identifier'))
        if app.get('Application_Identifier') == 'B003':
           # print(app.get('Application_Name'))
           b003_check(app)
        if app.get('Application_Identifier') == 'B023':
           # print(app.get('Application_Name'))
           b023_check(app)
        if app.get('Application_Identifier') == 'B014-1N':
            # print(app.get('Application_Name'))
            b014_check(app)
        if app.get('Application_Identifier') == 'A083-0':
            # print(app.get('Application_Name'))
            a083_check(app)
        if app.get('Application_Identifier') == 'B015':
            # print(app.get('Application_Name'))
            b015_check(app)

def b003_check(app):
    # The XML export does not contain the report deadband.
    print('B003 - D.20 Peripheral Link')
    print('\t', 'Report Deadband not in XML')
    return

def b023_check(app):
    # <app>
    #   <table "B023_CFG">
    #   <table "B023_DEV">
    #   <table "B023_PNT">
    #   <table "B023_POL">

    print('B023 - DNP DCA')
    print('\t', 'B023_PNT')
    b023_pnt_list = []

    for i, record in enumerate(app[2]):
        print('\t\t', i, '-', record[0].get('Field_Value'), ':', record[1].get('Field_Value'))
        b023_pnt_list.append((record[0].get('Field_Value'), record[1].get('Field_Value')))

    print('\t', 'B023_POL')
    b023_pol_list = []
    for i, record in enumerate(app[3]):
        print('\t\t', 'Record', ':', i)
        print('\t\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
        print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
        print('\t\t\t', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))
        print('\t\t\t', record[5].get('Field_Name'), ':', record[5].get('Field_Value'))
        print('\t\t\t', record[6].get('Field_Name'), ':', record[6].get('Field_Value'))
        print('\t\t\t', record[7].get('Field_Name'), ':', record[7].get('Field_Value'))
        print('\t\t\t', record[8].get('Field_Name'), ':', record[8].get('Field_Value'))
        b023_pol_list.append((i, record[0].get('Field_Value')))

    print('\t' 'B023_DEV')
    b023_dev_list = []
    for i, record in enumerate(app[1]):
        print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
        print('\t\t\t', record[3][0][0][7].get('Field_Name'), ':', record[3][0][0][7].get('Field_Value'))
        print('\t\t\t', record[3][0][0][8].get('Field_Name'), ':', record[3][0][0][8].get('Field_Value'))
        print('\t\t\t', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))
        print('\t\t\t', record[6].get('Field_Name'), ':', record[6].get('Field_Value'))
        print('\t\t\t', record[8][0][0][2].get('Field_Name'), ':', record[8][0][0][2].get('Field_Value'))
        print('\t\t\t', record[8][0][0][3].get('Field_Name'), ':', record[8][0][0][3].get('Field_Value'))
        for index in range(int(record[8][0][0][2].get('Field_Value')),
                           int(record[8][0][0][2].get('Field_Value')) + int(
                                   record[8][0][0][3].get('Field_Value'))):
            print('\t\t\t\t', b023_pnt_list[index])
        print('\t\t\t', record[8][0][0][4].get('Field_Name'), ':', record[8][0][0][4].get('Field_Value'))
        print('\t\t\t', record[8][0][0][5].get('Field_Name'), ':', record[8][0][0][5].get('Field_Value'))
        for index in range(int(record[8][0][0][4].get('Field_Value')),
                           int(record[8][0][0][4].get('Field_Value')) + int(
                                   record[8][0][0][5].get('Field_Value'))):
            print('\t\t\t\t', b023_pol_list[index])
        print('\t\t\t', record[9][0][0][5].get('Field_Name'), ':', record[9][0][0][5].get('Field_Value'))
        b023_dev_list.append(record[0].get('Field_Value'))

    print('\t' 'B023_CFG')
    for i, record in enumerate(app[0]):
        print('\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
        print('\t\t\t', record[3].get('Field_Name'), ':', record[3].get('Field_Value'))
        print('\t\t\t', record[2][0][0][0].get('Field_Name'), ':', record[2][0][0][0].get('Field_Value'))
        print('\t\t\t', 'Devices in DCA:')
        for index in range(int(record[10].get('Field_Value')),
                           int(record[10].get('Field_Value')) + int(record[11].get('Field_Value'))):
            print('\t\t\t\t', b023_dev_list[index])
    return

def b014_check(app):
    # Check SOE BUFFER SIZE = 500
    # Check SOE LOCATION = NVRAM
    # Check User Name = something
    # Check Password = something
    # Check Control Password = something

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    print('\t', app[3][0][0].get('Field_Name'), ':', app[3][0][0].get('Field_Value'))
    print('\t', app[3][0][4][0][0][0].get('Field_Name'), ':', app[3][0][4][0][0][0].get('Field_Value'))
    print('\t', app[9][0][6].get('Field_Name'), ':', app[9][0][6].get('Field_Value'))
    print('\t', app[9][0][7].get('Field_Name'), ':', app[9][0][7].get('Field_Value'))
    print('\t', app[9][0][8].get('Field_Name'), ':', app[9][0][8].get('Field_Value'))

def a083_check(app):
    # Check all calc points have Event Types = Both

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))
    for record in app[2][2]:
        print('\t Calc', record.get('Record_Number'))
        print('\t Calc', record.get('Record_Number'), '-', record[0][1].get('Field_Name'), ':', record[0][1].get('Field_Value'))

def b015_check(app):
    # Check Bridgeman app

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    # Count the number of remote DNP devices
    num_dnp_dev = 0
    for record in app[5]:
        num_dnp_dev += 1
    print('\t', num_dnp_dev, 'remote DNP devices')
    print('\t', app[0][0][1].get('Field_Name'), ':', app[0][0][1].get('Field_Value'))

    print('\t', 'Local Application Table [DNP Address(Hex), Data Link channel]')
    for record in app[3]:
        print('\t\t', record[0].get('Field_Value'), '(x', record[3].get('Field_Value'), ')',
              record[2].get('Field_Value'))

    print('\t', 'Remote Application Table [DNP Address(Hex), Data Link channel]')
    for record in app[5]:
        print('\t\t', record[0].get('Field_Value'), '(x', record[3].get('Field_Value'), ')',
              record[2].get('Field_Value'))