from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

# data

@login_required
def data(request):
    user_data = Member.objects.filter(user=request.user)
    return render(request, 'crud/data.html', {'user_data': user_data})

# create

@login_required
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        std = request.POST.get('std')
        phone_number = request.POST.get('phone_number')
        
        Member.objects.create(user=request.user, name=name, std=std, phone_number=phone_number)
        return redirect('data')
    else:
        return render(request, 'crud/form.html')

# update

@login_required
def update(request, member_id):
    member = get_object_or_404(Member, id=member_id, user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name')
        std = request.POST.get('std')
        phone_number = request.POST.get('phone_number')
        
        member.name = name
        member.std = std
        member.phone_number = phone_number
        member.save()
        return redirect('data')
    else:
        return render(request, 'crud/update.html', {'member': member})

# delete

@login_required
def delete(request, member_id):
    member = get_object_or_404(Member, id=member_id, user=request.user)
    if request.method == 'POST':
        member.delete()
        return redirect('data')
    else:
        return render(request, 'crud/data.html', {'member': member})

# search

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            user_data = Member.objects.filter(name__icontains=query) 
            return render(request, 'crud/search.html', {'user_data': user_data})
        else:
            print("No Result")
            return render(request, 'crud/search.html', {})


