import re
from .base import PatternStrategy


class SocialFlagStrategy(PatternStrategy):
    FLAG_RE = re.compile(
        r'(facebook|instagram)\s*-\s*(.+)',
        re.IGNORECASE
    )

    def detect(self, text: str):
        matches = []

        for m in self.FLAG_RE.finditer(text):
            matches.append({
                'type': 'social_flag',
                'platform': m.group(1).lower(),
                'segment': m.group(2),
                'start': m.start(),
                'end': m.end()
            })

        return matches
