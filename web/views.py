from django.shortcuts import render
import subprocess
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def submit(request):
    info = request.POST['info']
    n = len(info)
    k = len(set(info))
    ans = float('inf')
    i, j = 0, 0
    while True:
        if len(set(info[j:i+1])) == k:
         ans = min(ans, i + 1 - j)
         j+=1
        else:
         i+=1
        if i > len(info):
            break
    return HttpResponse(ans)
    # do something with info