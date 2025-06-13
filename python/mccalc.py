#! /usr/bin/env python3
import readline

def lv2dexp(lv): # lv-1 to lv
    if lv<=0:
        return 0
    elif lv<=16:
        return 2*lv + 7
    elif lv<=31:
        return 5*lv - 38
    else:
        return 9*lv - 138


def lv2exp(lv): # 0 to lv
    # print( sum(map(lv2dexp, range(lv+1))))
    return sum(map(lv2dexp, range(lv+1)))
    # return sum([lv2dexp(i) for i in range(lv+1)])


def lvs2exp(lvs):
    return sum(map(lv2exp, lvs))
    # return sum([lv2exp(lv) for lv in lvs])


def pns2lv(pns):
    return (1<<pns) - 1

def pnss2exp(pnss):
    return lvs2exp(map(pns2lv, pnss))
    # return lvs2exp([pns2lv(pns) for pns in pnss])


def expr2lvs(expr:str): # ( a b )
    # print(expr)
    for c in '()':
        expr = expr.replace(c, ' '+c+' ')
    expr = expr.replace(',', ' ')

    expr, p, lvs = list(expr.split()), 0, []
    # print(expr)
    def dfs(s): # 自己理解的自动机: s个状态, 每次调用处理至少1个token, 每个状态要检查token合法, 再由token内容决定下一步状态
        nonlocal expr, p, lvs
        if s==0:
            if expr[p][0] in '0123456789':
                res = int(expr[p])
                p += 1
                return res, 0
            else:
                assert(expr[p]=='(')
                p += 1
                return dfs(1)
        else:
            xval, xcnt = dfs(0)
            yval, ycnt = dfs(0)
            assert(expr[p]==')')
            p += 1
            lvs += [(1<<xcnt) + (1<<ycnt) - 2 + yval]
            return (xval + yval), (max(xcnt, ycnt)+1)
    dfs(0)
    return lvs


def main():
    while(True):
        line = ''
        try:
            line = input('>>> ')
        except:
            exit()
        if line=='q':
            exit()
        lvs = expr2lvs(line)
        print(f'  {lvs2exp(lvs)}, {sum(lvs)}, {lvs}')


if __name__ == '__main__':
    main()