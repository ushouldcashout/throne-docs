# points and the King Drop

Every trade on the desk scores for you and for your side. Each week the side with more points takes the King Drop. These are the rules, in one place. The live board is at [throne.network/board](https://throne.network/board), the seats and the simulator at [throne.network/points](https://throne.network/points).

## the shape of it

- Every wallet is on **White** or **Black**. Your side is set from your address until you pick one (one free signature, no transaction).
- **1 point per $10** of taker volume, on any market on the desk. Maker volume earns nothing.
- Points are counted per wallet, per UTC day, from the venue's public daily rows. The board refreshes every ten minutes; the venue publishes hourly, so a trade shows within about an hour.
- **Season zero** scores from **25 September to 13 December 2026**. Pre-season points (25 September to 8 October) carry into the season and count for pieces, but belong to no drop.
- **Week 1 opens Friday 9 October at 23:00 UTC (7pm ET)** and closes at the **end of Sunday 18 October UTC** (midnight UTC, 8pm ET). Every week after closes at the end of Sunday UTC. Nine drops, the last closing 13 December.

## the drop

**923,000 $THRONE a week**, from the 3% of supply set aside for traders. Split:

| share | goes to |
|---|---|
| 72% | every wallet on the **winning side**, pro rata by that week's points |
| 18% | the winning side's **sixteen pieces**, weighted king (16 shares) down to pawn (1 share each) |
| 10% | the **losing side's king and queen**, 7% and 3% |
{: .left}

The winning side is the side with more points at the close. Equal points is a draw; a draw carries the drop into the next week.

## the floor

**$20,000 of taker volume in the week** is the floor to be paid from that week's drop. Points, seats and check-ins count regardless of the floor; the floor only decides who receives tokens. Your seat on the board shows how far you are from it.

Every share of the drop is paid out to wallets past the floor. A piece seat below the floor passes its share to the other qualified pieces on its side; a losing king or queen below the floor passes theirs into the winning side's pool. Nothing is held back.

## multipliers

| hold through the week | points |
|---|---|
| 100,000 $THRONE | 1.25x |
| 500,000 $THRONE | 1.5x |
{: .left}

- The balance is checked every ten minutes; the **week's lowest balance** sets the tier, so flashing tokens for a snapshot does not work.
- Beta-list wallets score 2x while the beta multiplier is on. Combined cap **2x**.
- A multiplier applies to the week it was earned in. Buying tokens later does not re-price earlier weeks.
- Power hour: from week 1, the **final hour of each week** (23:00 to 24:00 UTC Sunday) counts **1.5x** on points above your 23:00 baseline.

## pieces

The **top sixteen wallets on each side by season points** hold its pieces: king, queen, two rooks, two bishops, two knights, eight pawns. Seats change hands live. A wallet directly below you that out-scores you this week puts your piece **under attack**. Pieces come with first pick of the Court.

## sides

- Pick once per season, switch once per season, one free signature each.
- Side changes are open for the **first 48 hours after a week opens** and locked for the rest of the week. Changing side moves every point you have scored with you.
- A side is "full" when it holds more than 55% of confirmed picks (once 20 picks exist). Full only blocks new picks into it.

## daily check-in

One free signature a day, on the board or the points page, is **+100 points**. All seven days in a week adds **+300** more. Check-in points land on your week once you clear the $20,000 floor; until then they show as pending.

## names

You can put a name on your seat, and an X handle. Both are signed by the wallet. Verifying the handle means posting a short code from your X account and pasting the link; we read the public post, no login and no API keys. Verified handles show with a check everywhere: the board, the points page, share cards and the [King Drop channel](https://t.me/kingdropthrone).

## how a week closes

1. The week closes at the end of Sunday UTC. About an hour later, once the venue has published the final Sunday row, the result is computed and frozen.
2. The result file lists the winner, both totals, every wallet's week points, floor status, multiplier, and the sixteen pieces per side, and it is **hashed** (SHA-256 of the canonical JSON). The hash is shown on the board and posted in the channel.
3. Anyone can recompute it: pull the venue's public daily rows for the week's dates, apply the rules above, hash the same way. The result endpoint is `throne.network/api/arena/results?week=N`.
4. Drops are distributed to qualified wallets after each close. How and when is announced on [@thronedefi](https://x.com/thronedefi) and in the channel before the first drop.

## anti-wash

Points reward real taking. Matching your own orders across accounts, or back-and-forth with a partner at no risk, is reviewed and zeroed, and rankings for a week are final only after review.

## what points are not

Points are not a token and carry no promise of value. The King Drop is a weekly distribution of $THRONE under the rules above; the rules can change between weeks and changes are announced before they apply.

> Nothing on this page is financial advice. Read the [risks](risks.html) and the [terms](https://throne.network/terms).
