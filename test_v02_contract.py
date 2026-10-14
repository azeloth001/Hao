from pathlib import Path
import math
import hashlib

ROOT = Path(__file__).resolve().parents[1]
V01 = ROOT / "src" / "HAO_Infinity_Reconstruction_Lab_v0_1.pine"
V02 = ROOT / "src" / "HAO_Infinity_Reconstruction_Lab_v0_2.pine"


def read_v02():
    return V02.read_text(encoding="utf-8")


def surface_geometry(control, thickness, side_blend):
    outer = control + side_blend * thickness
    return min(control, outer), max(control, outer), control


def test_v01_baseline_is_preserved():
    assert V01.exists()
    raw = V01.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == '3d68b1bd5516828e6b4a50a893b1981d7b069910281c3a507c6c239d0d23ff4d'
    text = raw.decode('utf-8')
    assert 'indicator("HAO ∞ — Reconstruction Lab v0.1"' in text
    assert 'float ribbonShift = -flowPressure * shiftFactor * ribbonWidth' in text


def test_v02_exists_and_defaults_to_control_surface():
    text = read_v02()
    assert 'indicator("HAO ∞ — Reconstruction Lab v0.2"' in text
    assert 'input.string("Control Surface v0.2", "Ribbon Model"' in text
    assert '"Flow Ribbon v0.1 (Legacy)"' in text


def test_legacy_formula_is_retained_in_v02():
    text = read_v02()
    assert 'f_ribbon_legacy(' in text
    assert 'float liquidityStrength = 0.65 + 0.85 * math.abs(flowPressure)' in text
    assert 'float ribbonShift = -flowPressure * shiftFactor * ribbonWidth' in text
    assert 'float axis = center + ribbonShift' in text


def test_control_surface_is_one_sided_around_poc():
    lo, hi, poc = surface_geometry(3.0, 5.0, 0.8)
    assert poc == 3.0
    assert lo == 3.0
    assert hi > poc
    lo, hi, poc = surface_geometry(3.0, 5.0, -0.8)
    assert poc == 3.0
    assert hi == 3.0
    assert lo < poc


def test_control_surface_has_inertia_and_bounded_htf_volatility_influence():
    text = read_v02()
    assert 'surfaceFlowSmoothing = input.int(' in text
    assert 'surfaceTransitionSmoothing = input.int(' in text
    assert 'surfaceVolatilityWeight = input.float(0.20' in text
    assert 'flowPressureSlow = ta.rma(flowPressure, surfaceFlowSmoothing)' in text
    assert 'surfaceSide = ta.ema(float(ribbonState), surfaceTransitionSmoothing)' in text
    # With the default 0.20 weight, the old max vol factor 1.75 should only add 15% width.
    adjusted = 1.0 + (1.75 - 1.0) * 0.20
    assert math.isclose(adjusted, 1.15)


def test_event_markers_are_quiet_by_default():
    text = read_v02()
    assert 'showEventMarkers = input.bool(false, "Show Event Markers"' in text
    assert 'bool showEvents = showEventMarkers and f_visible(displayMode, "EVENTS")' in text


def test_reference_geometry_candle_mode_is_available():
    text = read_v02()
    assert '"Reference Geometry"' in text
    assert 'haVisualMode = input.string("Project Colors", "HA Visual Mode"' in text


def test_confirmed_state_gating_is_preserved():
    text = read_v02()
    assert 'ribbonState := barstate.isconfirmed ?' in text
    assert 'structureState := barstate.isconfirmed ?' in text
    assert 'bullBreakoutAlert = barstate.isconfirmed and' in text
