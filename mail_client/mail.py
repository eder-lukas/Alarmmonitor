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
            res.update({parts[0].strip() : parts[1].strip()})
        return res