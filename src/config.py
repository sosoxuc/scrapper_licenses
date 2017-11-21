from openpyxl import load_workbook


class Config():
    def __init__(self):
        pass

    @staticmethod
    def get():
        return {
            'download_path': '/media/soso/7cb3c38d-2304-46f7-aa2e-26e1ff598a1b/downloads/',
            'upload_addr': 'os.uploads.ing.enigma.com',
            'upload_user': 'kkuloshvili',
            'upload_pass': '',
            'upload_root': 'uploads',
            'upload_path': 'licenses',
            'remove_temp': False,
        }

    @staticmethod
    def read_schema():
        """Read data dictionary from excel file and load in dictionary as a list"""
        schema = []
        wb = load_workbook('../schema/schema.xlsx')
        # Traverse worksheets
        worksheet = wb.worksheets[0]
        title_row = None
        for row in worksheet:
            if not title_row:
                title_row = row
                continue
            item = {}
            # Traverse cells
            for cell in row:
                key = title_row[cell.col_idx - 1].value
                value = cell.value
                if not key and not value:
                    continue
                # Save in dictionary
                item[key] = value
            # Add to schema
            if item['link to data']:
                schema.append(item)
        return schema
