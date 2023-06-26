import convertjson


def test_dict():
    file = 'C:/Users/QL725WY/OneDrive - EY/Desktop/practice/tesjson.json'
    assert convertjson.read_json_file(file) == """{'fields': {'codename': 'add_logentry',
            'content_type': 8,
            'name': 'Can add log entry'},
 'model': 'auth.permission',
 'pk': 22}"""

    # assert convertjson.read_json_file(file) != 'abc.json'
    # assert convertjson.read_json_file(file) == ''
    # assert convertjson.read_json_file(None) == ''

'''@pytest.mark.parametrize("data, expected", [((2, 3, 1, 4, 6), 1),
    ((5, -2, 0, 9, 12), -2), ((200, 100, 0, 300, 400), 0)])

def twosum_test(data,expected):
    val = twosumpg.twoSum(data)
    assert val == expected'''

