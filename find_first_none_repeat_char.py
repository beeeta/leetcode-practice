"""
寻找一个字符串中第一个未重复的字符
"""
def ffnrc():
    test = 'abahfuwefonqflaifhahgpakpdfounewfwaffba'
    tarr = []
    for i in test:
        if i in tarr:
            tarr.remove(i)
        else:
            tarr.append(i)
    if len(tarr):
        return tarr[0]
    else:
        return None

if __name__ == '__main__':
    print(ffnrc())

