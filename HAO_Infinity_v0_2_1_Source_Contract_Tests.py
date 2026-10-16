from pathlib import Path
import hashlib
import re
import unittest

ROOT = Path('/mnt/data')
BASE = ROOT / 'HAO_Infinity_Reconstruction_Lab_v0_2.pine'
NEW = ROOT / 'HAO_Infinity_Reconstruction_Lab_v0_2_1.pine'
EXPECTED_BASE_SHA = (ROOT / 'HAO_v0_2_SHA256.txt').read_text().split()[0]

class TestHAOv021(unittest.TestCase):
    def source(self):
        self.assertTrue(NEW.exists(), 'v0.2.1 Pine file has not been created yet')
        return NEW.read_text(encoding='utf-8')

    def test_v02_is_preserved_byte_for_byte(self):
        actual = hashlib.sha256(BASE.read_bytes()).hexdigest()
        self.assertEqual(actual, EXPECTED_BASE_SHA)

    def test_version_and_three_ribbon_models(self):
        s = self.source()
        self.assertIn('Reconstruction Lab v0.2.1', s)
        self.assertRegex(s, r'ribbonModel\s*=\s*input\.string\("Control Surface v0\.2\.1')
        for name in ['Control Surface v0.2.1', 'Control Surface v0.2', 'Flow Ribbon v0.1 (Legacy)']:
            self.assertIn(name, s)

    def test_memory_state_requires_acceptance_and_confirmation(self):
        s = self.source()
        for token in ['surfaceAcceptanceBars', 'surfaceAcceptanceBuffer', 'bullAccepted', 'bearAccepted', 'ribbonStateMemory']:
            self.assertIn(token, s)
        self.assertRegex(s, r'ribbonStateMemory\s*:=\s*barstate\.isconfirmed')
        self.assertIsNotNone(re.search(r'bullAccepted.*ribbonStateMemory|ribbonStateMemory.*bullAccepted', s, re.S))
        self.assertIsNotNone(re.search(r'bearAccepted.*ribbonStateMemory|ribbonStateMemory.*bearAccepted', s, re.S))

    def test_attack_decay_thickness_memory_exists(self):
        s = self.source()
        for token in ['surfaceAttackLength', 'surfaceDecayLength', 'f_attack_decay', 'surfaceThicknessMemory']:
            self.assertIn(token, s)
        self.assertRegex(s, r'target\s*>?=\s*(?:previous|safePrev)')

    def test_hud_is_tiny_four_line_guide_by_default(self):
        s = self.source()
        self.assertIn('HAO Guide HUD', s)
        self.assertRegex(s, r'hudMode\s*=\s*input\.string\("Guide"')
        self.assertRegex(s, r'hudTransparency\s*=\s*input\.int\(88')
        self.assertRegex(s, r'table\.new\([^\n]*2,\s*4')
        for label in ['MARKET', 'LIQUIDITY', 'MOMENTUM', 'WATCH']:
            self.assertIn(f'"{label}"', s)
        self.assertIn('text_size = size.tiny', s)
        self.assertIn('text_color = color.white', s)

    def test_hud_language_explains_market_in_plain_english(self):
        s = self.source()
        phrases = [
            'Bull structure', 'Bear structure', 'support', 'resistance',
            'Momentum rising', 'Momentum falling', 'confirms reversal', 'No clear edge'
        ]
        for phrase in phrases:
            self.assertIn(phrase, s)

    def test_candle_palette_defaults_to_deep_ocean_and_keeps_black_flag(self):
        s = self.source()
        self.assertRegex(s, r'candlePalette\s*=\s*input\.string\("Deep Ocean Adaptive"')
        for name in ['Deep Ocean Adaptive', 'Black Flag', 'Aurora', 'Classic', 'Custom', 'Reference Geometry']:
            self.assertIn(name, s)
        self.assertIn('f_candle_palette_color', s)
        # Dark graphite + muted burgundy/teal families should be explicit, not aliases of Aurora.
        self.assertIn('color.rgb(45, 43, 50)', s)
        self.assertIn('color.rgb(145, 24, 74)', s)
        self.assertIn('color.rgb(84, 151, 132)', s)

if __name__ == '__main__':
    unittest.main(verbosity=2)
