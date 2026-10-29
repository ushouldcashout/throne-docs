# the senior vault

deposit USDG. hold a share. the share is priced once a week.

## what it is

The senior vault is the court's main pool. You deposit USDG, the vault supplies all of it to a lending vault on Robinhood Chain (the Steakhouse USDG vault on Morpho), and the desk's fee income is added on top. Everything settles once per 7-day epoch. Between settlements nothing moves: the share price is fixed from one close to the next, so there is nothing to time and nothing to front-run.

Your position is an ERC-20 share (`svUSDG`). It is transferable. One share price, written at every close, converts shares to USDG and back.

Senior is senior because it is paid before the junior vault: when the lending vault loses money, the [junior vault](junior-vault.html) absorbs that loss first, up to everything it holds, before a senior share is marked down.

## the flow of a deposit

<div class="flow">
<div class="step"><b>1 · you hold USDG</b><span>USDG on Robinhood Chain, in a wallet you control. Connect it on the court page and approve the vault to pull the amount.</span></div>
<div class="arrow"></div>
<div class="step"><b>2 · request a deposit</b><span>Your USDG moves into the vault and waits. It is not supplied anywhere yet and it earns nothing yet: it is held idle until the epoch closes, so nobody who is already in can be diluted by money that has not been priced. One open request per wallet; add to it any time before the close. The request is refused if the vault is at its cap, if deposits are paused, or if the lending vault's share price is below where it was at the last close.</span></div>
<div class="arrow"></div>
<div class="step"><b>3 · the epoch closes</b><span>Every 7 days. The vault reads what it is worth right now (idle USDG plus its lending-vault position plus this week's fee income), compares it with last week's book, and writes the new share price. Then every pending deposit of the week is minted into shares at that price in one step, your USDG is netted against anyone leaving that week, and the rest is supplied to the lending vault.</span></div>
<div class="arrow"></div>
<div class="step"><b>4 · claim your shares</b><span>After the close your shares are waiting in the vault. Claim them to your wallet in one transaction. They are yours from that point: hold, transfer, or queue them to exit.</span></div>
<div class="arrow"></div>
<div class="step"><b>5 · earn</b><span>From the next close on, your shares carry the vault's results: lending interest, the desk's fee income for the week, and any loss the lending vault takes that the junior vault could not cover. The price moves once a week, at the close, and at no other time.</span></div>
</div>

## the flow of a withdrawal

<div class="flow">
<div class="step"><b>1 · request a redeem</b><span>You name how many shares to redeem. They move into the vault's custody at once (they can no longer be transferred or redeemed twice) and are priced at the next close.</span></div>
<div class="arrow"></div>
<div class="step"><b>2 · the epoch closes</b><span>The vault strikes the week's price and raises the USDG your shares are worth, in this order: first from the USDG that new depositors brought in this week, then from idle cash, then by redeeming from the lending vault. If the lending vault is not fully liquid that week you are paid what could be raised and the rest of your shares stay queued, at full exposure, for the following close. Nothing is lost by waiting.</span></div>
<div class="arrow"></div>
<div class="step"><b>3 · claim your USDG</b><span>The USDG raised for you is set aside in the vault, excluded from everyone else's price, until you claim it. Claim all of it or part of it, whenever you like.</span></div>
</div>

A deposit and a redeem in the same epoch never returns more than you put in, and a loss recognised at a close is always applied before anyone leaving that week is paid.

## the numbers that govern it

| what | value |
|---|---|
| epoch | 7 days |
| who closes it | the keeper at the boundary; anyone after 6 hours |
| share token | svUSDG, ERC-20, transferable |
| price changes | only at a close |
| cap | set by governance, raised only through a 7-day timelock |
| lending vault | Steakhouse USDG (Morpho Vaults V2), on Robinhood Chain |
| migration | 7-day timelocked, Morpho Vault V2 only, 0.5% max slippage, sentinel can cancel |
{: .left}

## what can go wrong

**The lending vault loses money.** The loss shows up at the close as a lower price. If the junior vault is wired it pays first, from its own USDG and its own lending-vault position, up to everything it holds. What it cannot cover lands on senior. Deposits pause automatically while the lending vault's share price sits below its last-close level.

**The lending vault is illiquid.** Redeems are filled with what can be raised and the rest rolls to the next close. Deposits still work.

**Total wipeout.** If a close ever prices the vault at zero, deposits are refused for good and any deposit still pending at that close is refundable one for one. The vault is not reset; a new one would be deployed.

**A close is late.** Missed epochs are caught up in one call with one live valuation; no interpolation, no smoothing. If a late close would leave less than half an epoch before the next boundary, the next epoch is absorbed into the catch-up too, so there is never a days-long epoch that someone could jump into for a slice of a week's fees.

> Nothing on this page is an offer, a promise of yield, or financial advice. Read the [risks](risks.html) and the [terms](https://throne.network/terms).
