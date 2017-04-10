import re

from django import forms


class MessageForm(forms.Form):
    to_number = forms.CharField(label="수신번호 : '-', 공백 없이 넣어주세요", widget=forms.TextInput(attrs={'size': '100'}))
    text = forms.CharField(max_length=500,
                           widget=forms.Textarea,
                           label="문자내용",
                           )

    def clean_recipient_numbers(self):
        cleaned_numbers = []
        p = re.compile(r'^0\d{9}\d?$')

        number_string = self.cleaned_data['to_number']
        numbers = number_string.replace('-', '').replace(' ', '').split(',')
        for number in numbers:
            if re.match(p, number):
                cleaned_numbers.append(number)
                print(cleaned_numbers)
            else:
                pass
                # raise ValidationError('Invalid phone number format! {}'.format(number))
        return cleaned_numbers
