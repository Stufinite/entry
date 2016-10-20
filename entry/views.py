from django.shortcuts import render

from django.views.decorators.cache import never_cache

from userper import Userper
u = Userper('login.stufinite.faith')


@never_cache
def entry(request):
    stufinite = {}
    username = u.get_username(request.session.session_key if request.session.session_key != None else '')
    if username != 'None':
        stufinite['is_authenticated'] = True
        stufinite['username'] = username
    else:
        stufinite['is_authenticated'] = False

    return render(request, 'entry/entry.html', {'stufinite': stufinite})
