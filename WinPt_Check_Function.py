import xml.etree.ElementTree as ET
import xlrd
import os

def winpt_check(xcel_filename, directory, app):

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

        # Counters for WinPt status printing
        status_count = 0
        analog_count = 0
        control_count = 0

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
                        print('\t\t\t', 'DNP Point (', i, ')', check_value[6], ':', xl_status[0],
                              '<status> WinPt does not match the points list. Please refer to the SGConfig.')
                        status_count = status_count + 1  # Indicates that a status WinPt does not match
                else:
                    if xl_status[0] + xl_status[1] == (check_value[5] + check_value[6]):
                        pass
                        # print('\t\t\t\t', check_value[5] + check_value[6], ':', xl_status[0] + xl_status[1], '<status> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point (', i, ')', check_value[5] + check_value[6], ':',
                              xl_status[0] + xl_status[1],
                              '<status> WinPt does not match the points list. Please refer to the SGConfig.')
                        status_count = status_count + 1  # Indicates that a status WinPt does not match
            else:
                if xl_status[0] + xl_status[1] + xl_status[2] == (check_value[4] + check_value[5] + check_value[6]):
                    pass
                    # print('\t\t\t\t', check_value[4] + check_value[5] + check_value[6], ':', xl_status[0] + xl_status[1]
                    #      + xl_status[2], '<status> WinPts match')
                else:
                    print('\t\t\t', 'DNP Point (', i, ')', check_value[4] + check_value[5] + check_value[6], ':',
                          xl_status[0] + xl_status[1] + xl_status[2],
                          '<status> WinPt does not match the points list. Please refer to the SGConfig.')
                    status_count = status_count + 1  # Indicates that a status WinPt does not match

        # If all status WinPts match, print statement
        if status_count == 0:
            print('\t\t\t', 'All <status> WinPts match.')
        else:
            pass

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
                        analog_count = analog_count + 1  # Indicates that an analog WinPt does not match
                else:
                    if xl_analog[0] + xl_analog[1] == (check_value[5] + check_value[6]):
                        pass
                        # print('\t\t\t', check_value[5] + check_value[6], ':', xl_analog[0] + xl_analog[1],
                        #       '<analog> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point (', i, ')',
                              '<analog> WinPt does not match the points list. Please refer to the SGConfig.')
                        analog_count = analog_count + 1  # Indicates that an analog WinPt does not match
            else:
                if xl_analog[0] + xl_analog[1] + xl_analog[2] == (
                                check_value[4] + check_value[5] + check_value[6]):
                    pass
                    # print('\t\t\t', check_value[4] + check_value[5] + check_value[6], ':',
                    #       xl_analog[0] + xl_analog[1] + xl_analog[2], '<analog> WinPts match')
                else:
                    print('\t\t\t', 'DNP Point (', i, ')',
                          '<analog> WinPt does not match the points list. Please refer to the SGConfig.')
                    analog_count = analog_count + 1  # Indicates that an analog WinPt does not match

        # If all analog WinPts match, print statement
        if analog_count == 0:
            print('\t\t\t', 'All <analog> WinPts match.')
        else:
            pass

        # Control Point Check
        print('\t\t', 'Control Points Check')
        for i, record in enumerate(app[4]):
            xl_control = str(wsheet.cell_value(i + 2, control_index))
            check_value = record[0].get('Field_Value')
            if check_value[4] == '0':
                if check_value[5] == '0':
                    if xl_control[0] == (check_value[6]):
                        pass
                        # print('\t\t\t\t', check_value[6], ':', xl_control[0], '<control> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point', i,
                              '<control> WinPt does not match the points list. Please refer to the SGConfig.')
                        control_count = control_count + 1  # Indicates that a control WinPt does not match
                else:
                    if xl_control[0] + xl_control[1] == (check_value[5] + check_value[6]):
                        pass
                        # print('\t\t\t\t', check_value[5] + check_value[6], ':', xl_control[0] + xl_control[1],
                        #       '<control> WinPts match')
                    else:
                        print('\t\t\t', 'DNP Point', i,
                              '<control> WinPt does not match the points list. Please refer to the SGConfig.')
                        control_count = control_count + 1  # Indicates that a control WinPt does not match
            else:
                if xl_control[0] + xl_control[1] + xl_control[2] == (
                                check_value[4] + check_value[5] + check_value[6]):
                    pass
                    # print('\t\t\t\t', check_value[4] + check_value[5] + check_value[6], ':',
                    #       xl_control[0] + xl_control[1] + xl_control[2], '<control> WinPts match')
                else:
                    print('\t\t\t', 'DNP Point', i,
                          '<control> WinPt does not match the points list. Please refer to the SGConfig.')
                    control_count = control_count + 1  # Indicates that a control WinPt does not match

        # If all control WinPts match, print statement
        if control_count == 0:
            print('\t\t\t', 'All <control> WinPts match.')
        else:
            pass
    except Exception:
        print('\t\t\t', 'Error: Cannot find the file.')
