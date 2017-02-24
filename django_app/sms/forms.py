from django import forms


class MessageForm(forms.Form):
    to_number = forms.IntegerField(label="수신번호 : '-', 공백 없이 넣어주세요")
    text = forms.CharField(max_length=500,
                           widget=forms.Textarea,
                           label="문자내용",
                           )
