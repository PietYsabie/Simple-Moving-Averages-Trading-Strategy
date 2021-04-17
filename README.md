# Simple-Moving-Averages-Trading-Strategy
Simple Moving Averages Trading Framework Strategy
Using Jesse Trading Framework at https://github.com/jesse-ai/jesse

The code is based on multiple underlying Python libraries such as:
* crypto-empyrical
* matplotlib
* numba
* numpy
* pandas
* requests
* scipy
* TA-Lib
* quantstats

This file is a strategy definition file containing a very simple momentum strategy. 
Allows for easy entry when price moves above fast SMA, and slow exit when price drops below slow (long) SMA
Here's an example output for a backtest simulation based on BTC prices from 2019-12-30 till 2021-04-01:

![image](https://user-images.githubusercontent.com/78446548/115109783-16107000-9f78-11eb-9b02-efb7f15c149b.png)
