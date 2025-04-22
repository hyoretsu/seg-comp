import re
from .base import PatternStrategy


class PhoneStrategy(PatternStrategy):
    PHONE_RE = re.compile(r'\+?\d[\d\-\s\(\)]{7,}\d')

    def detect(self, text: str):
        matches = []

        for m in self.PHONE_RE.finditer(text):
            matches.append({
                'type': 'phone',
                'value': m.group().strip(),
                'start': m.start(),
                'end': m.end()
            })

        return matches
