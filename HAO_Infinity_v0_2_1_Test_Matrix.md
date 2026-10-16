# HAO ∞ v0.2.1 — Test Matrix

## Local source-contract verification

- [x] v0.2 file remains byte-for-byte unchanged.
- [x] v0.2.1 is the default ribbon model.
- [x] v0.2 and v0.1 remain selectable.
- [x] memory state changes are gated by confirmed-bar acceptance.
- [x] attack/decay surface thickness memory exists.
- [x] Guide HUD defaults ON with tiny text and 88 transparency.
- [x] HUD has exactly four semantic rows.
- [x] Deep Ocean Adaptive is the default candle palette.
- [x] Black Flag / Aurora / Classic / Custom / Reference palettes remain selectable.

## TradingView compiler gate

- [ ] Paste v0.2.1 into Pine Editor.
- [ ] Confirm Pine Script v6 compilation with zero errors.
- [ ] Confirm table positions work on mobile and desktop.
- [ ] Confirm HUD does not overlap Diagnostic table.

## Realtime / replay gate

- [ ] Ribbon role changes only after closed-bar acceptance.
- [ ] Historical role changes remain stable after reload.
- [ ] Thickness expands faster than it decays.
- [ ] Opposing flow weakens the current ribbon before role reversal.
- [ ] v0.2 and v0.1 selectors reproduce their expected prior behavior.

## Visual gate

- [ ] Deep Ocean Adaptive: neutral states appear dark, confidence brightens bull/bear states.
- [ ] Black Flag: muted teal and burgundy/wine appearance is distinct from Deep Ocean.
- [ ] HUD remains readable at tiny size on phone.
- [ ] HUD white text remains legible over all semantic backgrounds.
- [ ] Event markers remain off by default.
