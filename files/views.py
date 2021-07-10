from django.shortcuts import render
from .forms import AuthForm
from django.shortcuts import redirect
from .models import UserFile

def download(request,authCode):
    file = UserFile.objects.get(assetAuthCode=authCode)
    alias = file.alias
    url = file.userAsset.url
    return render(request, 'files/download.html', {'url': url, 'alias':alias})
def authorize(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            userFile = UserFile.objects.get(assetAuthCode=code)
            actualCode = userFile.assetAuthCode
            #1234567892356894
            return redirect('files:download', authCode=actualCode)
    else:
        form = AuthForm(request.POST)
    return render(request, 'files/form.html', {'form': form})
