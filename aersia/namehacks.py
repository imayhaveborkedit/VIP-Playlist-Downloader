from re import sub

conversions = {
    # trailing dot
    '\.{2,}m4a': '.m4a',

    # extra spaces
    '\s{2,}': ' ',

    # .dothack
    '^\.hack': 'dothack',
    '^dothack': 'dothack - ', # Maybe this is what I wanted?
    # '^dothack\S': 'dothack - ', # kasdjfkajsbdflkbsadf

    # Original Version despacing & parenthesizing
    '  Original Version': ' (Original Version)',

    # Double space to dash
    '\s\s': ' - ',

    # Pokemon name fixing
    'TimeDarknessSky': 'Time-Darkness-Sky',
    'RedBlueYellow': 'Red-Blue-Yellow',
    'GoldSilverCrystal': 'Gold-Silver-Crystal',
    'BlackWhite': 'Black & White',

    # Ecco vocal remix
    'MaskVocal Remix': 'Mask (Vocal Remix)',

    # FFVII X'mas edit
    "  X'mas Edit": " (X'mas Edit)"
}

def apply(text):
    for hacks in conversions:
        text = sub(hacks, conversions[hack], text)
    return text
