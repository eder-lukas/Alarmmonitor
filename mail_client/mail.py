KEYWORD_STRASSE='Strasse'
KEYWORD_HAUSNUMMER='Hausnummer'
KEYWORD_PLZ='PLZ'
KEYWORD_ORT='Ort'
KEYWORD_ADRESSE='Adresse'
KEYWORD_LATITUDE='Latitude'
KEYWORD_LONGITUDE='Longitude'
KEYWORD_SEPARATOR=';'

class Mail:
    def __init__(self, sender, subject, content):
        self.sender = sender
        self.subject = subject
        self.content = content
    

    def parse_content(self) -> dict:
        content = self._get_content_into_dict()
        content = self._summarize_address(content)
        return content
    
    
    def _get_content_into_dict(self) -> dict:
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


    def _summarize_address(self, content: dict) -> dict:
        """
        this method summarizes the address. It takes street, house number, postal code and city together
        """
        street, house_number, postal_code, city = None, None, None, None

        for key, value in content.items():
            if key == KEYWORD_STRASSE:
                street = value
            elif key == KEYWORD_HAUSNUMMER:
                house_number = value
            elif key == KEYWORD_PLZ:
                postal_code = value
            elif key == KEYWORD_ORT:
                city = value

        address = ''
        if street:
            address = address + street + " "
            del content[KEYWORD_STRASSE]
        if house_number:
            address = address + house_number + " "
            del content[KEYWORD_HAUSNUMMER]
        if postal_code:
            address = address + postal_code + " "
            del content[KEYWORD_PLZ]
        if city:
            address = address + city
            del content[KEYWORD_ORT]

        content = self._insert_address_in_pos(content, address, 3)
        return content

    def _insert_address_in_pos(self, content: dict, address, pos) -> dict:
        res = {}
        i = 0
        for key, value in content.items():
            if i == pos:
                res[KEYWORD_ADRESSE] = address
                i += 1
            res[key] = value
            i += 1
        return res
    
    """
    Returns the content dict without latitude and longitude and the latitude and longitude in the original (str) fromat
    """
def extract_coordinates_from_content(content: dict):
    res_dict = {}
    latitude = ""
    longitude = ""
    for key, value in content.items():
        if key == KEYWORD_LATITUDE:
            latitude = value
        elif key == KEYWORD_LONGITUDE:
            longitude = value
        else:
            res_dict.update({key : value})
    return res_dict, latitude, longitude