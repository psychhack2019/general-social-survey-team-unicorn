#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

DATA_FILEPATH = "data/gss-political-views-1972-2018.csv"
COLUMNS = [
    'year',
    'polviews',
    'spkhomo'
]

df = pd.read_csv(DATA_FILEPATH, usecols = COLUMNS)

is_liberal = lambda x: x.isin(['Extremely liberal', 'Liberal', 'Slightly liberal'])
is_conservative = lambda x: x.isin(['Extrmly conservative', 'Conservative', 'Slightly conservative'])

homosexuals_allowed_to_speak = lambda x: x.isin(['Allowed'])
homosexuals_not_allowed_to_speak = lambda x: x.isin(['Not allowed'])

fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)
ax1.plot(df.groupby('year')['polviews'].agg(lambda x: len(x[is_liberal(x)]) / len(x)), label = 'liberal')
ax1.plot(df.groupby('year')['polviews'].agg(lambda x: len(x[is_conservative(x)]) / len(x)), label = 'conservative')
ax1.legend()

ax2.plot(df.groupby('year')['spkhomo'].agg(lambda x: len(x[homosexuals_allowed_to_speak(x)]) / len(x)), label = 'homosexuals allowed to speak')
ax2.plot(df.groupby('year')['spkhomo'].agg(lambda x: len(x[homosexuals_not_allowed_to_speak(x)]) / len(x)), label = 'homosexuals not allowed to speak')
ax2.legend()

fig.show()
