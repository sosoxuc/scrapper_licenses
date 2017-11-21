import os
import pysftp


class Parser:
    def __init__(self, config, schema, rows=None):
        self.config = config
        self.rows = rows
        self.schema = schema
        self.dir = config['download_path']

    def upload(self, file_path):
        """SFTP upload"""
        print('Uploading %s' % file_path)
        sftp = pysftp.Connection(host=self.config['upload_addr'],
                                 username=self.config['upload_user'])
        with sftp.cd(self.config['upload_root']):
            path = self.config['upload_path']
            if not sftp.exists(path):
                sftp.mkdir(path)
            with sftp.cd(path):
                sftp.put(file_path)
        sftp.close()
        if self.config['remove_temp']:
            os.remove(file_path)

    def parse(self):
        """Parse files"""
        result = []
        for item in self.schema:
            if not os.path.exists(item['file_path']):
                continue
            out_folder = os.path.join(self.dir, 'parsed')
            if not os.path.exists(out_folder):
                os.makedirs(out_folder)
            out = os.path.join(out_folder, item['CSV File Output Name'])
            if out not in result:
                result.append(out)
                if os.path.exists(out):
                    os.remove(out)
            with open(item['file_path'], 'rb') as infile:
                # Open write with append
                with open(out, 'wb+') as outfile:
                    # Remove header
                    header = item['Header Included? Y/N'] == 'Y'
                    for line in infile:
                        if header:
                            header = False
                            continue
                        outfile.write(line)
            if self.config['remove_temp']:
                os.remove(item['file_path'])
        for item in result:
            self.upload(item)
        return result
