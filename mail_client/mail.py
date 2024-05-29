KEYWORD_STRASSE='Strasse'
KEYWORD_HAUSNUMMER='Hausnummer'
KEYWORD_PLZ='PLZ'
KEYWORD_ORT='Ort'
KEYWORD_SEPARATOR=';'

class Mail:
    def __init__(self, sender, subject, content):
        self.sender = sender
        self.subject = subject
        self.content = content
    
    def parse_content(self) -> dict:
        last_keyword = None
        res = {}
        lines = self.content.splitlines()
        for line in lines:
            if '***' in line:
                continue
            if KEYWORD_SEPARATOR in line: # new line with new keyword
                parts = line.split(KEYWORD_SEPARATOR)
                if (len(parts[1].strip()) >= 1): # to filter empty values
                    res.update({parts[0].strip() : parts[1].strip()})
                    last_keyword = parts[0].strip()
            else: # new line without keyword -> if there is some content, append it to the last keyword
                if len(line.strip()) == 0:
                    continue
                if last_keyword:
                    existing_content = res.get(last_keyword)
                    new_content = existing_content + '\n' + line
                    res.update({last_keyword : new_content})
        return res


def get_address_from_content(content: dict) -> str:
    address = ''
    for key, value in content.items():
        if key == KEYWORD_STRASSE:
            address = value
        elif key == KEYWORD_HAUSNUMMER: 
            address = address + " " + value
        elif key == KEYWORD_PLZ:
            address = address + ", " + value
        elif key == KEYWORD_ORT:
            address = address + " " + value
    return address