class Mail:
    def __init__(self, sender, subject, content):
        self.sender = sender
        self.subject = subject
        self.content = content

    def parse_content(self) -> dict:
        res = {}
        lines = self.content.splitlines()
        for line in lines:
            parts = line.split(":")
            if (len(parts) >= 2): # to avoid printing lines without a keyword and a value
                if (len(parts[1].strip()) >= 1): # to filter empty values
                    res.update({parts[0].strip() : parts[1].strip()})
        return res