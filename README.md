# mgarch

mgarch is a python package for predicting volatility of daily returns in financial markets. 

DCC-GARCH(1,1) for multivariate normal distribution.


## Use case:

```python
rt = (t, n) numpy matrix with t days of observation and n number of assets
import mgarch
vol = mgarch(rt)
vol.fit()
cov_nextday = vol.predict()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Academic Free License v3.0