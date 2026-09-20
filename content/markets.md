# markets and hours

perpetual futures on stocks and crypto, 24 hours a day, 7 days a week.

## what a perp is

A perpetual future is a contract that tracks the price of an asset without expiring. You never hold the stock or the coin. You hold a long or short position, marked to a reference price, with funding payments that keep the perp near the underlying. You can close any time the desk is open, which is always.

## markets

The desk lists crypto perps (BTC, ETH, SOL and others) and stock perps (large US names). The full list, with current price, 24h change, funding and open interest, is under **Markets** on the desk, and the symbol in the top bar of the trade page opens the same list.

Each market has its own maximum leverage and minimum order size. Both are shown on the order form before you submit.

## stock perps when the market is closed

Stocks trade on exchanges roughly 9:30 to 16:00 New York time on weekdays. The perps on this desk do not stop.

- **During market hours** the index price tracks the underlying stock in real time, and the perp trades tightly around it.
- **Outside market hours** there is no live stock print. The perp keeps trading on its own order book. Its mark price is derived from the book and the last index, and funding pulls it back toward where the stock last traded. Where pre-market and after-hours prices exist, the index uses them.
- **At the open** the index snaps to the live stock price. If the perp drifted overnight, that gap closes fast. Positions held through the open can move sharply in either direction. Size accordingly.

This is the defining feature of the desk and its main risk. Read [risks](risks.html) before holding stock perps over a weekend or an earnings print.

## prices you will see

| price | what it is |
|---|---|
| last | the most recent trade on this desk |
| mark | the price used for margin, unrealised PnL and liquidation. Derived from index and book, resistant to single prints. |
| index | the reference price of the underlying, from external sources |
| funding | the periodic payment between longs and shorts, shown as a rate and a countdown |
{: .left}
