# HAO ∞ v0.1 Test Matrix

## Task 1 — Core shell / centered RSI
- [ ] Pine v6 declaration compiles in TradingView.
- [ ] `overlay=false` keeps the indicator in a lower pane.
- [ ] Default RSI length is 14.
- [ ] Centered RSI uses ordinary RSI minus 50, so centered 0 corresponds to RSI 50.
- [ ] Structural levels are exactly +30, +10, 0, -10, -30.
- [ ] Default RSI moving average is SMA 14, width 1.
- [ ] MA choices include SMA, EMA, RMA, WMA, HMA.
- [ ] Deep Ocean and Aurora appear as theme options.
- [ ] Bull background spans 0→+30, range spans -10→+10, bear spans -30→0.

> TradingView compile/visual checks remain manual because this execution environment has no Pine compiler.

## Task 2 — Oscillator Heiken-Ashi engine
- [ ] Model A is the default HA source model.
- [ ] Model A uses centered RSI of open/high/low/close.
- [ ] Experimental Model B and Model C can be selected without changing structural zone geometry.
- [ ] HA high always encloses both HA open and HA close.
- [ ] HA low always encloses both HA open and HA close.
- [ ] First valid HA bar seeds open from `(oscOpen + oscClose) / 2`.
- [ ] Warm-up `na` values do not create invalid recursive state.
- [ ] Oscillator candles render with `plotcandle()` in the lower pane.
- [ ] Diagnostic mode reports `HA GEO = OK/FAIL`.

## Task 3 — ADL / flow pressure / ATR normalization
- [ ] Flat bars (`high == low`) return neutral MFM 0 without division by zero.
- [ ] Missing or zero volume contributes neutral MFV 0.
- [ ] ADL velocity is smoothed before normalization.
- [ ] Flow pressure is clamped to [-1,+1].
- [ ] Robust normalization uses rolling mean/stdev and a bounded tanh transform.
- [ ] ATR denominator has a nonzero floor.
- [ ] Volatility factor is conservatively clamped so ribbon width cannot explode.
- [ ] Research/Diagnostic modes expose flow pressure, ADL velocity, and ATR factor.

## Task 4 — Liquidity ribbon / Point of Control
- [ ] Ribbon width is always nonnegative.
- [ ] Ribbon lower edge never exceeds upper edge.
- [ ] Positive flow displaces the ribbon toward support beneath momentum.
- [ ] Negative flow displaces the ribbon toward resistance above momentum.
- [ ] Flow deadband plus persistence prevents rapid bull/bear flip-flop.
- [ ] Bull POC resolves to the lower/support edge.
- [ ] Bear POC resolves to the upper/resistance edge.
- [ ] Initial neutral POC resolves to the displaced ribbon axis.
- [ ] Ribbon width expands with volatility/liquidity conviction and is hard-clamped.
- [ ] Diagnostic mode reports `RIBBON GEO = OK/FAIL`.

## Task 5 — Structural events / compression
- [ ] Breakouts cannot confirm on an open realtime bar.
- [ ] Crossing +10/-10 alone is not enough: HA must clear ribbon/POC and flow must align.
- [ ] Failed breaks require a prior probe plus rejection/re-entry within memory.
- [ ] Continuation requires directional ribbon state, defended POC, and renewed HA expansion.
- [ ] Compression score is bounded 0..100; higher = tighter/less energetic.
- [ ] Compression itself never emits a long/short alert.
- [ ] Compression release is separately alertable.
- [ ] Historical event conditions are gated by `barstate.isconfirmed`.

## Task 6 — Structure-aware HA candle personality
- [ ] Structure-aware coloring is optional and enabled by default.
- [ ] Candle family does not have to flip on every opposite HA body if POC/ribbon structure still holds.
- [ ] Bull/Bear impulse requires structural progress beyond a prior rolling high/low, not candle direction alone.
- [ ] Weakening can appear before a full opposite impulse.
- [ ] Rolling structural levels exclude the current bar and do not use future-looking pivots.
- [ ] Structure confidence is clamped to 0..1.
- [ ] Classic HA direction coloring remains available as fallback.

## Task 7 — Deep Ocean / Aurora visual system
- [ ] Deep Ocean uses teal/aqua/turquoise bullish conviction and burgundy/crimson/red-orange bearish conviction.
- [ ] Aurora uses green/lime/cyan bullish conviction, magenta/coral/crimson bearish conviction, violet/blue transitions.
- [ ] Theme intensity changes color only; ribbon/HA geometry is unchanged.
- [ ] Focus shows the trading baseline with minimal event markers.
- [ ] Clean removes RSI/MA, backgrounds, diagnostics, research traces, and event markers while retaining HA/ribbon/POC.
- [ ] Research exposes calibration traces without the full diagnostic table.
- [ ] Diagnostic shows a compact tiny-text internal status table.
- [ ] Theme colors are default-on but custom HA/line/zone colors remain available by disabling theme colors.
- [ ] Mobile layout remains unobstructed by large panels.

## Task 8 — v0.1 calibration / release gate
- [x] Reconstruction-only controls are grouped under `Reconstruction Calibration`.
- [x] Frozen initial defaults: Model A; flow 14/5/50; ribbon smoothing 14, width 3.0, shift 0.85, deadband 0.12; failed-break memory 4; compression threshold 72.
- [x] Local static gate: Pine v6 declaration, lower-pane indicator, balanced delimiters, no deprecated `transp`, no MTF calls, no future-looking pivots.
- [x] Local executable reference tests cover HA geometry, flow edge cases, ribbon invariants, event confirmation, and structure personality.
- [ ] TradingView Pine compiler: paste and compile source.
- [ ] BTCUSDT 1m visual/behavior pass.
- [ ] BTCUSDT 3m visual/behavior pass.
- [ ] BTCUSDT 5m visual/behavior pass.
- [ ] BTCUSDT 15m visual/behavior pass.
- [ ] ETHUSDT 5m visual/behavior pass.
- [ ] One liquid non-crypto symbol visual/behavior pass.
- [ ] Reference screenshot comparison on seven calibration axes.

> External TradingView checks are intentionally left unchecked: this environment cannot execute Pine on TradingView servers. Do not treat them as passed until the script is compiled and observed on-chart.
