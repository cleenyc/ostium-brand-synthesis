> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ostium.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fees

> Every cost you'll pay trading on Ostium: opening, oracle, rollover, and liquidation fees in one page.

export const OpeningFeeTable = () => {
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [expanded, setExpanded] = useState(new Set());
  useEffect(() => {
    let cancelled = false;
    const pairLabel = (from, to) => {
      const raw = `${from}/${to}`;
      const overrides = {
        "CL/USD": "WTI/USD",
        "HG/USD": "XCU/USD",
        "SPX/USD": "US500/USD",
        "NDX/USD": "US100/USD",
        "DJI/USD": "US30/USD",
        "DAX/EUR": "GER40/EUR",
        "FTSE/GBR": "UK100/GBR",
        "HSI/HKD": "HK50/HKD",
        "NIK/JPY": "JP225/JPY"
      };
      return overrides[raw] ?? raw;
    };
    (async () => {
      try {
        const res = await fetch("https://api.subgraph.ormilabs.com/api/public/67a599d5-c8d2-4cc4-9c4d-2975a97bc5d8/subgraphs/ost-prod/live/gn", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            query: `query { pairs(first: 100) { takerFeeP from to group { name } } }`
          })
        });
        const json = await res.json();
        if (json.errors?.length) throw new Error(json.errors.map(e => e.message).join("; "));
        if (!cancelled) setRows((json.data?.pairs ?? []).map(p => ({
          market: pairLabel(p.from, p.to),
          group: p.group?.name ?? "other",
          feeBps: parseFloat(p.takerFeeP) / 1e4
        })));
      } catch (e) {
        if (!cancelled) setError(e.message || "Failed to load fees");
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();
    return () => {
      cancelled = true;
    };
  }, []);
  const fmtGroup = name => {
    if (!name) return "Other";
    if (name.toLowerCase() === "etf") return "ETF";
    return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
  };
  const fmtBps = n => {
    if (!Number.isFinite(n)) return "—";
    return `${Math.round(n * 100) / 100} bps`;
  };
  const groups = useMemo(() => {
    const map = new Map();
    for (const r of rows) {
      if (!map.has(r.group)) map.set(r.group, []);
      map.get(r.group).push(r);
    }
    return Array.from(map.entries()).map(([name, pairs]) => {
      const fees = pairs.map(p => p.feeBps).filter(Number.isFinite);
      const minRaw = fees.length ? Math.min(...fees) : null;
      const maxRaw = fees.length ? Math.max(...fees) : null;
      const minR = minRaw != null ? Math.round(minRaw * 100) / 100 : null;
      const maxR = maxRaw != null ? Math.round(maxRaw * 100) / 100 : null;
      const feeRange = minR === maxR ? fmtBps(minRaw) : `${fmtBps(minRaw)} – ${fmtBps(maxRaw)}`;
      return {
        name,
        label: fmtGroup(name),
        pairs: [...pairs].sort((a, b) => a.market.localeCompare(b.market)),
        feeRange
      };
    }).sort((a, b) => a.label.localeCompare(b.label));
  }, [rows]);
  const toggle = name => setExpanded(prev => {
    const next = new Set(prev);
    next.has(name) ? next.delete(name) : next.add(name);
    return next;
  });
  if (error) return <p className="not-prose text-sm text-red-600 dark:text-red-400">{error}</p>;
  const headCell = "px-3 py-2 text-xs font-semibold uppercase tracking-wide text-zinc-500 dark:text-zinc-500";
  const bodyCell = "px-3 py-1.5 text-sm text-zinc-700 dark:text-zinc-300";
  const feeHead = `${headCell} w-[1%] whitespace-nowrap tabular-nums !text-right`;
  const feeBody = `${bodyCell} w-[1%] whitespace-nowrap text-right tabular-nums`;
  return <div className="not-prose w-full overflow-x-auto">
      <table className="w-full min-w-[20rem] border-collapse text-sm">
        <colgroup>
          <col />
          <col className="w-[1%]" />
          <col className="w-[1%]" />
        </colgroup>
        <thead>
          <tr className="border-b border-zinc-950/10 dark:border-white/10">
            <th scope="col" className={`${headCell} text-left`}>
              <span className="flex items-center gap-1">
                <span className="inline-block h-2 w-2 shrink-0" aria-hidden />
                Group / market
              </span>
            </th>
            <th scope="col" className={feeHead}>
              <span className="flex w-full justify-end">Opening</span>
            </th>
            <th scope="col" className={feeHead}>
              <span className="flex w-full justify-end">Closing</span>
            </th>
          </tr>
        </thead>
        <tbody className="divide-y divide-zinc-950/[0.06] dark:divide-white/[0.06]">
          {loading && Array.from({
    length: 6
  }).map((_, i) => <tr key={i}>
                <td className={bodyCell}>
                  <span className="flex items-center gap-1">
                    <span className="inline-block h-2 w-2 shrink-0" aria-hidden />
                    <div className="h-3.5 w-24 max-w-[12rem] animate-pulse rounded bg-zinc-100 dark:bg-zinc-800" />
                  </span>
                </td>
                <td className={`${feeBody} text-zinc-500 dark:text-zinc-500`}>
                  <div className="ml-auto h-3.5 w-14 animate-pulse rounded bg-zinc-100 dark:bg-zinc-800" />
                </td>
                <td className={`${feeBody} text-zinc-500 dark:text-zinc-500`}>
                  <div className="ml-auto h-3.5 w-10 animate-pulse rounded bg-zinc-100 dark:bg-zinc-800" />
                </td>
              </tr>)}

          {!loading && groups.flatMap(g => {
    const isOpen = expanded.has(g.name);
    const groupRow = <tr key={`g-${g.name}`} onClick={() => toggle(g.name)} className="group cursor-pointer select-none transition-colors hover:bg-zinc-950/[0.03] dark:hover:bg-white/[0.04]">
                  <td className={`${bodyCell} text-zinc-900 dark:text-zinc-100`}>
                    <span className="flex min-w-0 items-center gap-1.5 font-medium">
                      <span className="inline-block h-2 w-2 shrink-0" aria-hidden />
                      <span className="min-w-0 flex-1 break-words">{g.label}</span>
                      <span className="shrink-0 font-normal text-zinc-400 tabular-nums dark:text-zinc-500">
                        ({g.pairs.length})
                      </span>
                      <svg className={`h-3.5 w-3.5 shrink-0 text-zinc-400 transition-transform duration-200 dark:text-zinc-500 group-hover:text-zinc-600 dark:group-hover:text-zinc-400${isOpen ? " rotate-180" : ""}`} fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" aria-hidden>
                        <path d="M19 9l-7 7-7-7" />
                      </svg>
                    </span>
                  </td>
                  <td className={feeBody}>{g.feeRange}</td>
                  <td className={`${feeBody} text-zinc-400 dark:text-zinc-500`}>0 bps</td>
                </tr>;
    const pairRows = isOpen ? g.pairs.map(p => <tr key={`p-${p.market}`}>
                      <td className={`${bodyCell} text-zinc-500 dark:text-zinc-400`}>
                        <span className="flex min-w-0 items-center gap-1">
                          <span className="inline-block h-2 w-2 shrink-0" aria-hidden />
                          <span className="min-w-0 break-words" title={p.market}>{p.market}</span>
                        </span>
                      </td>
                      <td className={`${feeBody} text-zinc-600 dark:text-zinc-400`}>{fmtBps(p.feeBps)}</td>
                      <td className={`${feeBody} text-zinc-400 dark:text-zinc-500`}>0 bps</td>
                    </tr>) : [];
    return [groupRow, ...pairRows];
  })}
        </tbody>
      </table>
    </div>;
};

