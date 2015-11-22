import emma_requests
import slack_requests


def post_all_slack_emails_to_emma():
    members = slack_requests.get_user_information()

    emma_requests.post_emails_to_emma(members)

if __name__ == '__main__':
    post_all_slack_emails_to_emma()
