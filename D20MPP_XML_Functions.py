import xml.etree.ElementTree as ET
import os

def d20mpp_check(xml_filename, directory):
    tree = ET.parse(os.path.join(directory, xml_filename))
    root = tree.getroot()

    # with open(os.path.join(directory, xml_filename[:-4]+'_Check.txt')) as of:
    print(root[0][0].get('Device_Type'))
    for app in root[0][0][1][0]:
        #print(app.get('Application_Name'), app.get('Application_Identifier'))
        if app.get('Application_Identifier') == 'A003':
            # print(app.get('Application_Name'))
            a003_check(app)
        if app.get('Application_Identifier') == 'A020':
            # print(app.get('Application_Name'))
            a020_check(app)
        if app.get('Application_Identifier') == 'A026':
            # print(app.get('Application_Name'))
            a026_check(app)
        if app.get('Application_Identifier') == 'A030':
            # print(app.get('Application_Name'))
            a030_check(app)
        if app.get('Application_Identifier') == 'A083-0':
            # print(app.get('Application_Name'))
            a083_check(app)
        if app.get('Application_Identifier') == 'B003':
           # print(app.get('Application_Name'))
           b003_check(app)
        if app.get('Application_Identifier') == 'B013':
            # print(app.get('Application_Name'))
            b013_check(app)
        if app.get('Application_Identifier') == 'B014':
            # print(app.get('Application_Name'))
            b014_check(app)
        if app.get('Application_Identifier') == 'B015':
            # print(app.get('Application_Name'))
            b015_check(app)
        if app.get('Application_Identifier') == 'B021':
            # print(app.get('Application_Name'))
            b021_check(app)
        if app.get('Application_Identifier') == 'B023':
           # print(app.get('Application_Name'))
           b023_check(app)

def a003_check(app):
    # Check SOE
    # Check Offline Condition
    # Check Contact BUR/BASE Time

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    print('\t', app[6].get('Table_Identifier'), ':', app[6].get('Table_Name'), 'Table')
    print('\t\t', app[6][0][2].get('Field_Name'), ':', app[6][0][2].get('Field_Value'))

    print('\t', app[1].get('Table_Identifier'), ':', app[1].get('Table_Name'), 'Table')

    for i, record in enumerate(app[1]):
        print('\t\t', record[16].get('Field_Name'), ':', record[16].get('Field_Value'))

    print('\t', app[7].get('Table_Identifier'), ':', app[7].get('Table_Name'), 'Table')
    print('\t\t', app[7][0][1].get('Field_Name'), ':', app[7][0][1].get('Field_Value'))

def a020_check(app):
    # Check RE-INIT Interval

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    print('\t', app[1][0][4].get('Field_Name'), ':', app[1][0][4].get('Field_Value'))

def a026_check(app):
    # Check Point Type
    # Check System Point
    # Check Comm Event Point
    # Check Normal State

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    print('\t', app[0].get('Table_Identifier'), ':', app[0].get('Table_Name'), 'Table')

    for i, record in enumerate(app[0]):
        print('\t\t', i+1, ':')
        print('\t\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
        print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
        print('\t\t\t', record[2].get('Field_Name'), ':', record[2].get('Field_Value'))
        print('\t\t\t', record[3].get('Field_Name'), ':', record[3].get('Field_Value'))

    # Check SOE Enable
    # Check COS Enable

    print('\t', app[2].get('Table_Identifier'), ':', app[2].get('Table_Name'), 'Table')

    print('\t\t', app[2][0][1].get('Field_Name'), ':', app[2][0][1].get('Field_Value'))
    print('\t\t', app[2][0][2].get('Field_Name'), ':', app[2][0][2].get('Field_Value'))

def a030_check(app):
    # Check Time Sync Wait
    # Check Status/ACC Freeze
    # Check ACC Freeze/ Controls

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    print('\t', app[1].get('Table_Identifier'), ':', app[1].get('Table_Name'), 'Table')

    for i, record in enumerate(app[1]):
        print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
        print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))

    print('\t', app[2].get('Table_Identifier'), ':', app[2].get('Table_Name'), 'Table')

    for i, record in enumerate(app[2]):
        print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
        print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))

    print('\t', app[3].get('Table_Identifier'), ':', app[3].get('Table_Name'), 'Table')

    for i, record in enumerate(app[3]):
        print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
        print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))

def a083_check(app):
    # Check That All Points Have Event Types = Both

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))
    print('\t D20 Calculator does not have event types')
    # for record in app[2][0]:
    #     print('\t Calc', record.get('Record_Number'))
    #     print('\t Calc', record.get('Record_Number'), '-', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))

