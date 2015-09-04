import database_tools as dt 
import indicators
import datetime


print "standard_deviation " + str(indicators.standard_deviation("TXT",datetime.datetime.today(),10))

print "simple_moving_average " + str(indicators.SMA("TXT",datetime.datetime.today(),10))

print "volatility " + str(indicators.volatility("TXT",datetime.datetime.today(),10))

print "WilliamsR " + str(indicators.willamsR("TXT",datetime.datetime.today(),10))

print "RSI " + str(indicators.RSI("TXT",datetime.datetime.today(),10))

print "average_true_range " + str(indicators.ATR("TXT",datetime.datetime.today(),10))

print "EMA " + str(indicators.EMA("TXT",datetime.datetime.today(),10))

print "bollinger_bands_customized " + str(indicators.bollinger_bands_customized("TXT",datetime.datetime.today(),10))

