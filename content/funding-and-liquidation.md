# funding and liquidation

the two mechanisms that keep the perp honest and the desk solvent.

## funding

Funding is a periodic payment between longs and shorts. When the perp trades above the index, longs pay shorts; below the index, shorts pay longs. The current rate and the countdown to the next payment are shown in the market bar on the trade page and on the Markets list.

Funding is paid on the notional size of your position, not on your margin, so a 20x position pays 20x the funding of the same margin unleveraged. On stock perps funding is also what anchors the price when the underlying market is closed, so overnight rates can be larger than you are used to on crypto.

Funding you pay or receive shows in your portfolio history.

## liquidation

If the mark price moves against you until your margin no longer covers the maintenance requirement, the position is liquidated. In cross margin this can take the whole account; in isolated margin only that position's collateral.

What to expect:

- Liquidation happens at the **mark price**, not the last trade, so a single wick on the book does not liquidate you on its own.
- Large positions may be reduced in steps rather than closed at once.
- A liquidation fee is charged on the liquidated notional. It is shown in the fee schedule on the desk before you trade.
- If a position closes at a loss larger than its collateral, the shortfall is covered by the venue's insurance mechanism, not by other traders' balances.

The desk gives you two warnings before this: the risk rate colour and the 80% siren. Adding collateral or reducing size resets both.
