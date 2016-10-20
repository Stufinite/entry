from django.shortcuts import render

from userper import Userper
u = Userper('login.stufinite.faith')


def entry(request):
    stufinite = {}
    username = u.get_username()
    if username != 'None':
        stufinite['is_authenticated'] = True
        stufinite['username'] = username
    else:
        stufinite['is_authenticated'] = False

    return render(request, 'entry/entry.html', {'stufinite': stufinite})
