import xml.etree.ElementTree as ET
import xlrd
import os


def set_comlist():
  global b013_com_list # Needed to modify global copy of b013_comlist
  b013_com_list = []

def winpt_check(xcel_filename, directory, app, column, table_num, type):
    # xcel_filename - for the purpose of finding/opening the excel template file
    # directory - the path to get to the excel template file
    # app - the application currently in use
    # column - which column in the excel template you are wanting to check
    # table_num - which table in the SGConfig you are wanting to check
    # type - string value to indicate which type of point you are wanting to check

    try:
        # Counters for WinPt status printing
        count = 0

        filepath = directory + '/' + xcel_filename

        wbook = xlrd.open_workbook(filepath)

        for sheet in wbook.sheet_names():
            if 'Sheet1' in sheet:
                wsheet_name = sheet

        wsheet = wbook.sheet_by_name(wsheet_name)

        # General Point Check
        print('\t\t', type, 'Points Check')
        for i, record in enumerate(app[table_num]):
            xl_value = str(wsheet.cell_value(i + 2, column))
            check_value = record[0].get('Field_Value')
            if record[0].get('Field_Value') == '(______) Undefined':
                print('\t\t\t', 'DNP Point', i, '<', type, '> Point is undefined.')
            elif str(wsheet.cell_value(i+2, 1)) == '':
                print('\t\t\t', 'DNP Point', i, ': More SGConfig <', type, '> points than excel template <', type, '> points.')
                print('\t\t\t\t', 'Please match the number of excel points to the SGConfig.')
                break
            else:
                if check_value[4] == '0':
                    if check_value[5] == '0':
                        if xl_value[0] == (check_value[6]):
                            pass
                        else:
                            print('\t\t\t', 'DNP Point', i, '<',
                                  type, '> WinPt does not match the points list. Please refer to the SGConfig.')
                            count = count + 1  # Indicates that a WinPt does not match
                    else:
                        if xl_value[0] + xl_value[1] == (check_value[5] + check_value[6]):
                            pass
                        else:
                            print('\t\t\t', 'DNP Point', i, '<',
                                  type, '> WinPt does not match the points list. Please refer to the SGConfig.')
                            count = count + 1  # Indicates that a WinPt does not match
                else:
                    if xl_value[0] + xl_value[1] + xl_value[2] == (check_value[4] + check_value[5] + check_value[6]):
                        pass
                    else:
                        print('\t\t\t', 'DNP Point', i, '<',
                                  type, '> WinPt does not match the points list. Please refer to the SGConfig.')
                        count = count + 1  # Indicates that a WinPt does not match

        # If all WinPts match, print statement
        if count == 0:
            print('\t\t\t', 'All <', type, '> WinPts match.')
        else:
            pass

    except Exception:
        pass

