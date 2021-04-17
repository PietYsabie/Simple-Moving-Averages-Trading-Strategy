"""
Simple Moving Averages Trading Framework Strategy
Using Jesse Trading Framework at https://github.com/jesse-ai/jesse
Piet ysabie (piet.ysabie@gmail.com)
This strategy is a very simple momentum strategy
Allows for easy entry when price moves above fast SMA, and slow exit when price drops below slow (long) SMA
"""

from jesse.strategies import Strategy
import jesse.indicators as ta
from jesse import utils

class SMA1(Strategy):
    def __init__(self):
        super().__init__()

        self.vars["fast_sma_period"] = 5
        self.vars["slow_sma_period"] = 200

    @property
    def fast_sma(self):
        return ta.sma(self.candles, self.vars["fast_sma_period"])

    @property
    def slow_sma(self):
        return ta.sma(self.candles, self.vars["slow_sma_period"])

    def should_long(self) -> bool:
        # Decision wether we should go long IF we are not short; force to open (+ = buy) position if condition is met
        # Enter long if current price is above sma(200) and RSI(2) is below oversold threshold
        return self.price > self.fast_sma

    def should_short(self) -> bool:
        # Decision to go short IF we have no LONG position; force to go short if condition is met
        # Enter long if current price is below sma(200) and RSI(2) is above oversold threshold
        return False

    def should_cancel(self) -> bool:
        # Allows to cancel a not-yet-executed order (limit or stop pending order)
        return False

    def go_long(self):
        # Determines exact entry price "self.buy" and quantity in case we go long
        # self.price can be mearket price (then market order), or different from market (then stop or limit order)
        # Open long position and use entire balance to buy
        qty = utils.size_to_qty(self.capital, self.price, fee_rate=self.fee_rate)

        self.buy = qty, self.price

    def go_short(self):
        # Determines exact entry price in case we go short or close
        # Open short position and use entire balance to sell
        pass

    def update_position(self):
        # Updates exit points dynamically (evaluates at each candle); updates self.take_profit or self.liquidate
        # Exit long position if price is above sma(5)
        if self.is_long and self.price < self.slow_sma:
            self.liquidate()
    
