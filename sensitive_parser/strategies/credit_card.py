import re
from .base import PatternStrategy


class CreditCardStrategy(PatternStrategy):
    CC_RE = re.compile(r'(?:\d[ -]*?){13,16}')

    def detect(self, text: str):
        matches = []

        for m in self.CC_RE.finditer(text):
            digits = re.sub(r'\D', '', m.group())

            if 13 <= len(digits) <= 16:
                matches.append({
                    'type': 'credit_card',
                    'value': digits,
                    'start': m.start(),
                    'end': m.end()
                })

        return matches
