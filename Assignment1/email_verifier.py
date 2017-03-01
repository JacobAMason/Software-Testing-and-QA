import re


class EmailVerifier:
    emailPattern = re.compile(r"^\w+[\w.]+@(\w+\.)+(\w{1,3})$")

    @staticmethod
    def is_valid_email(address):
        return bool(EmailVerifier.emailPattern.match(str(address)))
