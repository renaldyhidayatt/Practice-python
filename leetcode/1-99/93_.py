from typing import List


def restore_ip_address(s: str) -> List[str]:
    if not s:
        return []

    res = []
    ip = []

    dfs(s=s, index=0, ip=ip, res=res)

    return res


def dfs(s: str, index: int, ip: List[int], res: List[str]):
    if index == len(s):
        if len(ip) == 4:
            res.append(get_string(ip))
        return

    if index == 0:
        num = int(s[0])
        ip.append(num)
        dfs(s=s, index=index + 1, ip=ip, res=res)
    else:
        num = int(s[index])

        if len(ip) > 0:
            next_val = ip[-1] * 10 + num
            if next_val <= 255 and ip[-1] != 0:
                ip[-1] = next_val
                dfs(s, index + 1, ip, res)
                ip[-1] //= 10
            if len(ip) < 4:
                ip.append(num)
                dfs(s, index + 1, ip, res)
                ip.pop()


def get_string(ip: str):
    return ".".join(map(str, ip))
