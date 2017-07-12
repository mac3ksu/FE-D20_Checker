import xml.etree.ElementTree as ET
import xlrd
import os

def set_comlist():
  global b013_com_list # Needed to modify global copy of globvar
  b013_com_list = []

def d20meII_check(xml_filename, directory):
    tree = ET.parse(os.path.join(directory, xml_filename))
    root = tree.getroot()

    # with open(os.path.join(directory, xml_filename[:-4]+'_Check.txt')) as of:
    print(root[0][0][1][0].get('Part_Number'))
    for app in root[0][0][1][0]:
        # print(app.get('Application_Name'), app.get('Application_Identifier'))
        if app.get('Application_Identifier') == 'A003':
            # print(app.get('Application_Name'))
            a003_check(app)
        if app.get('Application_Identifier') == 'A020':
            # print(app.get('Application_Name'))
            a020_check(app)
        if app.get('Application_Identifier') == 'A026-1':
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
        if app.get('Application_Identifier') == 'B014-1':
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

# Application A003 is NOT in the D20MEII XML File
def a003_check(app):
    # Check SOE
    # Check Offline Condition
    # Check Contact BUR/BASE Time

    # Check if the Application is Enabled
    if app.get('Enabled')=='True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        print('\t', app[6].get('Table_Identifier'), ':', app[6].get('Table_Name'), 'Table')
        # Tracker Variable
        count = 0
        # Loop Through the Table
        for i, record in enumerate(app[6]):
            if app[6][0][2].get('Field_Value') == 'No':
                count
            else:
                count = count + 1
        # Print Statement if an SOE Variable Differs
        if count == 0:
            print('\t\t', app[6][0][2].get('Field_Name'), ':', app[6][0][2].get('Field_Value'))
        else:
            print('An SOE value differs from the rest. Please check the SGConfig.')

        print('\t', app[1].get('Table_Identifier'), ':', app[1].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[1]):
            print('\t\t', record[16].get('Field_Name'), ':', record[16].get('Field_Value'))

        print('\t', app[7].get('Table_Identifier'), ':', app[7].get('Table_Name'), 'Table')
        # Tracker Variable
        count2 = 0
        # Loop Through the Table
        for i, record in enumerate(app[7]):
            if app[7][0][1].get('Field_Value') == '500':
                count2
            else:
                count2 = count2 + 1
        if count2 == 0:
            print('\t\t', app[7][0][1].get('Field_Name'), ':', app[7][0][1].get('Field_Value'))
        else:
            print('A Contact Dur/Base Time value differs from the rest. Please check the SGConfig.')
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def a020_check(app):
    # Check RE-INIT Interval

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))
        # Loop Through the Table
        for i, record in enumerate(app[1]):
            print('\t', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def a026_check(app):
    # Check Operating Condition
    # Check Channel Type/Specifier
    # Check Status Point
    # Check Normal State
    # Check Start Point

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        print('\t', app[0].get('Table_Identifier'), ':', app[0].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[0]):
            print('\t\t', i, ':')
            print('\t\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
            print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
            print('\t\t\t', record[2].get('Field_Name'), ':', record[2].get('Field_Value'))
            print('\t\t\t', record[3].get('Field_Name'), ':', record[3].get('Field_Value'))
            print('\t\t\t', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))

    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def a030_check(app):
    # Check Time Sync Wait
    # Check Status/ACC Freeze
    # Check ACC Freeze/ Controls

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        print('\t', app[1].get('Table_Identifier'), ':', app[1].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[1]):
            print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
            print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))

        print('\t', app[2].get('Table_Identifier'), ':', app[2].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[2]):
            print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
            print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))

        print('\t', app[3].get('Table_Identifier'), ':', app[3].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[3]):
            print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
            print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def a083_check(app):
    # Check all calc points have Event Types = Both

    # Check if Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))
        for record in app[5]:
            print('\t Calc', record.get('Record_Number'), '-', record[2].get('Field_Name'), ':',
                  record[2].get('Field_Value'))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b003_check(app):
    # Check if Application is Enabled
    if app.get('Enabled') == 'True':
        # The XML export does not contain the report deadband.
        print('B003 - D.20 Peripheral Link')
        print('\t', 'Report Deadband not in XML')
        return
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b013_check(app):
    # Check Reset Link on Rx NACK
    # Check DCD, RTS, & CTS
    # Check DCD to RX Enable Time
    # Check Baud Rate
    # Check RTS Preamble
    # Check RTS Postamble
    # Check Max Frame Size
    # Check Transmit Retries
    # Check Transmit Buffers
    # Check Receive Buffers
    # Check Confirm Timeout
    # Check Response Timeout

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        print('\t', app[0].get('Table_Identifier'), ':', app[0].get('Table_Name'), 'Table')
        # Port Com Global Variable
        set_comlist()
        # Loop Through the Table
        for i, record in enumerate(app[0]):
            print('\t\t', i, ':')
            print('\t\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
            print('\t\t\t', record[2].get('Field_Name'), ':', record[2].get('Field_Value'))
            print('\t\t\t', record[3].get('Field_Name'), ':', record[3].get('Field_Value'))
            print('\t\t\t', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))
            print('\t\t\t', record[5].get('Field_Name'), ':', record[5].get('Field_Value'))
            print('\t\t\t', record[6].get('Field_Name'), ':', record[6].get('Field_Value'))
            print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
            print('\t\t\t', record[7].get('Field_Name'), ':', record[7].get('Field_Value'))
            print('\t\t\t', record[8].get('Field_Name'), ':', record[8].get('Field_Value'))
            print('\t\t\t', record[9].get('Field_Name'), ':', record[9].get('Field_Value'))
            print('\t\t\t', record[10].get('Field_Name'), ':', record[10].get('Field_Value'))
            print('\t\t\t', record[11].get('Field_Name'), ':', record[11].get('Field_Value'))
            print('\t\t\t', record[12].get('Field_Name'), ':', record[12].get('Field_Value'))
            print('\t\t\t', record[13].get('Field_Name'), ':', record[13].get('Field_Value'))
            print('\t\t\t', record[14].get('Field_Name'), ':', record[14].get('Field_Value'))

            # Append Port Com to list
            b013_com_list.append((record[0].get('Field_Value')))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b014_check(app):
    # Check SOE BUFFER SIZE = 500
    # Check SOE LOCATION = NVRAM
    # Check User Name = something
    # Check Password = something
    # Check Control Password = something

    # Check if Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        print('\t', app[3].get('Table_Identifier'), ':', app[3].get('Table_Name'), 'Table')
        for i, record in enumerate(app[3]):
            print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
            print('\t\t', record[4][0][0][0].get('Field_Name'), ':', record[4][0][0][0].get('Field_Value'))

        print('\t', app[4].get('Table_Identifier'), ':', app[4].get('Table_Name'), 'Table')
        for i, record in enumerate(app[4]):
            print('\t\t', record[5].get('Field_Name'), ':', record[5].get('Field_Value'))
            print('\t\t', record[6].get('Field_Name'), ':', record[6].get('Field_Value'))
            print('\t\t', record[7].get('Field_Name'), ':', record[7].get('Field_Value'))

        print('\t', app[7].get('Table_Identifier'), ':', app[7].get('Table_Name'), 'Table')
        for i, record in enumerate(app[7]):
            print('\t\t', '(', record.get('Record_Number'), ')', record[3].get('Field_Name'), ':', record[3].get('Field_Value'))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b015_check(app):
    # Check Bridgeman app

    # Check if Application in Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        # Count the number of remote DNP devices
        num_dnp_dev = 0
        for record in app[5]:
            num_dnp_dev += 1
        print('\t', num_dnp_dev, 'remote DNP devices')
        print('\t', app[0][0][1].get('Field_Name'), ':', app[0][0][1].get('Field_Value'))

        print('\t', 'Local Application Table [LAN Address(Hex), Data Link channel]')
        for i, record in enumerate(app[3]):
            print('\t\t', record[0].get('Field_Value'), '(x', record[3].get('Field_Value'), ')',
                  record[2].get('Field_Value'), ':', b013_com_list[i])

        print('\t', 'Remote Application Table [LAN Address(Hex), Data Link channel]')
        for record in app[5]:
            print('\t\t', record[0].get('Field_Value'), '(x', record[3].get('Field_Value'), ')',
                  record[2].get('Field_Value'), '   -   ', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b021_check(app):
    # Check Datalink Confirm
    # Check Time Sync Enable State
    # Check Offline Local IIN
    # Check Idle Report Period
    # Check SOE

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        print('\t', app[0].get('Table_Identifier'), ':', app[0].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[0]):
            print('\t\t', i, ':')
            print('\t\t\t', record[15].get('Field_Name'), ':', record[15].get('Field_Value'))
            print('\t\t\t', record[40].get('Field_Name'), ':', record[40].get('Field_Value'))
            print('\t\t\t', record[25][0][0][3].get('Field_Name'), ':', record[25][0][0][3].get('Field_Value'))
            print('\t\t\t', record[12][0][0][5].get('Field_Name'), ':', record[12][0][0][5].get('Field_Value'))

        print('\t', app[3].get('Table_Identifier'), ':', app[3].get('Table_Name'), 'Table')
        counter = 0
        for i, record in enumerate(app[3]):
            if record[3].get('Field_Value') == 'Enabled':
                counter
            else:
                counter = counter + 1
        if counter == 0:
            print('\t\t', app[3][0][3].get('Field_Name'), ':', app[3][0][3].get('Field_Value'))
        else:
            print('\t\t', 'An', app[3][0][3].get('Field_Name'), 'value is not enabled. Please check the SGConfig.')

        # Compare the Winpoints to what's programmed in the D20
        directory = os.path.expanduser(os.path.join('~', 'Documents', 'GitHub', 'FE-D20_Checker', 'Example D20 XML', 'D20MEII'))

        for thing in os.listdir(directory):
            if 'D20 DNP Map WinPt Check' in thing:
                filename = thing
                print('\t', filename)

        filepath = directory + '/' + filename

        wbook = xlrd.open_workbook(filepath)

        for sheet in wbook.sheet_names():
            if 'Sheet1' in sheet:
                wsheet_name = sheet

        wsheet = wbook.sheet_by_name(wsheet_name)

        for i, cell in enumerate(wsheet.row(1)):
            if cell.value == 'DNP INDEX':
                dnp_index = i
            elif cell.value == 'STATUS':
                status_index = i
            elif cell.value == 'ANALOG':
                analog_index = i
            elif cell.value == 'CONTROL':
                control_index = i

        # Status Point Check
        print('\t\t', 'Status Points Check')
        for i, record in enumerate(app[3]):
            xl_status = str(wsheet.cell_value(i + 2, status_index))
            check_value = record[0].get('Field_Value')
            if check_value[4] == '0':
                if check_value[5] == '0':
                    if xl_status[0] == (check_value[6]):
                        pass
                        # print('\t\t\t\t', check_value[6], ':', xl_status[0], '<status> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point (', i, ')', check_value[6], ':', xl_status[0], '<status> WinPt does not match the points list. Please refer to the SGConfig.')
                else:
                    if xl_status[0]+xl_status[1] == (check_value[5] + check_value[6]):
                        pass
                        # print('\t\t\t\t', check_value[5] + check_value[6], ':', xl_status[0] + xl_status[1], '<status> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point (', i, ')', check_value[5] + check_value[6], ':', xl_status[0] + xl_status[1], '<status> WinPt does not match the points list. Please refer to the SGConfig.')
            else:
                if xl_status[0] + xl_status[1] + xl_status[2] == (check_value[4] + check_value[5] + check_value[6]):
                    pass
                    # print('\t\t\t\t', check_value[4] + check_value[5] + check_value[6], ':', xl_status[0] + xl_status[1] + xl_status[2], '<status> WinPts match')
                else:
                    print('\t\t\t', 'DNP Point (', i, ')', check_value[4] + check_value[5] + check_value[6], ':', xl_status[0] + xl_status[1] + xl_status[2], '<status> WinPt does not match the points list. Please refer to the SGConfig.')

        # Analog Point Check
        print('\t\t', 'Analog Points Check')
        for i, record in enumerate(app[6]):
            xl_analog = str(wsheet.cell_value(i + 2, analog_index))
            check_value = record[0].get('Field_Value')
            if check_value[4] == '0':
                if check_value[5] == '0':
                    if xl_analog[0] == (check_value[6]):
                        pass
                        # print('\t\t\t', check_value[6], ':', xl_analog[0], '<analog> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point (', i, ')',
                              '<analog> WinPt does not match the points list. Please refer to the SGConfig.')
                else:
                    if xl_analog[0] + xl_analog[1] == (check_value[5] + check_value[6]):
                        pass
                        # print('\t\t\t', check_value[5] + check_value[6], ':', xl_analog[0] + xl_analog[1],
                        #       '<analog> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point (', i, ')',
                              '<analog> WinPt does not match the points list. Please refer to the SGConfig.')
            else:
                if xl_analog[0] + xl_analog[1] + xl_analog[2] == (
                        check_value[4] + check_value[5] + check_value[6]):
                    pass
                    # print('\t\t\t', check_value[4] + check_value[5] + check_value[6], ':',
                    #       xl_analog[0] + xl_analog[1] + xl_analog[2], '<analog> WinPts match')
                else:
                    print('\t\t\t', 'DNP Point (', i, ')',
                          '<analog> WinPt does not match the points list. Please refer to the SGConfig.')

        # Control Point Check
        print('\t\t', 'Control Points Check')
        for i, record in enumerate(app[4]):
            xl_control = str(wsheet.cell_value(i + 2, control_index))
            check_value = record[0].get('Field_Value')
            if check_value[4] == '0':
                if check_value[5] == '0':
                    if xl_control[0] == (check_value[6]):
                        print('\t\t\t\t', check_value[6], ':', xl_control[0], '<control> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point', i, ':')
                        print('\t\t\t\t',
                              '<control> WinPt does not match the points list. Please refer to the SGConfig.')
                else:
                    if xl_control[0] + xl_control[1] == (check_value[5] + check_value[6]):
                        print('\t\t\t\t', check_value[5] + check_value[6], ':', xl_control[0] + xl_control[1],
                              '<control> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point', i, ':')
                        print('\t\t\t\t',
                              '<control> WinPt does not match the points list. Please refer to the SGConfig.')
            else:
                if xl_control[0] + xl_control[1] + xl_control[2] == (
                                check_value[4] + check_value[5] + check_value[6]):
                    print('\t\t\t\t', check_value[4] + check_value[5] + check_value[6], ':',
                          xl_control[0] + xl_control[1] + xl_control[2], '<control> WinPts match')
                else:
                    print('\t\t\t', 'DNP Point', i, ':')
                    print('\t\t\t\t',
                          '<control> WinPt does not match the points list. Please refer to the SGConfig.')

    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b023_check(app):
    # <app>
    #   <table "B023_CFG">
    #   <table "B023_DEV">
    #   <table "B023_PNT">
    #   <table "B023_POL">

    # Check if Application is Enabled
    if app.get('Enabled') == 'True':
        print('B023 - DNP DCA')
        print('\t', 'B023_PNT')
        b023_pnt_list = []

        for i, record in enumerate(app[2]):
            print('\t\t', i, '-', record[0].get('Field_Value'), ':', record[1].get('Field_Value'))
            b023_pnt_list.append((record[0].get('Field_Value'), record[1].get('Field_Value')))

        print('\t', 'B023_POL')
        b023_pol_list = []
        for i, record in enumerate(app[3]):
            print('\t\t', i, ':')
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
                               int(record[8][0][0][2].get('Field_Value')) + int(record[8][0][0][3].get('Field_Value'))):
                print('\t\t\t\t', b023_pnt_list[index])
            print('\t\t\t', record[8][0][0][4].get('Field_Name'), ':', record[8][0][0][4].get('Field_Value'))
            print('\t\t\t', record[8][0][0][5].get('Field_Name'), ':', record[8][0][0][5].get('Field_Value'))
            for index in range(int(record[8][0][0][4].get('Field_Value')),
                               int(record[8][0][0][4].get('Field_Value')) + int(record[8][0][0][5].get('Field_Value'))):
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
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')
    return