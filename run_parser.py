import json
from sensitive_parser.parser import Parser

from sensitive_parser.strategies.phone import PhoneStrategy
from sensitive_parser.strategies.email import EmailStrategy
from sensitive_parser.strategies.credit_card import CreditCardStrategy
from sensitive_parser.strategies.social_flag import SocialFlagStrategy
from sensitive_parser.strategies.social_keyword import SocialKeywordStrategy


if __name__ == '__main__':

    sample = {
  "concatenatedKeys": "^_l\\x0easdasdsadasdasdsadasdasdas^_l\\x01hyoretsu+_@gmai\tsem^_l\b\b\n\nasdasd\n\nhyoretsu+_@gmail.com\nasdasdas\nhyoretsu+_@gmail.com\tsenhafalha"}
              
    parser = Parser([
        EmailStrategy(),
        SocialFlagStrategy(),
        SocialKeywordStrategy(),
        CreditCardStrategy(),
        PhoneStrategy(),
    ])

    matches = parser.parse(sample)

    print(json.dumps(matches, indent=2, ensure_ascii=False))
