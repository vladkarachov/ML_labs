import numpy as np


def findC(i, s, N):
    # P(x=c)
    uniqueC, counts = np.unique(T[:, i], return_counts=True)
    P_denominator = dict(zip(uniqueC, counts))
    # p(y=s x=c)
    y_equals_s, _ = np.where(y == s)
    uniqueC, counts = np.unique(T[y_equals_s, i], return_counts=True)
    P_numerator = dict(zip(uniqueC, counts))
    return np.array([(float(P_numerator[num]) / y_equals_s.size) / (float(P_denominator[num]) / N) for num in
                     P_numerator.keys()]).argmax()


N = 100
m = 10

T = np.random.randint(10, size=(N, m))
y = np.random.randint(15, size=(N, 1))
s = 4
x_star = np.array([T[findC(i, s, N), i] for i in range(m)])
print(x_star)
