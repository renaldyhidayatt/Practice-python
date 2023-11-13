def isNumber(s):
    numFlag, dotFlag, eFlag = False, False, False

    for i in range(len(s)):
        if "0" <= s[i] <= "9":
            numFlag = True
        elif s[i] == "." and not dotFlag and not eFlag:
            dotFlag = True
        elif (s[i] in ("e", "E")) and not eFlag and numFlag:
            eFlag = True
            numFlag = False  # reJudge integer after 'e' or 'E'
        elif (s[i] in ("+", "-")) and (i == 0 or s[i - 1] in ("e", "E")):
            continue
        else:
            return False

    return numFlag
