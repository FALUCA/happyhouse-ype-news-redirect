"""Static checks for the versioned Apache redirect rules; not an Apache runtime test."""
import csv
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
RULES = (ROOT / '.htaccess').read_text(encoding='utf-8')


def resolve(path):
    for line in RULES.splitlines():
        line = line.strip()
        if not line.startswith('RewriteRule '):
            continue
        parts = line.split()
        match = re.fullmatch(parts[1], path.lstrip('/'))
        if match:
            destination = parts[2]
            for idx, value in enumerate(match.groups(), start=1):
                destination = destination.replace(f'${idx}', value or '')
            if destination.startswith('/'):
                destination = 'https://hhdigital.com.br' + destination
            return destination
    return None


class RedirectTests(unittest.TestCase):
    def test_expected_cases(self):
        with (ROOT / 'tests' / 'redirects.csv').open(newline='', encoding='utf-8') as f:
            for row in csv.DictReader(f):
                with self.subTest(path=row['source_path']):
                    self.assertEqual(resolve(row['source_path']), row['expected_location'])

    def test_no_edition_specific_rules(self):
        active = [line.strip() for line in RULES.splitlines() if line.strip().startswith("RewriteRule ")]
        self.assertEqual(len(active), 3)

    def test_unrelated_path_not_matched(self):
        self.assertIsNone(resolve('/clientes/outrocliente/index.html'))

    def test_permanent_redirect_flags(self):
        for line in RULES.splitlines():
            if line.strip().startswith('RewriteRule '):
                self.assertIn('R=301', line)


if __name__ == '__main__':
    unittest.main()
