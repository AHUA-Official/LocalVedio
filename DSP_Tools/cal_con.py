import numpy as np


def discrete_convolution(x, h):
    # 判断卷积核是否全零
    if np.all(h == 0):
        return np.zeros(len(x) + len(h) - 1)

    # 计算卷积的长度
    N = len(x) + len(h) - 1

    # 将列表扩展到相同的长度，使用0填充
    x_ext = np.pad(x, (0, N - len(x)), 'constant')
    h_ext = np.pad(h, (0, N - len(h)), 'constant')

    # 初始化卷积结果
    conv_result = np.zeros(N)

    # 执行卷积
    for n in range(N):
        for k in range(len(x_ext)):
            # 检查索引是否在范围内
            if n - k >= 0 and n - k < len(h_ext):
                # 计算卷积
                conv_result[n] += x_ext[k] * h_ext[n - k]

    return conv_result


# 测试
x_org = [1, 2, 3]  # 输入列表x
h_org = [0, 0]  # 输入列表h
n = 0  # x_org中零点的位置
h = h_org

# 自动调整x的长度以匹配输入序列的长度
x = np.zeros(len(x_org) + len(h_org) - 1)
x[n:n + len(x_org)] = x_org  # 在x中将x_org插入到n的位置

result = discrete_convolution(x, h)

# 去除卷积结果中的填充0
trimmed_result = result[:len(x_org) + len(h_org) - 1]

print("卷积结果:", trimmed_result)
print("序列x的零点位置:", n)
print("序列h的零点位置:", 0)  # 这里h的零点位置假设是0，你可以根据实际情况进行调整
