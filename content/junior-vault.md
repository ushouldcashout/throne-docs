# the junior vault

the first-loss tranche. stake $THRONE. to get in, cover the senior vault's losses first, take the court's income.

## what it is

The junior vault sits under the [senior vault](senior-vault.html). It runs on the same 7-day clock, holds its own USDG position in the same lending vault, and does two things senior does not:

- **it pays first.** When the lending vault loses money, the senior vault pulls the loss from the junior vault before any senior share is marked down. Junior pays up to everything it holds.
- **it is paid the court's income.** The desk's fee streams that are not needed to keep senior whole flow to junior, through the income router, once that router is switched on.

In return the junior vault is gated: every deposit has to be backed by a $THRONE. stake, it is capped at a fifth of the whole stack, and exits take one full epoch of notice. Shares (`jrUSDG`) are not transferable.

It opens to the treasury first and to the public later, behind a 7-day governance switch. Until that switch is thrown, deposits from anyone but the treasury are refused.

## the flow of a deposit

<div class="flow">
<div class="step"><b>1 · you hold USDG and $THRONE.</b><span>Both in the same wallet. The vault reads its stake rate (THRONE per USDG, set by governance inside a fixed band) and tells you how much $THRONE. the deposit needs. Approve both tokens.</span></div>
<div class="arrow"></div>
<div class="step"><b>2 · the stake is pulled, then the USDG</b><span>The vault takes the $THRONE. first and checks what actually arrived; a short delivery is refused. Then it takes the USDG. The stake is locked to your wallet for as long as you hold any position. The request is refused if junior would exceed 20% of senior plus junior, if deposits are paused, or while the senior vault is mid catch-up.</span></div>
<div class="arrow"></div>
<div class="step"><b>3 · the USDG waits</b><span>Like senior, your USDG sits idle until the close. It is not exposed to anything yet and it is never used to cover a loss while it is pending.</span></div>
<div class="arrow"></div>
<div class="step"><b>4 · senior closes, then junior closes</b><span>Junior's epoch number is senior's; it cannot close until senior has. The keeper closes both in one transaction. Junior first folds in any income that arrived during the week, then values itself, writes its own share price, mints the week's deposits at that price and supplies the USDG to the lending vault.</span></div>
<div class="arrow"></div>
<div class="step"><b>5 · claim your shares</b><span>Claim them to your wallet. They can only ever sit in your wallet or in the vault's own escrow: no transfers, no approvals.</span></div>
<div class="arrow"></div>
<div class="step"><b>6 · earn, and stand first in line for losses</b><span>Each week your shares carry junior's lending interest and its share of the court's income. If the lending vault loses money that week, the senior vault calls junior for cover before it prices its own shares, and junior's price takes the hit instead.</span></div>
</div>

## how a loss is covered

<div class="flow">
<div class="step"><b>senior measures a loss</b><span>At its close, the senior vault sees its lending-vault position worth less than its book. Only the part caused by the lending vault's share price counts; senior's own migration slippage never does.</span></div>
<div class="arrow"></div>
<div class="step"><b>junior pays from idle USDG first</b><span>Any USDG junior holds free is sent across.</span></div>
<div class="arrow"></div>
<div class="step"><b>then from its lending-vault position</b><span>When both vaults sit on the same lending vault, junior hands over lending-vault shares directly. No liquidity is needed, which matters because a lending-vault loss and an illiquid lending vault tend to arrive together.</span></div>
<div class="arrow"></div>
<div class="step"><b>senior re-prices on the covered amount</b><span>Whatever junior could pay is added back to senior's value before the senior price is written. Anything junior could not pay lands on senior. Junior's pending deposits and USDG already set aside for exits are never touched.</span></div>
</div>

## the flow of a withdrawal

<div class="flow">
<div class="step"><b>1 · request a redeem</b><span>Your shares move into the vault's custody. The request is queued for the close after next: one full epoch of notice, counted on senior's clock. One open request per wallet; you can top it up while it waits in the same window.</span></div>
<div class="arrow"></div>
<div class="step"><b>2 · your shares keep working</b><span>Until they are filled, escrowed shares carry the full result of the vault, income and losses alike.</span></div>
<div class="arrow"></div>
<div class="step"><b>3 · the close that fills you</b><span>Same waterfall as senior: this week's pending deposits, then idle cash, then the lending vault. A partial fill rolls forward.</span></div>
<div class="arrow"></div>
<div class="step"><b>4 · claim your USDG, get your stake back</b><span>Claim the USDG set aside for you. Once you hold no shares and have no deposit pending, your whole $THRONE. stake is released to the wallet it came from, in the same transaction when possible, otherwise through a separate release call anyone can trigger. A partial exit keeps the whole stake locked.</span></div>
</div>

## the numbers that govern it

| what | value |
|---|---|
| epoch | senior's, in lockstep |
| notice to exit | one full epoch |
| share token | jrUSDG, non-transferable |
| size | at most 20% of senior plus junior, checked at entry |
| stake | $THRONE., at a governance rate inside a fixed band; returned in full on a complete exit |
| open to | the treasury at launch; the public after a 7-day governance switch |
| cover | up to junior's whole value, idle USDG first, then lending-vault shares |
{: .left}

## what can go wrong

**You are the first loss.** That is the product. A bad week in the lending vault can take a large part, or all, of junior's value before senior feels anything.

**Illiquidity delays exits.** Notice is one epoch; a fill can take longer if the lending vault cannot pay out that week.

**Wipeout.** A close at zero stops new deposits for good; pending deposits are refundable one for one and the stake behind them comes back.

> Nothing on this page is an offer, a promise of yield, or financial advice. Read the [risks](risks.html) and the [terms](https://throne.network/terms).
