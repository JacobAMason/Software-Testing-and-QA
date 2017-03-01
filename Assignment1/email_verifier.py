import re


class EmailVerifier:
    emailPattern = re.compile(r"^\w+[\w.]+@(\w+\.)+(\w\w\w)$")

    @staticmethod
    def is_valid_email(address):
        return bool(EmailVerifier.emailPattern.match(str(address)))
