#!/usr/bin/python3

"""
This is a module script that reads stdin line by line and computes metrics

"""


import sys
from collections import defaultdict


def print_statistics(total_size, status_codes):
    """
    Prints statistics based on the total file size and status code counts.

    Args:
        total_size (int): The total size of the files processed.
        status_codes (dict): A dictionary containing counts of each
        status code encountered.

    Returns:
        None
    """
    print(f"Total file size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


def main():
    """
    Main function to read stdin line by line, compute metrics,
    and print statistics.

    Reads input from stdin line by line. For each line,
    it extracts the file size and status code,
    updates the total file size, and increments the count
    for the corresponding status code.
    Every 10 lines or after a keyboard interruption (CTRL + C),
    it prints the total file size
    and the counts of each status code encountered so far, in ascending order.

    Returns:
        None
    """
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) >= 9:
                total_size += int(parts[8])
                status_code = parts[7]
                status_codes[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
