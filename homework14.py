import random
import requests
from pprint import pprint
import csv
import json
import re


# 1.###################################################


def get_quote(index):
    """
    The function returns quote in json format
    :param index: int
    :return: quote
    """
    params = {"method": "getQuote", "format": "json", "key": index}
    r = requests.get('http://api.forismatic.com/api/1.0/', params=params)
    return r.json()


def get_quotes(number):
    """
    The function returns quotes
    :param number: int
    :return: list of dicts
    """
    quotes = []
    while len(quotes) != number:
        quote = get_quote(random.randint(0, 999999))
        if quote['quoteAuthor'] == '' or quote in quotes:
            continue
        else:
            quotes.append(quote)
    return quotes


def write_csv_quotes(quotes, filename='quotes.csv'):
    """
    The function writes sorted quotes by Author in csv format
    """
    fieldnames = ['Author', 'Quote', 'URL']
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        for elements in quotes:
            elements['Author'] = elements['quoteAuthor']
            elements['Quote'] = elements['quoteText']
            elements['URL'] = elements['quoteLink']
        sorted_quotes = sorted(quotes, key=lambda k: k['Author'])
        writer.writerows(sorted_quotes)


file_q = get_quotes(10)
write_csv_quotes(file_q)
pprint(file_q)


# 2.###################################################


def read_json_data(filename='data.json'):
    """
    The function reads json file
    """
    with open(filename, "r") as json_file:
        return json.load(json_file)


new_data = read_json_data()
pprint(read_json_data())


def get_surname(mathematician_dict):
    """
    The function returns surname of mathematician
    """
    return mathematician_dict['name'].split()[-1]


def sorted_by_surname(data):
    """
    The function returns list of dicts sorted by surname
    """
    return sorted(data, key=get_surname)


pprint(sorted_by_surname(new_data))


def get_year_of_death(mathematician_dict):
    """
    The function returns year of death of mathematician
    """
    years = mathematician_dict['years']
    pattern = r"[0-9]+"
    year_of_death = re.findall(pattern, years)
    if years.endswith('BC') or years.endswith('BC.'):
        return -int(year_of_death[-1])
    else:
        return int(year_of_death[-1])


def sorted_by_year_of_death(data):
    """
    The function returns list of dicts sorted by years of death
    """
    return sorted(data, key=get_year_of_death)


pprint(sorted_by_year_of_death(new_data))


def get_text_len(item):
    """
    The function returns the length of text
    """
    text = item['text']
    return len(text.split())


def sorted_by_text_len(data):
    """
    The function returns list of dicts sorted by length of text
    """
    return sorted(data, key=get_text_len)


pprint(sorted_by_text_len(new_data))
