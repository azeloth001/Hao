# HAO ∞ v0.2.1 — Calibration Notes

## Purpose

v0.2.1 is a surgical calibration pass. It does **not** redesign the RSI/HA core.
It targets the three mismatches exposed by the multi-timeframe v0.2 comparison:

1. ribbon role reversals were sometimes too early,
2. liquidity lobes did not retain enough thickness/memory,
3. HAO needed a compact human-language explanation layer for mobile use.

## Default Ribbon Model

`Control Surface v0.2.1`

The previous engines remain selectable:

- `Control Surface v0.2`
- `Flow Ribbon v0.1 (Legacy)`

## v0.2.1 State Rule

Flow is now **candidate pressure**, not immediate authority to reverse the ribbon.

When the active role is bearish resistance:

1. positive flow first weakens/thins the red surface,
2. HA/RSI must establish above the Control/POC,
3. acceptance must persist for the configured number of confirmed bars,
4. only then does resistance become support.

The bullish-to-bearish process is mirrored.

Default acceptance controls:

- Acceptance Bars: `2`
- Acceptance Buffer: `0.75` oscillator points

## Thickness Memory

The surface now uses asymmetric response:

- Thickness Attack: `3`
- Thickness Decay: `12`

Expansion is therefore faster than contraction. The intent is to create broader,
more persistent liquidity lobes without simply making the entire ribbon fatter.

## HAO Guide HUD

Default: `Guide`

The HUD uses four tiny rows:

- MARKET
- LIQUIDITY
- MOMENTUM
- WATCH

Text is white. Cell backgrounds carry state meaning.

HUD modes:

- Off
- Guide
- Technical

Default background transparency: `88`

The HUD hides automatically in Diagnostic display mode to avoid covering the
research table.

## Candle Palettes

Default: `Deep Ocean Adaptive`

Available:

- Deep Ocean Adaptive
- Black Flag
- Aurora
- Classic
- Custom
- Reference Geometry

Deep Ocean Adaptive fades from dark neutral graphite into turquoise/crimson as
structural confidence develops.

Black Flag is intentionally darker and more muted: graphite, restrained teal,
dusty mauve and wine/burgundy.

## First A/B Test

Use defaults first. Do not tune calibration parameters before comparison.

Recommended sequence on BTCUSDT:

`1m → 3m → 5m → 7m → 15m → 45m → 1h → 2h → 4h → 6h`

Compare v0.2.1 against the protected reference, especially:

- 7m, 45m, 1h: does the active red/green role persist longer before reversal?
- all TFs: do liquidity lobes decay more gradually?
- HTFs: has the controlled geometry of v0.2 been preserved?
- HUD: does it describe the visible story without becoming clutter?

Then switch only `Ribbon Model`:

1. Control Surface v0.2.1
2. Control Surface v0.2
3. Flow Ribbon v0.1 (Legacy)

This isolates the effect of ribbon evolution from the unchanged oscillator core.
