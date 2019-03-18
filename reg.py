import re

REGEX_BANK = {}
REGEX_BANK['64BIT_LOWERCASE_HEX_STR'] = r'^[0-9a-f]{16}$'
REGEX_BANK['EXT_CSV'] = r'*.csv$'


def validate_token(pattern, token):
    matched = re.search(pattern, token)
    if matched:
        return True
    else:
        return False
# END validate_token()

def main():
    pass

if __name__ == '__main__':
    main()
