#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dumps last rolls to a CSV file, example usage:
```
./roll2csv --address 0x706a62cae6c65472cce04a8d013156d071f8c998 --csv rolls.csv
```
Results example:
```
Transaction hash,Date time,Bet size,Roll under
0x5ccf0ee807ddbecfbfc8355478a7dfb0f562ac8f7d1a89e7699c3d9d17909120,4864-12-05 15:17:44,0.19,2
0x51ca16cb583e7a9200524c8b34e89bbc543bb11f890811721e1948fd77b7c555,4864-12-05 15:15:17,0.1,3
0xf932cd98955b3deb0fb96075c9f109455c3d763f75468655ddfe6d5d0fa951ba,4864-12-05 15:12:41,0.1,3
0x4c93791068933692bd1f85cf8cba0bb0d7fdd78f9d5a457752243e0ec358a747,4864-12-05 14:42:56,0.5,12
0x84809637b0f796bb53be439107557698bf7a09cfedb4286ff11f470340a24ee1,4864-12-05 14:41:58,0.5,3
0x88a2429790e10f81136df14da4b8d6595e6de7e6a94bb3f8d8e92d42965100a2,4864-12-05 14:39:16,0.5,3
0x30a914c957750c22e3005e5028531c2799175741c10d660733ef3b1a66bf9740,4864-12-05 14:21:52,0.5,3
0x3d1d8b57a4c95ea0dab95c274fc5ebd47f8b8abc59ea54800db69c4b44a83b6a,4864-12-05 14:21:13,2.0,7
0x3ca253933a9a51f7d4e6f7ec718f83bed1b213a60cc37188a897686f46efb38c,4864-12-05 14:17:28,2.0,11
```
"""
import argparse
import csv

from pyetheroll.etheroll import Etheroll


def parse_arg():
    parser = argparse.ArgumentParser(description='Dumps player rolls to CSV')
    parser.add_argument('--address', help='Player address', required=True)
    parser.add_argument('--csv', help='CSV output file', required=True)
    return parser.parse_args()


def get_last_bets_transactions(address):
    etheroll = Etheroll()
    return etheroll.get_last_bets_transactions(address)


def dump_rolls(rolls, filename):
    with open(filename, mode='w') as roll_file:
        csv_write = csv.writer(roll_file)
        csv_write.writerow(
            ['Transaction hash', 'Date time', 'Bet size', 'Roll under'])
        for roll in rolls:
            csv_write.writerow([
                roll['transaction_hash'],
                roll['datetime'],
                roll['bet_size_ether'],
                roll['roll_under']])


def main():
    args = parse_arg()
    address = args.address
    filename = args.csv
    rolls = get_last_bets_transactions(address)
    dump_rolls(rolls, filename)


if __name__ == '__main__':
    main()
