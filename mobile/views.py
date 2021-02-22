from django.shortcuts import render, redirect
from .forms import CreateMobileForm, UpdateMobileForm
from .models import Mobile

# Create your views here.


def create_mobile(request):

    form = CreateMobileForm()
    mobile = Mobile.objects.all()
    context = {
        "form":form,
        "mobile": mobile,
    }

    if request.method == "POST":
        form = CreateMobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            form = CreateMobileForm()
            context = {
                "form": form,
            }

            return render(request, 'mobile/create.html', context)


    return render(request, 'mobile/create.html', context)



def view_mobile(request, id):

    mobile = Mobile.objects.get(id=id)
    context = {
        "mobile": mobile,
    }

    return render(request, 'mobile/view.html', context)






def edit_mobile(request, id):

    mobile = Mobile.objects.get(id=id)
    form = UpdateMobileForm(instance=mobile)

    context = {
        "form": form
    }

    if request.method == "POST":

        form = UpdateMobileForm(request.POST, instance=mobile)

        if form.is_valid():
            form.save()
            return redirect('create')
        else:
            form = UpdateMobileForm(instance=mobile)
            context = {
                "form":form,
            }
            return render(request, 'mobile/edit.html', context)

    return render(request, 'mobile/edit.html', context)



def delete_mobile(request, id):

    Mobile.objects.get(id=id).delete()

    return redirect('create')