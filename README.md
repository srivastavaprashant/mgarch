# mgarch
 DCC-GARCH(1,1) for multivariate normal distribution. 
Use case:
 rt = (t, n) numpy matrix with t days of observation and n number of assets.
import mgarch
vol = mgarch(rt)
vol.fit()
cov_nextday = vol.predict()
