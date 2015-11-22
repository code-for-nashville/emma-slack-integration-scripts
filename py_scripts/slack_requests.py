#!/usr/bin/python
import requests.auth


def get_user_information():
    # get slack users
    params = {'token': 'xoxp-3766825449-3769790952-13168674784-829c9237a7'}
    response = requests.get('https://slack.com/api/users.list', params=params)
    slack_users = response.json()['members']

    # users to add to mailing list - must be an iterator
    return slack_users
