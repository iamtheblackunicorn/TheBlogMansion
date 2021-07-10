from django.shortcuts import render
from .forms import AuthForm
from django.shortcuts import redirect
from .models import UserFile

def download(request,authCode):
    file = UserFile.objects.get(assetAuthCode=authCode)
    alias = file.alias
    url = file.userAsset.url
    path = file.userAsset.url.split('/')
    file = path[-1]
    return render(request, 'files/download.html', {'url': url, 'alias':alias, 'file': file})
def authorize(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            userFile = UserFile.objects.get(assetAuthCode=code)
            actualCode = userFile.assetAuthCode
            return redirect('files:download', authCode=actualCode)
        else:
            print("Error!")
    else:
        form = AuthForm()
    return render(request, 'files/form.html', {'form': form})
