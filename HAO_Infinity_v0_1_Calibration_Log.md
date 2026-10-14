# HAO ∞ Reconstruction Lab v0.1 — Calibration Log

## Frozen initial reconstruction defaults

| Parameter | v0.1 default | Reason |
|---|---:|---|
| HA source model | Model A | Closest literal reading of the public description: oscillator OHLC built from centered RSI streams. |
| Flow Length | 14 | Matches the baseline RSI/ATR cadence and keeps the first reconstruction neutral. |
| Flow Smoothing | 5 | Short enough for 1–15m use without allowing raw ADL noise into the ribbon. |
| Flow Normalization Length | 50 | Gives z-score context without very long memory. |
| Ribbon Smoothing | 14 | Matches the visible 14-based baseline and reference smoothness. |
| Ribbon Width Factor | 3.0 | Conservative first-pass envelope width in centered-RSI units. |
| Ribbon Shift Factor | 0.85 | Strong enough to move accumulation below momentum / distribution above it without extreme displacement. |
| Ribbon State Deadband | 0.12 | Prevents tiny normalized-flow sign changes from flipping state. |
| Failed Break Memory | 4 bars | Short-term rejection memory appropriate to the reference semantics. |
| Compression Threshold | 72 | Requires clear multi-factor contraction before labeling compression. |

These values are **starting calibration defaults**, not claims about the protected source formula.

## Required calibration record fields

Each actual tuning pass must record all of these fields before a change is accepted:

| Symbol | Timeframe | Reference | HA source model | Ribbon settings | Observed mismatch | Change made | Improved? |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

## TradingView validation matrix

The following runs require TradingView because this implementation environment has no Pine compiler or chart runtime.

| Matrix case | Status | Notes |
|---|---|---|
| BTCUSDT 1m | Pending TradingView | Check candle response, false-break noise, ribbon lag. |
| BTCUSDT 3m | Pending TradingView | Primary short-term calibration target. |
| BTCUSDT 5m | Pending TradingView | Check smoothness vs responsiveness. |
| BTCUSDT 15m | Pending TradingView | Check whether the ribbon becomes excessively lagged. |
| ETHUSDT 5m | Pending TradingView | Cross-asset crypto sanity check. |
| Non-crypto liquid symbol | Pending TradingView | Confirm volume/ATR normalization generalizes. |

## Reference screenshot comparison axes

Use the supplied closed-source reference screenshots and score each axis separately rather than judging by overall visual similarity:

1. **HA candle geometry** — body/wick size, oscillator placement, turning behavior.
2. **RSI position** — centered line placement relative to HA candles and fixed levels.
3. **Ribbon side vs momentum** — bullish support beneath momentum; bearish resistance above it.
4. **Ribbon expansion/contraction** — whether width tracks stronger/weaker liquidity conditions naturally.
5. **POC location** — dominant support edge in bull state, resistance edge in bear state.
6. **Bull/bear state timing** — timing of green/red field transitions versus the reference.
7. **Breakout/failure semantics** — clean breaks, rejected probes, continuations, and compression releases.

## Current unresolved fidelity questions

- The protected indicator's exact liquidity-ribbon formula is unknown; v0.1 uses an original ADL-velocity + ATR-normalized support/resistance model that matches the documented semantics.
- Model A is the default HA reconstruction, while Models B/C remain experimental probes until chart comparison establishes whether another OHLC→RSI mapping fits better.
- The original description mentions lower-timeframe HA break-of-structure information in candle coloring. v0.1 intentionally does **not** add MTF requests; its personality engine is non-repainting current-timeframe structure. LTF warnings belong after baseline fidelity is established.
- Exact state-change timing, ribbon width, and POC displacement cannot be frozen as "matched" until TradingView chart comparison is completed.

## First external run protocol

1. Paste `src/HAO_Infinity_Reconstruction_Lab_v0_1.pine` into TradingView Pine Editor.
2. Compile without changing defaults.
3. Use normal price candles on the chart; the HAO pane creates its own oscillator HA candles.
4. Start with BTCUSDT 3m, then 1m/5m/15m.
5. Capture Focus and Diagnostic screenshots over the same chart region.
6. Record mismatches in the table above **before** changing a reconstruction parameter.
7. Change one calibration family at a time; do not simultaneously tune HA mapping and ribbon geometry.
