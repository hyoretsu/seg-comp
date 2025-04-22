import re
from .base import PatternStrategy


class SocialKeywordStrategy(PatternStrategy):
    KEYWORDS = ['facebook', 'instagram', 'twitter', 'linkedin', 'youtube']

    def detect(self, text: str):
        results = []

        for kw in self.KEYWORDS:
            for m in re.finditer(kw, text, re.IGNORECASE):
                results.append({
                    'type': 'social_keyword',
                    'platform': kw,
                    'start': m.start(),
                    'end': m.end()
                })

        return results