def b003_check(app):
    # The XML export does not contain the report deadband.
    print('B003 - D.20 Peripheral Link')
    print('\t', 'Report Deadband not in XML')
    return

def b013_check(app):
    # Check Baud Rate
    # Check DCD, RTS, & CTS
    # Check DCD to RX Enable Time
    # Check RTS Preamble
    # Check RTS Postamble
    # Check Max Frame Size
    # Check Transmit Retries
    # Check Transmit Buffers
    # Check Receive Buffers
    # Check Confirm Timeout
    # Check Response Timeout

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    print('\t', app[0].get('Table_Identifier'), ':', app[0].get('Table_Name'), 'Table')
    print('\t\t', app[0][0][1].get('Field_Name'), ':', app[0][0][1].get('Field_Value'))
    print('\t\t', app[0][0][3].get('Field_Name'), ':', app[0][0][3].get('Field_Value'))
    print('\t\t', app[0][0][4].get('Field_Name'), ':', app[0][0][4].get('Field_Value'))
    print('\t\t', app[0][0][5].get('Field_Name'), ':', app[0][0][5].get('Field_Value'))
    print('\t\t', app[0][0][6].get('Field_Name'), ':', app[0][0][6].get('Field_Value'))
    print('\t\t', app[0][0][7].get('Field_Name'), ':', app[0][0][7].get('Field_Value'))
    print('\t\t', app[0][0][8].get('Field_Name'), ':', app[0][0][8].get('Field_Value'))
    print('\t\t', app[0][0][9].get('Field_Name'), ':', app[0][0][9].get('Field_Value'))
    print('\t\t', app[0][0][10].get('Field_Name'), ':', app[0][0][10].get('Field_Value'))
    print('\t\t', app[0][0][11].get('Field_Name'), ':', app[0][0][11].get('Field_Value'))
    print('\t\t', app[0][0][12].get('Field_Name'), ':', app[0][0][12].get('Field_Value'))
    print('\t\t', app[0][0][13].get('Field_Name'), ':', app[0][0][13].get('Field_Value'))
    print('\t\t', app[0][0][14].get('Field_Name'), ':', app[0][0][14].get('Field_Value'))

def b014_check(app):
    # Check SOE BUFFER SIZE = 500
    # Check SOE LOCATION = NVRAM

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    print('\t', app[1][0][0].get('Field_Name'), ':', app[1][0][0].get('Field_Value'))
    print('\t', app[1][0][4][0][0][0].get('Field_Name'), ':', app[1][0][4][0][0][0].get('Field_Value'))

    # Check the Standard UTC Offset
    # Check the DST Offset

    print('\t', app[4].get('Table_Identifier'), ':', app[4].get('Table_Name'))

    print('\t\t', app[4][0][11].get('Field_Name'), ':', app[4][0][11].get('Field_Value'))
    print('\t\t', app[4][0][12].get('Field_Name'), ':', app[4][0][12].get('Field_Value'))

    # Check User Name = something
    # Check Password = something
    # Check Control Password = something

    print('\t', app[2][0][5].get('Field_Name'), ':', app[2][0][5].get('Field_Value'))
    print('\t', app[2][0][6].get('Field_Name'), ':', app[2][0][6].get('Field_Value'))
    print('\t', app[2][0][7].get('Field_Name'), ':', app[2][0][7].get('Field_Value'))

    # Check Welcome Message for Field Value 15

    print('\t', app[5].get('Table_Identifier'), ':', app[5].get('Table_Name'))

    print('\t\t', app[5][8][3].get('Field_Name'), ':', app[5][8][3].get('Field_Value'))

def b015_check(app):
    # Check Bridgeman app

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    # Count the number of remote DNP devices
    num_dnp_dev = 0
    for record in app[2][0]:
        num_dnp_dev += 1
    print('\t', num_dnp_dev, 'remote DNP devices')
    print('\t', app[0][0][1].get('Field_Name'), ':', app[0][0][1].get('Field_Value'))

    print('\t', 'Local Application Table [LAN Address(Hex), Data Link Channel]')
    for record in app[2]:
        print('\t\t', record[0].get('Field_Value'), '(x', record[3].get('Field_Value'), ')',
              record[2].get('Field_Value'))

    print('\t', 'Remote Application Table [LAN Address(Hex), Data Link Channel]')
    for record in app[3]:
        print('\t\t', record[0].get('Field_Value'), '(x', record[3].get('Field_Value'), ')',
              record[2].get('Field_Value'))

    # Check TXT Delay to Appl.
    print('\t', app[3][1][4].get('Field_Name'), ':', app[3][1][4].get('Field_Value'))

