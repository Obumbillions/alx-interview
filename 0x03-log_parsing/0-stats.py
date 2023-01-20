#!/usr/bin/python3
"""Input stats"""
import sys

stats = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
 t_stats():
    print('File size: {}'.format(sum(si   '405': 0,
    '500': 0
}
sizes = [0]


def prinzes)))
    for s_code, count in sorted(stats.items()):
        if count:
            print('{}: {}'.numerate(sys.stdin, start=1):
        matches = liformat(s_code, count))


try:
    for i, line in ene.rstrip().split()
        try:
            status_code = matches[-2]
            file_size = matches[-1]
            if status_code in stats.keys():
                stats[status_code] += 1
            sizes.append(int(file_size))
        except Exception:
            pass
        if i % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
