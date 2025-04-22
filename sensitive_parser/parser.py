from typing import Any, List

from .utils import normalize_text

from .strategies.phone import PhoneStrategy
from .strategies.email import EmailStrategy
from .strategies.base import PatternStrategy
from .strategies.credit_card import CreditCardStrategy
from .strategies.social_flag import SocialFlagStrategy
from .strategies.social_keyword import SocialKeywordStrategy


class Parser:
    def __init__(self, strategies: List[PatternStrategy] = None):
        # carrega strategies padrão se não informado
        self.strategies = strategies or [
            EmailStrategy(),
            SocialFlagStrategy(),
            SocialKeywordStrategy(),
            CreditCardStrategy(),
            PhoneStrategy(),
        ]

    def parse(self, data: Any) -> List[dict]:
        results: List[dict] = []
        self._traverse(data, [], results)
        return results

    def _traverse(self, node: Any, path: List[Any], results: List[dict]):
        # Import dinâmico para evitar ciclo

        if isinstance(node, dict):
            for k, v in node.items():
                self._traverse(v, path + [k], results)

        elif isinstance(node, list):
            for idx, item in enumerate(node):
                self._traverse(item, path + [idx], results)

        elif isinstance(node, str):
            # <-- Aqui aplicamos o pós‑processamento
            text = normalize_text(node)

            # 1) Aplica todas as strategies no texto limpo
            for strat in self.strategies:
                for match in strat.detect(text):
                    match['path'] = list(path)
                    results.append(match)

            # 2) Se houver flag de social, aplica de novo no segmento
            for m in SocialFlagStrategy.FLAG_RE.finditer(text):
                segmento = m.group(2)
                for strat in self.strategies:
                    for sub in strat.detect(segmento):
                        sub['path'] = list(path)
                        sub['flag_context'] = m.group(1).lower()
                        results.append(sub)
        # int, float, None, etc. são ignorados
