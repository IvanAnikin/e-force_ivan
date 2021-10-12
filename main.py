from typing import Dict, List, Tuple, Union

from candb import CanDB
import numpy as np


def parse_log(file, pathToJson) -> Dict[int, List[Tuple[float, List[Union[int, float]]]]]:
    data: Dict[int, List[Tuple[float, List]]] = {}
    candb: CanDB = CanDB([pathToJson])
    with open(file, "r") as f:
        # discard first 4 lines
        [f.readline() for _ in range(4)]

        for line in f:
            parts = line.split()
            time = float(parts[0])
            id_str = parts[2]
            if id_str[-1] == "x":
                can_id = int(id_str[:-1], base=10)
            else:
                can_id = int(id_str, base=10)
            if can_id not in [419365098]:
                continue
            # first get number of bytes in payload
            byte_count = int(parts[5])
            payload = [int(x, base=10) for x in parts[6:6 + byte_count]]
            msg = candb.parseData(can_id, payload, time)

            if can_id not in data.keys():
                data[can_id] = []

            data[can_id].append((time, msg))
    return data


def main():
    data = parse_log("track_drive02.asc", "D1.json")


if __name__ == '__main__':
    main()
