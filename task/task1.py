#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    u = set('abcdefghijklmnopqrstuvwxyz')
    a = {'a', 'f', 'i', 'n', 'o'}
    b = {'f', 'g', 'o', 'p', 'z'}
    c = {'i', 'j', 'u', 'w'}
    d = {'f', 'h', 'n', 't', 'u', 'y', 'z'}
    x = b.union(a.intersection(c))
    y = a.intersection(u.difference(b)).union(c.difference(d))
    print(f'x = {x}')
    print(f'y = {y}')