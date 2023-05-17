from typing import List


def shoppingOffers(price: List[int], special: List[List[int]], needs: List[int]) -> int:
    res = -1
    dfsShoppingOffers(price, special, needs, 0, res)
    return res


def dfsShoppingOffers(
    price: List[int], special: List[List[int]], needs: List[int], pay: int, res: int
):
    noNeeds = True

    for need in needs:
        if need < 0:
            return
        if need != 0:
            noNeeds = False

    if len(special) == 0 or noNeeds:
        for i, p in enumerate(price):
            pay += p * needs[i]

        if pay < res or res == -1:
            res = pay

        return

    newNeeds = needs[:]
    for i, n in enumerate(newNeeds):
        newNeeds[i] = n - special[0][i]
    dfsShoppingOffers(price, special, newNeeds, pay + special[0][len(price)], res)
    dfsShoppingOffers(price, special[1:], newNeeds, pay + special[0][len(price)], res)
    dfsShoppingOffers(price, special[1:], needs, pay, res)