## Overview

Ostium has three explicit fees (opening, oracle, rollover) plus liquidation, which takes remaining collateral when your margin is wiped out. There is no closing fee; your displayed PnL equals your realized PnL.

| Fee Type     | When Charged           | Rate                                         |
| ------------ | ---------------------- | -------------------------------------------- |
| Opening fee  | Position entry         | 3–5 bps (varies by asset)                    |
| Oracle fee   | Price request          | \$0.10 USDC flat                             |
| Rollover fee | Continuous (all pairs) | Variable, derived from underlying carry cost |
| Liquidation  | Position liquidated    | Remaining collateral                         |

Opening, rollover, and liquidation proceeds flow into the Ostium Vault. 30% of opening fees accrues to OLP holders at each daily settlement. See [Vault Overview](/vault/overview) for how fees translate into OLP yield.

<Info>
  **Coming from crypto perps?** Ostium does not use a zero-sum funding-rate payment between longs and shorts. All pairs, including crypto, use rollover fees anchored to real-world carry costs — derived from funding rates and futures term structure for the underlying asset. See [Rollover vs. Funding Rates](#rollover-vs-funding-rates) below for the comparison.
</Info>

***

## Opening Fee

The opening fee is a one-time charge deducted from your collateral when you enter a position. Rates vary by pair; the table below loads live values from the protocol subgraph.

<OpeningFeeTable />

**Example:** 5x long on EUR/USD, 2,000 USDC collateral. Notional: 10,000 USDC. Fee: 10,000 × 3 bps = **3 USDC**. Effective collateral: 1,997 USDC.

### Where Opening Fees Go

Opening fees split between two destinations: 30% flows to OLP holders at each daily settlement, and the remainder funds protocol operations and development. The OLP allocation is a tunable protocol parameter.

***

## Oracle Fee

The oracle fee is a flat \$0.10 USDC charge each time the protocol fetches an onchain price. It covers oracle infrastructure and automation costs. The fee is refunded when you close your full position successfully, but not on partial closes or failed transactions.

| Action                       | Fee    | Refunded? |
| ---------------------------- | ------ | --------- |
| Open a market order          | \$0.10 | No        |
| Place a limit or stop order  | \$0.10 | No        |
| Cancel a limit or stop order | \$0.10 | No        |
| Partial close                | \$0.10 | No        |
| Full close (successful)      | \$0.10 | **Yes**   |
| Remove collateral            | \$0.10 | No        |

<Note>
  If a market open fails due to slippage, your collateral is returned but the \$0.10 oracle fee is still consumed. The interface blocks most failure cases, so slippage is the most common reason you'd see a failed open with the fee charged.
</Note>

**Fee cap:** Oracle fees in a single transaction cannot exceed 10 USDC.

***

## Rollover Fee

The rollover fee is the cost of holding any position over time. It reflects the real-world carry cost of the underlying asset — derived from the futures term structure or funding rates of the underlying — plus a carry premium from Ostium. Rates update daily via Gelato keepers; the fee itself accrues continuously per block.

Both the fee and the rate display under the **Net Rate (L/S)** label in the trading interface.

### Two-Sided Rollover

On every pair, rollover is two-sided: one side can collect rather than pay, depending on whether the underlying sits in contango or backwardation. The formula is symmetric:

* **Long rollover** = underlyingCarry + brokerPremium
* **Short rollover** = −underlyingCarry + brokerPremium

Where `underlyingCarry` is derived from the futures curve or funding-rate market of the underlying asset, and `brokerPremium` is Ostium's markup (typically 1–2% annualized). If `underlyingCarry` is strongly negative (backwardation), longs may end up with a net negative rate — collecting rollover — while shorts pay more. The reverse is true in contango.

### Example: Crude Oil (WTI/USD)

WTI/USD underlying term structure: −40% annualized (deep backwardation).

* **Long:** −40% + 2% = −38% → **negative**, so longs collect a rollover credit on this pair (\~38% annualized)
* **Short:** 40% + 2% = **42%** annualized (\~0.115% daily)

A 1,000 USDC short position accrues roughly \$1.15/day in rollover fees, deducted from collateral. A long position on this pair would collect rollover, in this example around 38% annualized.

### Positive Rollover (Earning While Holding)

On any pair, the rollover rate can be positive for one side of the trade — meaning traders on that side collect rather than pay. This is a structural property of how rollover is derived: when the underlying carry is asymmetric, one side receives the spread. Oil pairs are a common example given the depth of backwardation in energy futures, but the same dynamic applies across all asset classes when the underlying curve supports it.

### By Asset Type

* **Commodities & Forex:** Derived from the futures term structure of the underlying. Contango means longs pay more; backwardation means shorts pay more. The opposing side can collect when the curve is steep enough.
* **Stocks, ETFs & Indices:** Derived from SOFR plus carry premium.
* **Crypto:** Derived from funding rates and futures term structure of the underlying market, plus carry premium. Rollover on crypto is two-sided like every other asset class; it is not a zero-sum long-vs-short funding payment.

<Accordion title="How is rollover calculated in detail?">
  **Term Structure (Commodities, Forex, Crypto)**

  Ostium pulls settlement prices from consecutive contract months (M1, M2, M3+). Rather than using the raw basis `(M2 − M1) / M1`, which spikes at contract rolls, Ostium applies Gaussian weighting across contract months:

  ```
  w_i = exp(-0.5 × ((i - current_month) / σ)²)
  smoothed_rate = Σ(w_i × rate_i) / Σ(w_i)
  ```

  The smoothed result becomes the `underlyingCarry` component. Crypto pairs additionally incorporate funding-rate information from the underlying market to reflect the cost of carry observed by institutional market-makers.

  **SOFR (Stocks, ETFs & Indices)**

  Ostium uses the published SOFR rate plus carry premium. Updated daily by Gelato keepers at 00:00 UTC.

  **Carry Premium**

  A flat 1–2% annualized markup applied to all pairs.
</Accordion>

***

## Rollover vs. Funding Rates

If you're coming from other crypto perpetual platforms, you're likely familiar with funding rates: periodic payments between longs and shorts that keep perp prices anchored to spot. Ostium takes a different approach.

|                              | Funding Rates (Typical Perp Platforms)            | Rollover Fees (Ostium)                                               |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------------------------------- |
| **What drives the rate**     | Long/short OI imbalance                           | Real-world carry costs (SOFR, futures term structure, funding rates) |
| **Who pays whom**            | Dominant side pays minority side (zero-sum)       | Traders pay the vault (or collect on enabled pairs)                  |
| **Rate behavior**            | Flips positive/negative based on market sentiment | Reflects underlying interest rates and term structure                |
| **Typical update frequency** | Every 1–8 hours                                   | Rates update daily; fee accrues continuously per block               |

Funding rates are driven by trader positioning, so they can spike or flip direction when one side of the market gets crowded. Rollover fees are anchored to real-world borrowing costs and term structure, so rates move gradually and in line with broader macroeconomic conditions. Holding costs can be estimated before entering a position from the underlying carry plus carry premium.

***

## Liquidation

There is no separate liquidation fee charged to the trader. When a position is liquidated, remaining collateral is retained by the protocol as part of settlement. The keeper bot (Gelato Functions) that executes the liquidation is paid by the protocol. You are not charged gas.

For details on when and how liquidation triggers, see [Liquidation](/traders/trading/liquidation).

***

## No Closing Fee

Ostium charges nothing to close a position, whether full or partial. Your displayed PnL is your realized PnL: no hidden exit spreads, no closing fee deducted at settlement.

This means there's no penalty for exiting a losing trade early, no cost to scaling out in pieces, and no gap between what you see and what you receive. On platforms that charge closing fees or apply exit spreads, displayed PnL overstates what you actually get.

***

## FAQ

<Accordion title="Do fees compound over time?">
  Opening and oracle fees are one-time. Rollover fees accrue continuously per block on all pairs and reduce your effective collateral over time (unless you're on the receiving side of a positive rollover). Factor holding costs into any multi-day position.
</Accordion>

<Accordion title="Where do my fees go?">
  Opening fees, rollover, and liquidation proceeds flow into the Ostium Vault. 30% of opening fees accrues to OLP holders as yield at each daily settlement; the remainder funds protocol operations and development. Oracle fees cover oracle and automation infrastructure costs. See [Vault Overview](/vault/overview) for how these flows translate into LP yield.
</Accordion>

<Accordion title="What if I don't have enough collateral to cover fees?">
  The order is rejected. Opening and oracle fees are deducted from collateral at submission. If the fee exceeds your available balance, the transaction won't execute. Reduce leverage, choose a lower-fee pair, or deposit more USDC.
</Accordion>

***

## What to Read Next

* **[Markets](/traders/reference/markets)** — All 71 trading pairs with leverage caps, fee rates, and trading hours.
* **[Opening a Trade](/traders/trading/opening-a-trade)** — Step-by-step from collateral deposit to order confirmation.
* **[Managing Positions](/traders/trading/managing-positions)** — Adjust TP/SL and collateral while a position is open.
