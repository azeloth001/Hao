# HAO ∞ v0.2 Test Matrix

## Automated local contract checks

- [x] v0.1 source remains archived and unchanged.
- [x] v0.2 defaults to Control Surface v0.2.
- [x] v0.1 ribbon formula remains selectable inside v0.2.
- [x] v0.2 geometry is one-sided around POC/control line.
- [x] slow flow and side-transition inertia are present.
- [x] default volatility influence limits the old 1.75 ATR factor to a 1.15 geometry multiplier before other clamps.
- [x] event markers are off by default.
- [x] Reference Geometry candle mode exists.
- [x] bar-close state/alert gates remain present.

## TradingView gate — still required

- [ ] Pine v6 compilation.
- [ ] No runtime error on BTCUSDT.
- [ ] Control Surface screenshots on 1m/3m/5m/7m/15m/45m/1h/2h/4h/6h.
- [ ] Legacy mode visually reproduces v0.1 behavior.
- [ ] Reference Geometry mode renders cleanly.
- [ ] No historical event movement after reload.
