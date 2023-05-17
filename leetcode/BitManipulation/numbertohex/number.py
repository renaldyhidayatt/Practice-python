from typing import List, Dict


def toHex(num: int) -> str:
    if num == 0:
        return "0"

    if num < 0:
        num += 1 << 32

    mp: Dict = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "a",
        11: "b",
        12: "c",
        13: "d",
        14: "e",
        15: "f",
    }
    bitArr: List[str] = []
    while num > 0:
        bitArr.append(mp[num % 16])
        num // 16

    bitArr.reverse()
    return "".join(bitArr)
