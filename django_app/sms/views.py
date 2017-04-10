import json
import os

from django.shortcuts import render, redirect
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

from sms import forms


def text_send_view(request):
    if request.method == 'POST':
        form = forms.MessageForm(request.POST)
        if form.is_valid():

            message = request.POST["text"]

            to_number = form.cleaned_data['to_number']

            CONF_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                                    '.conf')
            conf = json.loads(open(os.path.join(CONF_DIR, 'settings_local.json')).read())
            api_key = conf["sms"]["api_key"]
            api_secret = conf["sms"]["api_secret"]
            from_num = conf["sms"]["sender_number"]
            print(to_number)

            for single_num in to_number:
                params = {
                    'type': 'sms',
                    'to': single_num,
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
            # sys.exit()
            return redirect("index")

    else:
        form = forms.MessageForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)
