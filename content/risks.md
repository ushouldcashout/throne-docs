# risks

read this once, properly.

## leverage

Leverage multiplies both gains and losses. A 10x position loses 10% of its margin for every 1% the price moves against you and is liquidated at roughly a 10% move. Liquidation closes the position at the mark price and charges a fee; you can lose the whole margin behind a position. In cross margin you can lose the whole account.

## stock perps outside market hours

Stock perps trade while the underlying market is closed. Overnight and over weekends the perp price is set by this desk's order book and funding, not by the stock exchange. When the exchange opens, the index snaps to the live price. Gaps at the open, after earnings, or after news can be large, and stop orders may fill far from their trigger. Do not hold a stock perp through the open with margin you cannot afford to lose.

## funding

Funding payments are charged on your full position size, not on your margin. Sustained one-sided funding, common on stock perps overnight, can consume margin even when the price does not move.

## liquidity

Some markets are thinner than others, especially off-hours. Market orders in thin books fill at worse prices than the last trade suggests. Use limit orders when size matters.

## technology

The desk is software running on a public blockchain and on third-party infrastructure. Outages, chain congestion, oracle delays, wallet bugs, front-end bugs and smart contract vulnerabilities are all possible. During an outage you may be unable to close a position. Never run size that depends on being able to exit at any second.

## regulatory

Perpetual futures are restricted or prohibited in some jurisdictions. It is your responsibility to know whether you may use this desk. Restricted regions are blocked at connect; circumventing that block breaches the terms.

## no advice, no guarantees

Nothing on the desk, the site, these docs or our social accounts is investment advice. Points, referral rewards and any future token are programs that can change or end. Past fee revenue is not a promise of future revenue.

## the rule

Only trade with money you can afford to lose entirely. That is not a disclaimer; it is how leverage works.