def b021_check(app):
    # Check Datalink Confirm
    # Check Idle Report Period

    print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

    print('\t', app[0].get('Table_Identifier'), ':', app[0].get('Table_Name'), 'Table')
    print('\t\t', app[0][0][14].get('Field_Name'), ':', app[0][0][14].get('Field_Value'))
    print('\t\t', app[0][0][11].get('Field_Name'), ':', app[0][0][11][0].get('Table_Identifier'))
    print('\t\t\t', app[0][0][11][0][0][5].get('Field_Name'), ':', app[0][0][11][0][0][5].get('Field_Value'))

def b023_check(app):
    # <app>
    #   <table "B023_CFG">
    #   <table "B023_DEV">
    #   <table "B023_PNT">
    #   There is no B023_POL

    print('B023 - DNP DCA')
    print('\t', 'B023_PNT')
    b023_pnt_list = []

    for i, record in enumerate(app[2]):
        print('\t\t', i, '-', record[0].get('Field_Value'), ':', record[1].get('Field_Value'))
        b023_pnt_list.append((record[0].get('Field_Value'), record[1].get('Field_Value')))

    print('\t', 'B023_POL')
    #b023_pol_list = []
    print('\t\t D20 DNP DCA does not have a POL list')
    # for i, record in enumerate(app[3]):
    #     print('\t\t', 'Record', ':', i)
    #     print('\t\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
    #     print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
    #     print('\t\t\t', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))
    #     print('\t\t\t', record[5].get('Field_Name'), ':', record[5].get('Field_Value'))
    #     print('\t\t\t', record[6].get('Field_Name'), ':', record[6].get('Field_Value'))
    #     print('\t\t\t', record[7].get('Field_Name'), ':', record[7].get('Field_Value'))
    #     print('\t\t\t', record[8].get('Field_Name'), ':', record[8].get('Field_Value'))
    #     b023_pol_list.append((i, record[0].get('Field_Value')))

    print('\t', 'B023_DEV')
    b023_dev_list = []
    for i, record in enumerate(app[1]):
        #Application Address
        print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
        #Poll Interval (s)
        print('\t\t\t', record[5][0][0][3].get('Field_Name'), ':', record[5][0][0][3].get('Field_Value'))
        #Integrity Poll Interval
        print('\t\t\t', record[6].get('Field_Name'), ':', record[6].get('Field_Value'))
        #Offline After Fail
        print('\t\t\t', record[3][0][0][8].get('Field_Name'), ':', record[3][0][0][8].get('Field_Value'))
        #Failures For Bad Channel
        print('\t\t\t', record[7].get('Field_Name'), ':', record[7].get('Field_Value'))
        #Time Syncing
        print('\t\t\t', record[3][0][0][4].get('Field_Name'), ':', record[3][0][0][4].get('Field_Value'))
        #Data Link CFM Required
        print('\t\t\t', record[3][0][0][7].get('Field_Name'), ':', record[3][0][0][7].get('Field_Value'))
        #First Point Record
        print('\t\t\t', record[9][0][0][2].get('Field_Name'), ':', record[9][0][0][2].get('Field_Value'))
        #Number of Point Records
        print('\t\t\t', record[9][0][0][3].get('Field_Name'), ':', record[9][0][0][3].get('Field_Value'))
        for index in range(int(record[9][0][0][2].get('Field_Value')),
                           int(record[9][0][0][2].get('Field_Value')) + int(
                                   record[9][0][0][3].get('Field_Value'))):
            print('\t\t\t\t', b023_pnt_list[index])
        # There are no POLL Records for the D20 DNP DCA
        # print('\t\t\t', record[8][0][0][4].get('Field_Name'), ':', record[8][0][0][4].get('Field_Value'))
        # print('\t\t\t', record[8][0][0][5].get('Field_Name'), ':', record[8][0][0][5].get('Field_Value'))
        # for index in range(int(record[9][0][0][4].get('Field_Value')),
        #                    int(record[9][0][0][4].get('Field_Value')) + int(
        #                            record[9][0][0][5].get('Field_Value'))):
        #     print('\t\t\t\t', b023_pol_list[index])
        # print('\t\t\t', record[9][0][0][5].get('Field_Name'), ':', record[9][0][0][5].get('Field_Value'))
        b023_dev_list.append(record[0].get('Field_Value'))

    print('\t' 'B023_CFG')
    for i, record in enumerate(app[0]):
        #DCA Address
        print('\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
        #Restart Delay
        print('\t\t\t', record[2].get('Field_Name'), ':', record[2].get('Field_Value'))
        print('\t\t\t', 'Devices in DCA:')
        for index in range(int(record[8].get('Field_Value')),
                           int(record[8].get('Field_Value')) + int(record[9].get('Field_Value'))):
            print('\t\t\t\t', b023_dev_list[index])
    return