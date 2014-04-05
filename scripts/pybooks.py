#! /usr/bin/env python3
import os
import sys

import requests
import yaml


def get_book_info_from_isbndb(isbn13):
    """
    Get book information from isbndb, using canonical isbn13
    """
    base_url = 'http://isbndb.com/api/v2/yaml/'
    api_key = os.environ.get('ISBNDB_API_KEY')
    full_url = base_url + api_key + '/book/%s' % isbn13

    ret = requests.get(full_url)
    ret_data = yaml.load(ret.text)
    if ret_data == {}: return None
    ret_data_core = ret_data.get('data')[0]
    return ret_data_core


if __name__ == '__main__':
    isbn13 = sys.argv[1]
    book_info = get_book_info_from_isbndb(isbn13)
    print(book_info)