def d20mpp_check(xml_filename, directory):
    tree = ET.parse(os.path.join(directory, xml_filename))
    root = tree.getroot()

    # with open(os.path.join(directory, xml_filename[:-4]+'_Check.txt')) as of:
    print(root[0][0][1][0].get('Part_Number'))
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
    # Check Point Type
    # Check System Point
    # Check Comm Event Point
    # Check Normal State

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

        # Check SOE Enable
        # Check COS Enable

        print('\t', app[2].get('Table_Identifier'), ':', app[2].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[2]):
            print('\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
            print('\t\t', record[2].get('Field_Name'), ':', record[2].get('Field_Value'))
            if record[1].get('Field_Value') == record[2].get('Field_Value'):
                print('\t\t', '** These values are not supposed to be the same. See the SGConfig. **')
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
        try:
            app[2][0].get('Record_Number')
            # Loop Through the Table
            for i, record in enumerate(app[2]):
                print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
                print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
        except IndexError:
            print('\t\t', '<no entries>')


        print('\t', app[3].get('Table_Identifier'), ':', app[3].get('Table_Name'), 'Table')
        try:
            app[3][0].get('Record_Number')
            # Loop Through the Table
            for i, record in enumerate(app[3]):
                print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
                print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
        except IndexError:
            print('\t\t', '<no entries>')
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def a083_check(app):
    # Check That All Points Have Event Types = Both

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))
        print('\t D20 Calculator does not have event types')
        # for record in app[2][0]:
        #     print('\t Calc', record.get('Record_Number'))
        #     print('\t Calc', record.get('Record_Number'), '-', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b003_check(app):
    # The XML export does not contain the report deadband.

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))
        print('\t', 'Report Deadband not in XML')
        return
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

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
            print('\t\t\t', record[1].get('Field_Name'), ':', record[1].get('Field_Value'))
            print('\t\t\t', record[3].get('Field_Name'), ':', record[3].get('Field_Value'))
            print('\t\t\t', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))
            print('\t\t\t', record[5].get('Field_Name'), ':', record[5].get('Field_Value'))
            print('\t\t\t', record[6].get('Field_Name'), ':', record[6].get('Field_Value'))
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

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        print('\t', app[1].get('Table_Identifier'), ':', app[1].get('Table_Name'))
        # Loop Through the Table
        for i, record in enumerate(app[1]):
            print('\t\t', record[0].get('Field_Name'), ':', record[0].get('Field_Value'))
            print('\t\t', record[4][0][0][0].get('Field_Name'), ':', record[4][0][0][0].get('Field_Value'))

        # Check the Standard UTC Offset
        # Check the DST Offset

        print('\t', app[4].get('Table_Identifier'), ':', app[4].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[4]):
            print('\t\t', record[11].get('Field_Name'), ':', record[11].get('Field_Value'))
            print('\t\t', record[12].get('Field_Name'), ':', record[12].get('Field_Value'))

        # Check User Name = something
        # Check Password = something
        # Check Control Password = something

        print('\t', app[2].get('Table_Identifier'), ':', app[2].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[2]):
            print('\t\t', record[5].get('Field_Name'), ':', record[5].get('Field_Value'))
            print('\t\t', record[6].get('Field_Name'), ':', record[6].get('Field_Value'))
            print('\t\t', record[7].get('Field_Name'), ':', record[7].get('Field_Value'))

        # Check Welcome Message for Field Value 15

        print('\t', app[5].get('Table_Identifier'), ':', app[5].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[5]):
            print('\t\t', '(', i+1,')', record[3].get('Field_Name'), ':', record[3].get('Field_Value'))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b015_check(app):
    # Check Bridgeman app

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        # Count the number of remote DNP devices
        num_dnp_dev = 0
        for record in app[2][0]:
            num_dnp_dev += 1
        print('\t', num_dnp_dev, 'remote DNP devices')
        print('\t', app[0][0][1].get('Field_Name'), ':', app[0][0][1].get('Field_Value'))

        print('\t', 'Local Application Table [LAN Address(Hex), Data Link Channel]')
        # Loop Through the Table
        for i, record in enumerate(app[2]):
            print('\t\t', record[0].get('Field_Value'), '(x', record[3].get('Field_Value'), ')',
                  record[2].get('Field_Value'), ':', b013_com_list[i])

        print('\t', 'Remote Application Table [LAN Address(Hex), Data Link Channel]')
        # Check TXT Delay to Appl.
        # Loop Through the Table
        for record in app[3]:
            print('\t\t', record[0].get('Field_Value'), '(x', record[3].get('Field_Value'), ')',
                  record[2].get('Field_Value'), '   ', record[4].get('Field_Name'), ':', record[4].get('Field_Value'))
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b021_check(app):
    # Check Datalink Confirm
    # Check Idle Report Period

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))

        print('\t', app[0].get('Table_Identifier'), ':', app[0].get('Table_Name'), 'Table')
        # Loop Through the Table
        for i, record in enumerate(app[0]):
            print('\t\t', i, ':')
            print('\t\t\t', record[14].get('Field_Name'), ':', record[14].get('Field_Value'))
            print('\t\t\t', record[11].get('Field_Name'))
            print('\t\t\t\t', record[11][0][0][5].get('Field_Name'), ':', record[11][0][0][5].get('Field_Value'))

        # Compare the Winpoints from the points list to what's programmed in the D20

        # Put in the path to the excel template file
        directory = os.path.expanduser(
            os.path.join('~', 'Documents', 'GitHub', 'FE-D20_Checker', 'Example D20 XML', 'D20MEII'))

        # Determine that the XCEL template's filename is D20 DNP Map WinPt Check
        for thing in os.listdir(directory):
            if 'D20 DNP Map WinPt Check' in thing:
                xcel_filename = thing
                print('\t', xcel_filename)

            try:
                filepath = directory + '/' + xcel_filename

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

            except Exception:
                print('\t\t\t', 'Error: Cannot find the file.')

        # Call the WinPt check function
        winpt_check(xcel_filename, directory, app, status_index, 3, 'Status')
        winpt_check(xcel_filename, directory, app, analog_index, 6, 'Analog')
        winpt_check(xcel_filename, directory, app, control_index, 4, 'Control')

    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')

def b023_check(app):
    # <app>
    #   <table "B023_CFG">
    #   <table "B023_DEV">
    #   <table "B023_PNT">
    #   There is no B023_POL

    # Check if the Application is Enabled
    if app.get('Enabled') == 'True':
        print(app.get('Application_Identifier'), '-', app.get('Application_Name'))
        print('\t', app[2].get('Table_Identifier'))
        b023_pnt_list = []

        # Loop Through the Table
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

        print('\t', app[1].get('Table_Identifier'))
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

        print('\t', app[0].get('Table_Identifier'))
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
    else:
        print(app.get('Application_Identifier'), '-', 'is disabled')


