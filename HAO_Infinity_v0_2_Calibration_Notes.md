# HAO ∞ Reconstruction Lab v0.2 — Calibration Notes

## Why v0.2 exists

Side-by-side BTCUSDT screenshots from 1m, 3m, 5m, 7m, 15m, 45m, 1h, 2h, 4h and 6h showed that v0.1 was already close on the centered RSI, RSI MA, oscillator turning points and broad bull/bear timing. The largest mismatch was ribbon geometry: v0.1 was too reactive, too vertically displaced, too thick during strong moves, and increasingly amplified on higher timeframes.

## Preserved v0.1 ribbon

The v0.1 Pine file is kept byte-for-byte unchanged in this release. v0.2 also contains the same geometry internally as:

`Ribbon Model = Flow Ribbon v0.1 (Legacy)`

This preserves the more reactive version as a valid alternative rather than deleting it.

## v0.2 default model — Control Surface

Default:

`Ribbon Model = Control Surface v0.2`

Key changes:

- POC/control line is separated from flow magnitude.
- `SMOOTH` is treated as a Wilder/SMMA-style control line for greater inertia.
- Ribbon body is one-sided around the control line:
  - bullish surface grows above a bottom POC;
  - bearish surface grows below a top POC.
- Direction switching still uses the v0.1 flow/state family to preserve timing.
- Flow magnitude is smoothed before it controls thickness.
- Side transitions are smoothed so the surface contracts through state changes instead of teleporting from one side to the other.
- ATR influence is damped to 20% by default to reduce HTF over-amplification.
- Thickness is itself smoothed and hard-bounded.
- Event markers are OFF by default during fidelity calibration.

## Reference Geometry mode

`HA Visual Mode = Reference Geometry`

This temporarily removes Deep Ocean/Aurora confidence coloring from the HA bodies. It is only for geometry comparison. `Project Colors` remains the normal default.

## First comparison run

Do not change defaults initially.

Capture the same BTCUSDT windows used for the v0.1 comparison:

- 1m
- 3m
- 5m
- 7m
- 15m
- 45m
- 1h
- 2h
- 4h
- 6h

For each timeframe, compare:

1. control-line vertical location;
2. whether green surface uses the control line as its lower boundary;
3. whether red surface uses the control line as its upper boundary;
4. thickness versus the protected reference;
5. smoothness at state transitions;
6. whether HTF surfaces remain proportionate;
7. whether state timing stayed close to v0.1/reference.

If geometry is still too large on HTF, tune `Surface Volatility Influence` before changing the flow engine. If geometry lags too much everywhere, tune `Surface Control Length` or `Surface Flow Inertia` before touching ADL mathematics.

## v0.2 defaults

- Surface Control Length: 14
- Surface Flow Inertia: 8
- Surface Side Transition: 3
- Surface Shape Smoothing: 5
- Surface Base Thickness: 5.0
- Surface Max Thickness: 8.0
- Surface Volatility Influence: 0.20
- Surface Momentum Distance Influence: 0.15
- Event Markers: OFF
- HA Visual Mode: Project Colors
