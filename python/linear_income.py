def func(k:float, n:int=1)->float:
    # k 单次收益率; n 连续失败n-1次之后的第n次
    # 返回第n次需要投入多少
    if not hasattr(func, "res"):
        func.res = {}
    if n==0:
        return 0.0
    if (k,n) in func.res:
        return func.res[(k,n)]
    res = n/k
    for i in range(n):
        res += func(k,i)/k
    func.res[(k,n)] = res
    return res


def main():
    k = 0.5
    print([1*func(k, i) for i in range(15)])
    # 发现结果是指数级别的, 所以其实完全不可行


if __name__ == '__main__':
    main()