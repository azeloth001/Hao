# HAO ∞ — Heiken Ashi Oscillator / Adaptive Liquidity Engine

> **Clean-room Pine Script v6 research project for TradingView**  
> Reconstructing and evolving a Heiken-Ashi / RSI oscillator concept into a more adaptive liquidity and market-structure engine.

---

## Overview

**HAO ∞** is a Pine Script v6 oscillator project built around a zero-centered RSI, custom Heiken-Ashi momentum candles, adaptive liquidity support/resistance surfaces, and structural market-state logic.

The project began as a **clean-room reconstruction experiment** based only on publicly visible behavior, screenshots, exposed settings, and public descriptions of a protected TradingView indicator.

No protected source code was used or recovered.

The long-term goal is not to clone the original indicator, but to use the reconstruction as a **research baseline** and then evolve it into a stronger independent system.

---

## Project Philosophy

HAO ∞ follows a simple development rule:

> **Reconstruct first. Understand second. Improve third.**

The project intentionally separates three stages:

1. **Fidelity** — reproduce the observable behavior as closely as practical.
2. **Calibration** — compare against reference behavior across multiple symbols and timeframes.
3. **Evolution** — add original adaptive logic only after the baseline is understood.

This prevents new features from hiding mistakes in the core mathematics.

---

## Current Status

### v0.1 — Reconstruction Lab

The first working baseline introduced:

- Pine Script v6
- Zero-centered RSI
- RSI moving average
- Oscillator-space Heiken-Ashi candles
- ADL / accumulation-distribution pressure
- ATR normalization
- Adaptive liquidity ribbon
- Point of Control / Control Line
- Breakout and failed-break states
- Continuation states
- Compression logic
- Structure-aware candle coloring
- Deep Ocean theme
- Aurora theme
- Focus / Clean / Research / Diagnostic display modes

The v0.1 ribbon showed unexpectedly useful behavior on several timeframes, so it has been preserved permanently as a legacy engine.

### v0.2 — Control Surface Calibration

v0.2 focuses primarily on improving the liquidity structure.

The major change is a new **one-sided liquidity surface** model.

Instead of behaving like a symmetric displaced channel:

- **Bull state:** POC / Control Line acts as the lower support boundary and the liquidity surface grows upward from it.
- **Bear state:** POC / Control Line acts as the upper resistance boundary and the liquidity surface grows downward from it.

Other v0.2 changes include:

- slower POC / Control Line
- stronger S/R inertia
- smoother flow magnitude
- compressed ribbon amplitude
- reduced higher-timeframe volatility amplification
- smoother state transitions
- bounded ribbon thickness
- cleaner Focus mode
- Reference Geometry candle mode for calibration

---

## Ribbon Models

HAO ∞ currently contains two ribbon engines.

### `Control Surface v0.2`

The default research model.

Designed to behave more like a persistent oscillator support/resistance structure rather than a fast-moving channel.

### `Flow Ribbon v0.1 (Legacy)`

The original reconstruction ribbon.

This model is intentionally preserved because it showed its own useful behavior, especially on some short and medium timeframes.

It remains selectable inside v0.2 and is also archived separately.

---

## Core Oscillator

The main coordinate system is:

```text
Centered RSI = RSI - 50
```

| Centered value | Normal RSI |
|---:|---:|
| +30 | 80 |
| +10 | 60 |
| 0 | 50 |
| -10 | 40 |
| -30 | 20 |

Defaults:

```text
RSI Length: 14
RSI MA: SMA 14
```

---

## Heiken-Ashi Oscillator

HAO ∞ builds Heiken-Ashi-style candles directly in oscillator space.

The project currently uses **Model A** as the main calibration model:

```text
RSI(open)
RSI(high)
RSI(low)
RSI(close)
```

Each component is centered around zero before the HA transformation is applied.

Experimental alternative source models are kept for research and comparison.

---

## Liquidity / Flow Engine

The flow engine uses a Chaikin-style accumulation/distribution foundation.

Conceptually:

```text
Price location inside candle
        ↓
Money Flow Multiplier
        ↓
Volume-weighted flow
        ↓
Accumulation / Distribution
        ↓
Flow velocity
        ↓
Normalization
        ↓
Liquidity pressure
```

The normalized pressure is not plotted directly.

It influences:

- liquidity direction
- ribbon state
- surface thickness
- structural conviction
- support/resistance behavior

---

## Control Line / POC

The **Point of Control / Control Line** is treated as the most important liquidity boundary.

In v0.2:

```text
Bull state:
POC = lower support boundary

Bear state:
POC = upper resistance boundary
```

The control line is intentionally slower than the oscillator so momentum can attack, reject, break, and retest the liquidity structure instead of having the structure simply follow price.

---

## Structural States

HAO ∞ currently recognizes states such as:

```text
RANGE
BULL_BREAKOUT
BEAR_BREAKOUT
FAILED_BULL_BREAK
FAILED_BEAR_BREAK
BULL_CONTINUATION
BEAR_CONTINUATION
COMPRESSION
TRANSITION
```

Heiken-Ashi candle personality also tracks:

```text
BULL_IMPULSE
BULL_HOLD
BULL_WEAKENING
NEUTRAL
BEAR_WEAKENING
BEAR_HOLD
BEAR_IMPULSE
```

