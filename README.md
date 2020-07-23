# mgarch

mgarch is a python package for predicting volatility of daily returns in financial markets. 

DCC-GARCH(1,1) for multivariate normal distribution.


## Use case:
For Multivariate normal Distribution
```python
rt = (t, n) numpy matrix with t days of observation and n number of assets
import mgarch
vol = mgarch.mgarch()
vol.fit(rt)
ndays = 10 # volatility of nth day
cov_nextday = vol.predict(ndays)
```

For Multivariate Student-t Distribution
```python
rt = (t, n) numpy matrix with t days of observation and n number of assets
import mgarch
dist = 't'
vol = mgarch.mgarch(dist)
vol.fit(rt)
ndays = 10 # volatility of nth day
cov_nextday = vol.predict(ndays)
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Academic Free License v3.0