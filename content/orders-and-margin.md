# orders, margin, leverage

how to place a trade and what backs it.

## order types

| order | behaviour |
|---|---|
| market | fills immediately against the book at the best available prices. pays the taker fee. |
| limit | rests on the book at your price. if it fills without crossing the spread it pays the maker fee, which is zero. |
| stop market / stop limit | triggers when the mark price reaches your trigger, then places a market or limit order |
| take profit / stop loss | attached to a position, closes it when the mark price reaches the level |
| reduce only | an order that can only shrink a position, never flip or grow it |
| post only | a limit order that is cancelled if it would take liquidity |
{: .left}

## margin modes

**Cross margin** is the default. All positions share one pool of collateral. A winning position supports a losing one, and one liquidation can affect everything.

**Isolated margin** gives a position its own collateral. Only that collateral is at risk for that position. You pick the mode per market from the order form, before you have a position open in it.

## leverage

Leverage is set per market with the slider on the order form, up to that market's maximum. Higher leverage means less collateral behind the same position and a liquidation price closer to entry. Changing leverage on a market with an open position changes the margin requirement for that position immediately.

## the risk rate

The desk shows a **risk rate** for your account (cross) or position (isolated). It is the ratio of margin you are required to hold to the margin you actually have. At **100%** the position is liquidated. The desk plays a low siren at **80%** and repeats it every 30 seconds while you stay above that line. You can mute sounds with the pill in the bottom right.

## sounds

The desk makes three sounds by default: a rising tone on a buy fill, a falling tone on a sell fill, and a chime when a position is closed or reduced. Plus the siren above. Mute them any time.
