import json
from sensitive_parser.parser import Parser

from sensitive_parser.strategies.phone import PhoneStrategy
from sensitive_parser.strategies.email import EmailStrategy
from sensitive_parser.strategies.credit_card import CreditCardStrategy
from sensitive_parser.strategies.social_flag import SocialFlagStrategy
from sensitive_parser.strategies.social_keyword import SocialKeywordStrategy


if __name__ == '__main__':

    sample = {
        # 1) Full e‑mail (regex padrão)
        "full_email": "user.one@domain.com",

        # 2) Fallback e‑mail + senha pós‑.com + ruído control code
        #    raw: "xxx+_@domai\x00n.commyP@ss"
        #    -> normaliza pra "xxx+_@domain.commyP@ss"
        "fallback_email": "xxx+_@domai\\x00n.commyP@ss",

        # 3) Social flags (case‑insensitive)
        "social_flags": "facebook - fb_user Instagram - InstaUsuário",

        # 4) Social keywords soltas
        "social_keywords": "Siga-me no twitter e linkedin e YOUTUBE para novidades",

        # 5) Cartão de crédito (13–16 dígitos, com espaços)
        "credit_card": "Número do cartão: 4111 1111 1111 1111",

        # 6) Telefones em formatos diferentes
        "phones": [
            "+55 (21) 98765-4321",
            "Ligue para 123-456-7890"
        ],

        # 7) Fallback e‑mail dentro de nó aninhado
        "nested": {
            "inner": "teste\\x0e@testdom.com1234senhaExtra"
        }
    }

    parser = Parser([
        EmailStrategy(),
        SocialFlagStrategy(),
        SocialKeywordStrategy(),
        CreditCardStrategy(),
        PhoneStrategy(),
    ])

    matches = parser.parse(sample)

    print(json.dumps(matches, indent=2, ensure_ascii=False))
