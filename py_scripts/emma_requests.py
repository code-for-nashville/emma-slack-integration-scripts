#!/usr/bin/python
import json
import requests

from auth_settings import auth_settings


def post_emails_to_emma(users):
    # transform each user into fields needed by emma
    for user in users:
        profile = user['profile']

        email = profile.get('email', '')
        fields = {
            'first_name': profile.get('first_name', ''),
            'last_name': profile.get('last_name', '')
        }
        groups = [1116425]

        user_details = {
            'email': email,
            'fields': fields,
            'group_ids': groups
        }

        keys = auth_settings()

        auth_data = requests.auth.HTTPBasicAuth(
            keys['pub_api'],
            keys['priv_api']
        )

        url = "https://api.e2ma.net/{}/members/add".format(keys['acc_id'])

        # Push each user to Emma if they have an email
        if email:
            request = requests.post(url, data=json.dumps(user_details), auth=auth_data)

            print(request.status_code)
        else:
            print 'no email - not sent'

    print 'all sent!'
