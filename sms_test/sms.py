import json
import os
import sys

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

CONF_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.conf')

conf = json.loads(open(os.path.join(CONF_DIR, 'settings_local.json')).read())

api_key = conf["sms"]["api_key"]
api_secret = conf["sms"]["api_secret"]

to_number = '01086342373'
from_num = conf["sms"]["sender_number"]
message = "영나 열공하자"
image = "../images/img1.jpeg"




params = {
    'type': 'sms',
    'to': to_number,
    'from': from_num,
    'text': message,
}
cool = Message(api_key, api_secret)

try:
    response = cool.send(params)
    print("Success Count : %s" % response['success_count'])
    print("Error Count : %s" % response['error_count'])
    print("Group ID : %s" % response['group_id'])

    if "error_list" in response:
        print("Error List : %s" % response['error_list'])

except CoolsmsException as e:
    print("Error Code : %s" % e.code)
    print("Error Message : %s" % e.msg)

sys.exit()
