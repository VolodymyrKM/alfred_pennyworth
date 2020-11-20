import argparse
from datetime import datetime, timezone
import os
from typing import List

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Stored all information into one file in input years range')

    parse.add_argument('-s', '--start_year', required=False,
                       help='Setting year to begin with.',
                       type=int, dest='start_year')

    parse.add_argument('-e', '--end_year', required=False,
                       help='Setting year as end point.',
                       type=int, dest='end_year')

    parse.add_argument('-p', '--pass', help='path to source',
                       required=True, dest='path_to_source')

    parse.add_argument('-d', '--destination', help='Path to folder', required=False,
                       default='/beer_review')

    parse.add_argument('-df', '--def_file', required=False,
                       dest='file_name')

    args = parse.parse_args()


    def default_start_year() -> int:
        '''setting the min value if the user don't input such value himself'''
        min_num_f = min([i.strip('.csv')[:4] for i in os.listdir(args.path_to_source)])
        return int(min_num_f)



    if not args.start_year:
        args.start_year = default_start_year()
        print(args.start_year)

    def default_end_year() -> int:
        '''setting the max value if the user don't input such value himself'''
        max_num_f = max([i.strip('.csv')[:4] for i in os.listdir(args.path_to_source)])
        return int(max_num_f)


    if not args.end_year:
        args.end_year = default_end_year()
        print(args.end_year)

    def file_name() -> str:
        '''setting the name of the file in witch will be stored info'''
        return (f'{args.start_year}-{args.end_year}_{datetime.now(timezone.utc).strftime("%d-%m-%Y-%H_%M")}_utc.csv')


    if not args.file_name:
        args.file_name = file_name()
    print(args.end_year)


    def data_file_list() -> List[str]:
        '''sorting files according to the range which was defined by value'''
        file_list = [i for i in os.listdir(args.path_to_source) if args.end_year >= int(i[:4]) >= args.start_year]
        return file_list
    print(data_file_list())

    def write_file(file_name: str) -> None:
        '''Open the file in the set value and write the into to one file named according to the task'''
        for reed_file in data_file_list():
            with open(f'{args.path_to_source}/{reed_file}', 'r', encoding='utf - 8') as file:
                with open(file_name, 'a', encoding='utf - 8') as file_1:
                    for row in file.readlines():
                        if 'brewery_name' in row:
                            continue
                        file_1.writelines(row)
    write_file(args.file_name)
