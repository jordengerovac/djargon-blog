# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Entry
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def all_entries(request):
    entries = Entry.objects.all().order_by('date')
    return render(request, 'entries/all_entries.html', {'entries':entries})

def entry_detail(request, url):
    # return HttpResponse(url)
    entry = Entry.objects.get(url=url)
    return render(request, 'entries/entry_detail.html', {'entry':entry})

@login_required(login_url="/accounts/login/")
def entry_create(request):
    if request.method == 'POST':
        form = forms.CreateEntry(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('entries:all')
    else:
        form = forms.CreateEntry()
    return render(request, 'entries/entry_create.html', {'form':form})
