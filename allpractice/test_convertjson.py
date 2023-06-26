import unittest
import pandas as pd
import convertjson


file = 'C:/Users/QL725WY/OneDrive - EY/Desktop/practice/tesjson.json'
file1 = 'C:/Users/QL725WY/OneDrive - EY/Desktop/practice/tes2json.json'
file3 = 'C:/Users/QL725WY/OneDrive - EY/Desktop/practice/tes3json.json'


class TestConvert(unittest.TestCase):

    def test_read_json_file(self):
        dcc = {'pk': 22, 'model': 'auth.permission',
               'fields': {'codename': 'add_logentry', 'name': 'Can add log entry', 'content_type': 8}}
        assert convertjson.read_json_file(file) == {}
        assert convertjson.read_json_file(file1) == dcc
        # assert convertjson.read_json_file(file3) == False

    def test_normalize_json(self):
        dcc = {'pk': 22, 'model': 'auth.permission',
               'fields': {'codename': 'add_logentry', 'name': 'Can add log entry', 'content_type': 8}}
        dcc2 = {'pk': 22, 'model': 'auth.permission', 'fields_codename': 'add_logentry',
                'fields_name': 'Can add log entry'}
        dcc4 = {'pk': 22, 'model': 'auth.permission', 'fields_codename': 'add_logentry',
                'fields_name': 'Can add log entry', 'fields_content_type': 8}
        dcc3 = {}
        dcc6 = {'pk': 22, 'model': 'auth.permission'}
        dcc7 = {'pk': 22, 'model': 'auth.permission'}
        a = convertjson.normalize_json(dcc3)
        self.assertEqual(a, {})
        assert convertjson.normalize_json(dcc) != dcc2
        assert convertjson.normalize_json(dcc) == dcc4
        assert convertjson.normalize_json(dcc6) == dcc7

    def test_write_json_in_csv(self):
        tgtfile = 'C:/Users/QL725WY/OneDrive - EY/Desktop/practice/test.csv'
        df = pd.DataFrame()
        df1 = pd.DataFrame()
        # assert convertjson.write_json_in_csv(df, tgtfile)=

    if __name__ == '__main__':
        unittest.main()
