from django.shortcuts import render
from .models import AppVariety, AppStore
from django.shortcuts import get_object_or_404
from .forms import AppVarietyForm

# Create your views here.
def all_demo_app(request):
    apps = AppVariety.objects.all()
    return render(request, 'demo_app/all_demo_app.html', {'apps': apps})

def demo_app_detail(request, demo_app_id):
    app = get_object_or_404(AppVariety, pk=demo_app_id)
    return render(request, 'demo_app/demo_app_detail.html', {'app': app})

def demo_app_store_view(request):
    app_stores = None
    if request.method == 'POST':
        form = AppVarietyForm(request.POST)
        if form.is_valid():
            app_variety = form.cleaned_data['app_variety']
            app_stores = AppStore.objects.filter(app_varieties = app_variety)
    else:
        form = AppVarietyForm()
    return render(request, 'demo_app/demo_app_stores.html', {'app_stores': app_stores, 'form': form})