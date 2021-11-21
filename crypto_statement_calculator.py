import csv

class CryptoStatement:
    def __init__(self, file_path:str = None, file_type: str='csv'):
        if not file_path:
            raise Exception('Invalid file path.')

        if file_type == 'csv':
            with open(filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        print(f'Column names are {", ".join(row)}')
                    else:
                        print(f'Rows: {", ".join(row)}')
                    line_count += 1
                print(f'Processed {line_count} lines')
            test = csv
    pass

class CryptoStatementCalculator:
    csv_to_calc = None
    net_gain = 0


    def krakenCalculator(self):

        pass

    pass

filename = './Banffca 2021 YTD/09-11-2021_YTD.csv'
