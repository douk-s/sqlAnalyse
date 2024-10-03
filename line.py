import re
import os

def cresql(sql_data):
    with open('script.sql', 'w', encoding='utf-8') as file:
        for name in sql_data:
            # Ö±½ÓÐ´Èë×Ö·û´®
            file.write(name + '\n')

def createLine(table_name):
    results = []
    found_copy = False
    with open('dump.sql', 'r', encoding='utf-8') as file:
        pattern = re.compile(r'CREATE TABLE.*' + table_name + ' ')
        for line_number, line in enumerate(file, start=1):
            # sys.stdout.flush()
            # sys.stdout.write(f'\rline: {line_number}')
            if pattern.search(line):
                found_copy = True

            if found_copy:
                results.append(line.strip())
                print(line.strip())
            if line.strip() == r');':
                found_copy = False
    return results

def copyLine(table_name):
    results = []
    found_copy = False
    with open('dump.sql', 'r', encoding='utf-8') as file:
        pattern = re.compile(r'COPY.*' + table_name + ' ')
        for line_number, line in enumerate(file, start=1):
            # sys.stdout.flush()
            # sys.stdout.write(f'\rline: {line_number}')
            if pattern.search(line):
                found_copy = True

            if found_copy:
                results.append(line.strip())
                print(line.strip())
            if line.strip() == r'\.':
                found_copy = False
    return results
