from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Character, Inventory, Inventory_Item, Perk, Weapon, Armor

@login_required()
def index(request):
    # Fetch Data From Model
    #tasks = Task.objects.filter(user=request.user)

    # Fetch Form from Forms
    # form = TaskForm()

    # Insert Model Data into Template, Run Template Code, and Return to Client
    # return render(request, 'index.html', {'tasks': tasks, 'form': form})
    return render(request, 'index.html')


#@login_required
#@require_POST  # Ensure that only POST requests can access this view
#def create_task(request):
#    form = TaskForm(request.POST)
#    if form.is_valid():
#        task = form.save(commit=False)
#        task.user = request.user
#        task.save()
#        return JsonResponse({'status': 'ok', 'task_description': task.description, 'task_id': task.id})
#    else:
#        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)