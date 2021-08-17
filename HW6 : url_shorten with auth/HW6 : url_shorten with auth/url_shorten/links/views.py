from django.shortcuts import render, redirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Link, Key

def main(request):
    user = request.user
    return render(request, 'main.html', {'user': user})

def reduce_link(request):
    #print(f'all links = {Link.get_all_links()}')
    #print(f'all keys = {Key.get_all_keys()}')

    if not request.user.is_authenticated:
        return redirect('auth:log_in')
    else:
        ctx = {}
        if request.POST:
            new_link = request.POST.get('new_link', '')
            validate = URLValidator()
            try:
                validate(new_link)
                if new_link in Link.get_all_links():
                    new_key = Link.objects.get(link=new_link).get_key()
                else:
                    link = Link(link=new_link)
                    link.save()
                    new_key = Key.create_key()
                    key = Key(key=new_key, link=link, redirect_count=0)
                    key.save()
            except ValidationError:
                new_key = None
            ctx['new_link'] = new_link
            ctx['new_key'] = new_key
        return render(request, 'index.html', ctx)

def link(request, key):
    if key in Key.get_all_keys():
        return redirect(Link.objects.get(key=key))
    else:
        return redirect('links:reduce_link')

def redirect_link(request, new_key):
    key = Key.objects.get(key=new_key)
    key.add_redirect()
    key.save()
    #print(key.redirect_count)
    return redirect(key.get_link())
