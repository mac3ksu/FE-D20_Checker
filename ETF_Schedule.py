import os
import xlrd
from datetime import date

def date_convert(row, col):
    try:
        date_tuple = xlrd.xldate_as_tuple(float(wsheet.cell_value(row, col)), 0)
        date_string = str(date_tuple[0]) + '-' + str(date_tuple[1]) + '-' + str(date_tuple[2])
    except:
        date_string = 'null'
    return date_string

if __name__ == '__main__':
    #directory = 'Z:\Clients\TND\FirstEnr\82568_EtfScadaSupprt\Design\Substation Projects\SCADA TRACKER AND P6 LATEST'
    directory = os.path.expanduser(os.path.join('~', 'Desktop'))

    for thing in os.listdir(directory):
        if 'SCADA TRACKING' in thing:
            filename = thing

    filepath = directory + '/' + filename

    wbook = xlrd.open_workbook(filepath)

    wsheet_name = ''

    for sheet in wbook.sheet_names():
        if 'EtF Projects' in sheet:
            wsheet_name = sheet

    wsheet = wbook.sheet_by_name(wsheet_name)

    for i, cell in enumerate(wsheet.row(0)):
        if cell.value == 'RTU Config Engineer':
            engineer_rtu_index = i
        elif cell.value == 'Project Description':
                desc_index = i
        elif 'Adina' in cell.value:
            date_config_q6_index = i
        elif 'Q4' in cell.value:
            date_config_q4_index = i
        elif cell.value == 'Configs Due On FE Network On or Before':
            date_config_network_index = i
        elif cell.value == 'RTU Config Upload':
            date_rtu_upload_index = i
        elif cell.value == 'Sub':
            sub_name_index = i
        elif cell.value == 'Configs Uploaded on FE Network for Testers':
            date_config_uploaded_tester = i
        elif cell.value == 'Network #':
            network_po_index = i

    engineer_list = ['Marshall', ]#'Zack', 'Adina', 'Ian', 'Scott']
    for engineer_rtu in engineer_list:
        outfile_name = date.today().strftime('%Y_%m_%d') + '_' + engineer_rtu + '_Config_Dates.csv'
        desktop = os.path.expanduser(os.path.join('~', 'Desktop'))
        outfile = desktop + '/' + outfile_name

        with open(outfile, 'w') as output_file:
            output_file.write(filename + '\n')
            output_file.write('Network #,Site,Project Description,Engineer,Q4 Date,Q6 Date,Tester Upload,RTU Config Upload\n')
            for i, cell in enumerate(wsheet.col(engineer_rtu_index)):
                if engineer_rtu in cell.value:
                    #print(wsheet.cell_value(i, sub_name_index))
                    #print(date_convert(i, date_rtu_upload_index))
                    output_file.write('{},{},{},{},{},{},{},{}\n'.format(wsheet.cell_value(i, network_po_index),
                                                                    wsheet.cell_value(i, sub_name_index),
                                                                    wsheet.cell_value(i, desc_index),
                                                                    wsheet.cell_value(i, engineer_rtu_index),
                                                                    date_convert(i, date_config_q4_index),
                                                                    date_convert(i, date_config_q6_index),
                                                                    date_convert(i, date_config_uploaded_tester),
                                                                    date_convert(i, date_rtu_upload_index)
                                                                    )
                                      )
