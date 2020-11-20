import argparse
import csv
from typing import List
import time

parser = argparse.ArgumentParser(description='This is a very useful script. It will help you '
                                             'to find some interesting info about beer')

parser.add_argument('-p', '--path', required=True, dest='path')

parser.add_argument('-bt', '--beer_type', required=False,
                    help='Find most favorite beer type', action='store_true')

parser.add_argument('-bn', '--beer_name', required=False,
                    help='Find most favorite beer name', action='store_true')

parser.add_argument('-dr', '--day_of_review', required=False,
                    help='Find day with they most number of review', action='store_true')

parser.add_argument('-r', '--reviewer', required=False,
                    help='Show number of reviews for reviewer', action='store_true')

args = parser.parse_args()
print(args)


def read_beer_csv() -> List[dict]:
    '''create the dictionary with the beer info data'''
    beer_list = []
    with open(args.path, 'r', encoding='utf - 8') as file:
        for row in csv.reader(file):
            data_beer_dict = {}
            if 'brewery_name' in row:
                continue
            data_beer_dict['brewery_name'] = row[0]
            data_beer_dict['review_time'] = row[1]
            data_beer_dict['review_overall'] = row[2]
            data_beer_dict['review_aroma'] = row[3]
            data_beer_dict['review_profilename'] = row[4]
            data_beer_dict['beer_style'] = row[5]
            data_beer_dict['review_taste'] = row[6]
            data_beer_dict['beer_name'] = row[7]
            data_beer_dict['beer_beerid'] = row[8]
            beer_list.append(data_beer_dict)
    return beer_list


def top_day_review() -> None:
    dict_days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    days_list = [0, 0, 0, 0, 0, 0, 0]
    for i in read_beer_csv():
        week_day = time.gmtime(float(i['review_time'])).tm_wday
        days_list[week_day] += 1
    max_week_day = max(days_list)
    index_day = days_list.index(max_week_day)
    print(
        f'the most times reviewing of the all kinds of beers was {dict_days[index_day]}, there are {max_week_day} times ')


def number_of_reviews() -> None:
    dict_total_times = {}
    for name in read_beer_csv():
        if name['review_profilename'] in dict_total_times:
            dict_total_times[name['review_profilename']] += 1
        else:
            dict_total_times[name['review_profilename']] = 1
    for reviewer, num in dict_total_times.items():
        print(f'The number of reviews <{num}> for reviewer: <{reviewer}> ')


def find_info_beer(type_beer_name) -> None:
    '''Find the best type or name beer by calculation review time of all beer names separated from each other and find the
greatest number witch defined best type'''
    dict_total_score_beer = {}
    for beer in read_beer_csv():
        score = [float(j['review_overall']) for j in read_beer_csv() if j[type_beer_name] == beer[type_beer_name]]
        score = sum(score) / len(score)
        if beer['beer_style'] in dict_total_score_beer:
            continue
        dict_total_score_beer[score] = beer[type_beer_name]
    winner_beer_type = max([i for i in dict_total_score_beer])
    if dict_total_score_beer.keys() == 'beer_style':
        type_or_name = 'type'
    else:
        type_or_name = 'name'
    print(f'The most favorite bear {type_or_name} is <{dict_total_score_beer[winner_beer_type]}>')


if args.beer_type:
    find_info_beer('beer_style')

if args.beer_name:
    find_info_beer('beer_name')

if args.day_of_review:
    top_day_review()

if args.reviewer:
    number_of_reviews()