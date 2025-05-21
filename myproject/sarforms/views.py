from django.db.models import Max
from .models import Form133, Form133Next
from .forms import Form133Form, Form133NextForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Incident

# radio register view   
def radio_log(request):
    laatste = Form133.objects.last()
    volgend_incident_nr = (Form133.objects.aggregate(Max('incident_nr'))['incident_nr__max'] or 0) + 1

    if request.method == "POST":
        form = Form133Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs')  # redirect to the logs page after saving

    else:
        form = Form133Form(initial={'incident_nr': volgend_incident_nr})

    context = {
        'form': form,
        'laatste': laatste,
        'volgend_incident_nr': volgend_incident_nr,
    }
    return render(request, 'radio_register.html', context) #render the form

# radio log view
def radio_log_combined(request):
    if request.method == "POST":
        form = Form133NextForm(request.POST)
        if form.is_valid():
            form.save()

    max_incident_nr = Form133.objects.aggregate(Max('incident_nr'))['incident_nr__max']
    logs = Form133Next.objects.filter(incident_nr=max_incident_nr).order_by('-datum', '-tijd')

    incidenten = Form133.objects.all()
    laatste = Form133.objects.last()
    form = Form133NextForm(initial={'incident_nr': max_incident_nr})

    context = {
        'form': form,
        'form133next': logs,
        'form133': incidenten,
        'laatste': laatste,
    }

    return render(request, 'radio_log_combined.html', context)

# update view
def edit_form133next(request, pk):
    instance = get_object_or_404(Form133Next, pk=pk)
    
    if request.method == "POST":
        form = Form133NextForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('logs')  # Pas aan indien je een andere viewnaam gebruikt
    else:
        form = Form133NextForm(instance=instance)
    
    context = {'form': form, 'object': instance}
    return render(request, 'edit_form133next.html', context)


#delete view
def delete_form133next(request, pk):
    instance = get_object_or_404(Form133Next, pk=pk)
    if request.method == "POST":
        instance.delete()
    return redirect('logs')



def incidenten_lijst(request):
    incident_nr = request.GET.get('incident_nr')

    if incident_nr:
        data = Form133Next.objects.filter(incident_nr=incident_nr).order_by('-datum', '-tijd')
    else:
        data = Form133Next.objects.none()

    # Unieke incident_nrs voor de dropdown
    alle_incident_nrs = Form133Next.objects.values_list('incident_nr', flat=True).distinct().order_by('-incident_nr')

    return render(request, 'incidenten_lijst.html', {
        'incidenten': data,
        'huidig_incident_nr': incident_nr,
        'alle_incident_nrs': alle_incident_nrs,
    })