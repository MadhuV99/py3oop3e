# mailing_list.py
from contextlib import suppress
from collections import defaultdict
import smtplib
from email.mime.text import MIMEText

class MailingList:
    """Manage groups of e-mail addresses for sending e-mails.
       In another terminal, run:
            python -m smtpd -n -c DebuggingServer localhost:1025
    """

    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails

    def send_mailing(
        self, subject, message, from_addr, *groups, headers=None
    ):
        emails = self.emails_in_groups(*groups)
        send_email(
            subject, message, from_addr, *emails, headers=headers
        )

    def save(self):
        with open(self.data_file, "w") as file:
            for email, groups in self.email_map.items():
                file.write("{} {}\n".format(email, ",".join(groups)))

    def load(self):
        self.email_map = defaultdict(set)
        with suppress(IOError):
            with open(self.data_file) as file:
                for line in file:
                    email, groups = line.strip().split(" ")
                    groups = set(groups.split(","))
                    self.email_map[email] = groups

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()

def send_email(
    subject,
    message,
    from_addr,
    *to_addrs,
    host="localhost",
    port=1025,
    headers=None
):
    headers = headers if headers else {}

    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = from_addr
    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host, port)
    for addr in to_addrs:
        del email["To"]
        email["To"] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()

def main():
    # send_email("A model subject", "The message contents",
    #             "from@example.com", "to1@example.com", "to2@example.com")

    # m = MailingList()
    # m.send_mailing("A Party",
    #         "Friends and family only: a party", "me@example.com", "friends",
    #         "family", headers={"Reply-To": "me2@example.com"})
    
    # m = MailingList('addresses.db')
    # print(m.email_map)
    # m.load()
    # print(m.email_map)
    # m.add_to_group("friend1@example.com", "friends")
    # m.add_to_group("friend2@example.com", "friends")
    # m.add_to_group("family1@example.com", "family")
    # m.add_to_group("pro1@example.com", "professional")
    # m.add_to_group('family1@example.com', 'friends')
    # print(m.email_map)
    # m.save()

    with MailingList('addresses.db') as ml:
        ml.add_to_group('friend3@example.com', 'friends')
        ml.send_mailing("What's up", "hey friends, how's it going",
                        'me@example.com',
                        'friends')

if __name__ == '__main__':
    main()
