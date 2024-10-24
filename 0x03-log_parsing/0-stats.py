#!/usr/bin/python3
import sys
import signal


total = 0
s_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
l_count = 0


def print_stats():
    global total
    global s_code

    print(f"File size: {total}")
    for code in sorted(s_code.keys()):
        if s_code[code] > 0:
            print(f"{code}: {s_code[code]}")


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    l_count += 1
    try:
        parts = line.split()
        if len(parts) < 7:
            continue

        ip_address = parts[0]
        date = parts[3][1:]
        request = parts[5] + ' ' + parts[6] + ' ' + parts[7]
        status_code = int(parts[8])
        file_size = int(parts[9])

        if request != '"GET /projects/260 HTTP/1.1"':
            continue

        total += file_size

        if status_code in s_code:
            s_code[status_code] += 1

    except (IndexError, ValueError):
        continue

    if l_count % 10 == 0:
        print_stats()

print_stats()
