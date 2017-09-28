#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re

with open('text.srt', 'r', encoding='utf-8') as source_file:
    file_by_lines = source_file.readlines()
    with open('clean_text.txt', 'w', encoding='utf-8') as result_file:

        for line in file_by_lines:
            match_sub_index = re.search(r'^[0-9]*$', line)
            match_time = re.search(r'^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d$', line)
            if match_sub_index:
                pass
            elif match_time:
                pass
            else:
                print(re.sub(r'<[a-zA-Z0-9#="/ ]*>', '', line))
                result_file.write(re.sub(r'<[a-zA-Z0-9#="/ ]*>', '', line))
