import os
import csv
import xlrd
import shutil
from urllib import request
from contextlib import closing


class Source:

    def __init__(self, config, schema):
        """Init Config and Schema"""
        self.config = config
        self.schema = schema
        self.dir = config['download_path']

    def file_save(self, url):
        """Download file from FTP"""
        file_name = url.split('/')[-1]
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        print('Loading %s' % file_name)
        # Download from ftp
        file_path = os.path.join(self.dir, file_name)
        with closing(request.urlopen(url)) as r:
            with open(file_path, 'wb') as f:
                shutil.copyfileobj(r, f)
        return file_path

    def get_all(self):
        """Download all files from FTP"""
        for item in self.schema:
            file_path = self.file_save(item['link to data'])

            # In case of xls convert to csv
            if file_path.endswith('.xls'):
                wb = xlrd.open_workbook(file_path)
                sh = wb.sheet_by_index(0)
                file_orig = file_path
                file_path = file_path.replace('.xls', '.csv')
                csv_file = open(file_path, 'w')
                wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for row in range(sh.nrows):
                    data  = sh.row_values(row)
                    wr.writerow(data)
                csv_file.close()
                if self.config['remove_temp']:
                    os.remove(file_orig)

            item['file_path'] = file_path
        return self.schema
