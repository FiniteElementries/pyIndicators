
import datetime
import strategy

current_strategy=strategy.simple_moving_average_envelope_with_RSI()

print current_strategy.buy_signal("GOOG",datetime.date.today())
