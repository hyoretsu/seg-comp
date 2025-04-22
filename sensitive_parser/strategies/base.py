from abc import ABC, abstractmethod
from typing import Any, Dict, List

Match = Dict[str, Any]


class PatternStrategy(ABC):
    @abstractmethod
    def detect(self, text: str) -> List[Match]:
        """Retorna lista de matches encontrados no texto."""
        ...
