# MakerSpell Translations

Community translations for the MakerSpell Android app.
English (`flutter/app_en.arb`) is the source of truth. Every other language lives in its own file next to it.

## Add or fix a language

1. Copy `flutter/app_en.arb` to `flutter/app_XX.arb`, where `XX` is your language code (use `pt_BR` style for regions).
2. Translate only the text after the colon. Leave everything else untouched:
   - key names on the left,
   - `{placeholders}` in curly braces, exactly as they are,
   - lines starting with `@`, they are metadata, not text.
3. Check your file is still valid JSON.
4. Open a pull request. An automatic check validates JSON and placeholder parity with English.

No GitHub account? Email your file to support@makerspell.com with the language name and we will add it for you.

## License of contributions

By submitting a translation you agree it may be shipped in MakerSpell under the same terms as the app.

## Files

- `flutter/` - Android app strings, one `.arb` file per language.
- `tools/check_translations.py` - the same validation the CI runs, so you can check locally.
