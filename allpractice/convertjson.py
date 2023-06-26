import errno
import json
import os
import logging
import pandas as pd

filename = 'C:/Users/QL725WY/OneDrive - EY/Desktop/practice/article.json'
tgtfile = 'C:/Users/QL725WY/OneDrive - EY/Desktop/practice/article.csv'


def read_json_file(filename):
    readjson = dict()
    try:
        with open(filename, 'r') as f:
            readjson = json.loads(f.read())
    except:
        print(f"finame {filename} having error")
    print(readjson)
    return readjson


def normalize_json(read_json_data):
    new_data = dict()
    for key, value in read_json_data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + '_' + k] = v
    print(new_data)
    return new_data


def write_json_in_csv(df, tgtfile):
    return df.to_csv(tgtfile)


if __name__ == '__main__':
    try:
        if filename != '':
            readjsondata = read_json_file(filename)
            logging.debug()
            cleanjson = normalize_json(readjsondata)
            df = pd.DataFrame([cleanjson])
            write_json_in_csv(df, tgtfile)
    except:
        raise "File is null"
