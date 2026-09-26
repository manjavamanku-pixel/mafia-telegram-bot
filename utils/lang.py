from locales.uz import STRINGS as uz_strings

def t(lang: str, key: str, **kwargs) -> str:
    text = uz_strings.get(key, key)
    if kwargs and isinstance(text, str):
        try:
            text = text.format(**kwargs)
        except:
            pass
    return text