The goal is for candle color to represent more than simply:

```text
HA close > HA open
```

---

## Themes

### Deep Ocean

Bull family:

```text
Deep teal
Aqua
Electric turquoise
```

Bear family:

```text
Deep burgundy
Crimson
Red-orange
```

### Aurora

Bull family:

```text
Green
Lime
Cyan
```

Bear family:

```text
Magenta
Coral
Crimson
```

Transition states use blue/violet tones.

---

## Display Modes

### Focus
Primary trading view with minimal clutter.

### Clean
Reduced visual load.

### Research
Exposes additional internal calculations.

### Diagnostic
Used for development and calibration.

Useful diagnostics include:

- centered RSI
- HA close
- money-flow multiplier
- ADL velocity
- normalized flow
- ATR factor
- ribbon center
- ribbon width
- ribbon shift
- POC
- event state
- structure state
- structure confidence
- compression score

---

## Suggested Repository Structure

```text
HAO-Infinity/
│
├── README.md
│
├── src/
│   ├── HAO_Infinity_Reconstruction_Lab_v0_2.pine
│   └── HAO_Infinity_Reconstruction_Lab_v0_1_LEGACY.pine
│
├── docs/
│   ├── HAO_Infinity_v0_2_Calibration_Notes.md
│   ├── HAO_Infinity_v0_2_Test_Matrix.md
│   └── development/
│       ├── HAO_Infinity_Design_Spec.md
│       └── HAO_Infinity_v0_1_Implementation_Plan.md
│
└── screenshots/
    ├── reference/
    └── comparisons/
```

---

## Installation

1. Open TradingView.
2. Open **Pine Editor**.
3. Create a new indicator.
4. Paste the contents of:

```text
HAO_Infinity_Reconstruction_Lab_v0_2.pine
```

5. Save.
6. Add to chart.

Recommended initial settings:

```text
Ribbon Model: Control Surface v0.2
Theme: Deep Ocean
Display Mode: Focus
RSI Length: 14
RSI MA: SMA 14
HA Source Model: Model A
S/R MA: SMOOTH
```

Do not tune calibration parameters immediately.

The project is currently still in the reconstruction/calibration phase.

---

## Recommended Calibration Timeframes

The current comparison set uses:

```text
1m
3m
5m
7m
15m
45m
1h
2h
4h
6h
```

BTCUSDT has been the primary research market.

The purpose of multi-timeframe testing is not to optimize every timeframe independently, but to find mathematics that remain structurally coherent across all of them.

---

## Development Roadmap

### v0.2.x — Ribbon Calibration

Current focus:

- Control Line inertia
- ribbon thickness
- state-transition timing
- HTF scaling
- one-sided surface geometry
- comparison against reference behavior

### v0.3 — Structural Calibration

Planned work:

- refine HA structural coloring
- improve failed-break logic
- improve continuation logic
- acceptance / rejection states
- improve compression release behavior

### v0.4 — Visual Refinement

Planned work:

- Deep Ocean refinement
- Aurora refinement
- cleaner mobile presentation
- conviction-weighted intensity
- optional reference-style visual mode

### v1.0 — HAO ∞

Only after the reconstruction core is stable.

Potential future research:

- adaptive smoothing
- lower-timeframe turning awareness
- higher-timeframe structural anchors
- multi-timeframe regime context
- divergence
- dynamic confidence scoring
- liquidity compression / expansion
- acceptance / rejection memory
- signal quality routing
- optional integration of ideas developed in other independent oscillator projects

---

## Development Rule

New features are not accepted simply because they look useful.

A feature should answer at least one of these questions:

```text
Does it improve timing?
Does it improve structural clarity?
Does it reduce false interpretation?
Does it expose useful information not already present?
Does it remain useful across multiple timeframes?
```

If not, it does not belong in HAO ∞.

---

## Important Notes

HAO ∞ is currently a **research indicator**.

It is not a finished trading system and does not provide financial advice.

Signals, states, colors, and liquidity structures should be independently tested before being used in live trading.

---

## Clean-Room Notice

This project was created independently.

The original inspiration is a protected-source TradingView indicator whose public screenshots, public descriptions, visible settings, and observable behavior were used as research references.

No protected source code was accessed, copied, decompiled, or reproduced.

HAO ∞ uses independently designed formulas and architecture.

The project is intended to evolve beyond the original reference concept.

---

## License

No license has been selected yet.

Before making the repository public, choose a license that matches the intended use of the project.

Common options include:

- MIT
- Apache-2.0
- GPL-3.0
- All Rights Reserved / private research repository

---

## Project Status

```text
Current development version: v0.2
Stage: Reconstruction / Calibration
Primary market: BTCUSDT
Primary platform: TradingView
Language: Pine Script v6
Default theme: Deep Ocean
```

---

## Final Goal

HAO ∞ is not intended to become another indicator with dozens of disconnected features.

The goal is a single coherent visual engine where:

```text
Momentum
+
Heiken-Ashi structure
+
Liquidity
+
Support / Resistance
+
Compression / Expansion
+
Market acceptance / rejection
```

tell one consistent story.

**The original indicator was the starting point — not the destination.**
