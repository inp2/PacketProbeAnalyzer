import dask.dataframe as dd
import numpy as np
import hvplot.pandas
import hvplot.dask
from bokeh.resources import INLINE

ddf = dd.read_csv('output.csv', dtype={'ip.dst': 'object',
       'ip.len': 'object',
       'ip.proto': 'object',
       'ip.src': 'object',
       'qframe.number': 'object'}
)
ddf = ddf.dropna()
print(ddf['ip.proto'].value_counts())
#plot = ddf.hvplot.hist("ip.len")
#hvplot.save(plot, 'test.html', resources=INLINE)
