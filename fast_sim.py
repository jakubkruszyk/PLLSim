import matplotlib.pyplot as plt
import numpy as np
from random import randint

T1 = 50
T2 = 48

SUM_MAX = 16
LEAD_LAG_MAX = 9

PERIODS = 100


def osc(x):
    return 1 if(x % T1 >= T1/2) else 0


def osc2(x):
    return 1 if(x % T2 >= T2/2) else 0


def fast_sim(periods, iters=1, rip=False):
    tick = 0
    lead = 0
    lag = 0

    if rip:
        tick += randint(-5, 5)
    for _ in range(iters):
        for i in range(periods):
            tick += T2
            if osc(tick) == 1:
                lead += 1
            else:
                lag += 1
    return lead/iters, lag/iters


def fast_pll(periods):
    lead_list = [0 for _ in range(periods)]
    lag_list = [0 for _ in range(periods)]
    inc_dec_list = [0 for _ in range(periods)]
    lead = 0
    lag = 0
    tick = 0
    T2_offset = 0

    for i in range(periods):
        tick += (T2 + T2_offset)
        if osc(tick) == 1:
            lead += 1
            lead_list[i] = 1
        else:
            lag += 1
            lag_list[i] = 1

        if lead+lag > SUM_MAX:
            lead = 0
            lag = 0
        elif lead >= LEAD_LAG_MAX:
            lead = 0
            lag = 0
            inc_dec_list[i] = 1
            T2_offset += 1
        elif lag >= LEAD_LAG_MAX:
            lead = 0
            lag = 0
            inc_dec_list[i] = -1
            T2_offset -= 1

    return lead_list, lag_list, inc_dec_list


leads, lags = fast_sim(PERIODS)
print(f"Lead: {leads}, lag: {lags}")

leads, lags, inc = fast_pll(PERIODS)
ticks = [i for i in range(len(leads))]

fig, axes = plt.subplots(3, 1, sharex="all")
axes[0].stem(leads)
axes[0].set_ylabel("Leads")
axes[0].set_ylim(0, 1.1)

axes[1].stem(lags)
axes[1].set_ylabel("Lags")
axes[1].set_ylim(0, 1.1)

axes[2].stem(inc)
axes[2].set_ylabel("Delta")
axes[2].set_ylim(-1.1, 1.1)

plt.show()

