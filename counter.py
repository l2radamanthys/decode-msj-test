#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io

def main():
    keys = {};
    data = io.open('message.txt', mode='r', encoding='utf-8').readlines()[0]
    for char_ in data.replace(' ', ''):
        print(char_, char_ in keys)
        if char_ in keys:
            keys[char_] += 1
        else:
            keys[char_] = 1
    print(data)
    print(keys, len(keys))


main()