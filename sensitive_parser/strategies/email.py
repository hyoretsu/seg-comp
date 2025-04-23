import re
from .base import PatternStrategy


class EmailStrategy(PatternStrategy):

    EMAIL_RE = re.compile(
        r'[\w\.-]+@[\w\.-]+\.(?:com|net|org|edu)', 
        re.IGNORECASE
    )

    def detect(self, text: str):
        matches = []

        for m in self.EMAIL_RE.finditer(text):
            matches.append({
                'type': 'email',
                'value': m.group(),
                'start': m.start(),
                'end': m.end(),
                'password': None  # sem senha extra nessa rota
            })

        # Fallback: procurar '@' que não entrou na regex
        for at_pos in [m.start() for m in re.finditer(r'@', text)]:

            prefix_start = max(0, at_pos - 10)
            segment = text[prefix_start:]

            idx_com = segment.lower().find('.com')
            if idx_com == -1:
                continue

            com_end = prefix_start + idx_com + len('.com')

            raw_email = text[prefix_start:com_end]

            if raw_email.find('@') <= 0:
                continue

            rest = text[com_end:]
            pwd_match = re.match(r'(\S+)', rest)
            password = pwd_match.group(1) if pwd_match else None

            matches.append({
                'type': 'email_fallback',
                'value': raw_email,
                'start': prefix_start,
                'end': com_end + (len(password) if password else 0),
                'password': password
            })

        return matches
