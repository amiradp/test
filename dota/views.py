from django.shortcuts import render, redirect
from .models import DateCalculator

def index(request):
    if request.method == 'POST':
        total_hours = int(request.POST['total_hours'])
        days = total_hours // 24
        years = days // 365
        months = (days % 365) // 30
        remaining_days = (days % 365) % 30
        date_calculator = DateCalculator(
            total_hours=total_hours,
            years=years,
            months=months,
            days=remaining_days
        )
        date_calculator.save()
        return redirect('result', pk=date_calculator.pk)
    return render(request, 'dota/index.html')

def result(request, pk):
    date_calculator = DateCalculator.objects.get(pk=pk)
    return render(request, 'dota/result.html', {'date_calculator': date_calculator})


def find_dota_playtime(request):
    return render(request, 'dota/how-to-find-dota2-playtime.html')
   
   
def uninstall_dota(request):
    return render(request, 'dota/how-to-uninstall-dota-2.html')
