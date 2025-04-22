import re


def normalize_text(raw: str) -> str:
    
    try:
        # transforma sequências \xNN, \n, \t, etc., em seus caracteres
        decoded = raw.encode('latin1').decode('unicode_escape')
    except Exception:
        decoded = raw

    # remove U+0000–U+001F, menos \n (0x0A), \t (0x09) e \b (0x08)
    cleaned = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', decoded)
    
    return cleaned
