#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    flights = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            dst = input("What destination do you need? ")
            nmb = int(input("Which number of the flight do you need? "))
            tpe = input("Which type of plane do you need? ")
            flight = {
                'destination': dst,
                'number_flight': nmb,
                'type_plane': tpe,
            }
            flights.append(flight)
            if len(flights) > 1:
                flights.sort(key=lambda item: item.get('destination', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 18
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^18} |'.format(
                    "№",
                    "Destination",
                    "Number of the flight",
                    "Type of the plane"
                )
            )
            print(line)
            for idx, flight in enumerate(flights, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>18} |'.format(
                        idx,
                        flight.get('destination', ''),
                        flight.get('number_flight', ''),
                        flight.get('type_plane', 0)
                    )
                )
            print(line)

        elif command.startswith('select'):
            t = input("choose type of the plane: ")
            count = 0
            for flight in flights:
                if flight.get('type_plane') == t:
                    count += 1
                    print(
                        '{:>4}: {} {}'.format(
                            count,
                            flight.get('destination', ''),
                            flight.get("number_flight")
                        )
                    )
            if count == 0:
                print("We couldn't find this type of plane")
        elif command == 'help':
            print("command list:\n")
            print("add - add information about a flight;")
            print("list - display the flight schedule;")
            print("select <type> - select the type of the plane;")
            print("help - show reference;")
            print("exit - leave a program.")
        else:
            print(f"unknown command {command}", file=sys.stderr)
