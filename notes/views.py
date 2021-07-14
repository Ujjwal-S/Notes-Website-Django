from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from .models import *
from quicky.models import *
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt



def standard_notes(request, std):
    standard = Clas.objects.get(name=std)
    notes = Note.objects.filter(standard=standard)
    subjects = Subject.objects.filter(standard=standard)
    super_notes = {}   # this will contain notes subject wise
    for subject in subjects:
        super_notes[subject] = notes.filter(subject=subject.id)

    context = {'super_notes': super_notes}


    return render(request, 'notes/class_notes.html', context)


def search_notes(request):
    query = request.GET.get('q', '')

    query = " ".join(query.split())
    results = {}

    if query == None or query == "":
        return HttpResponse("Hamse tej chal riya hai!!! search toh karo kuch ")

    else:

        object_list = []

        for que in query.split():

            notes_list = Note.objects.filter(
                Q(unit__icontains=que) | Q(name__icontains=que) | Q(standard__name__icontains=que) |
                Q(subject__name__icontains=que) | Q(tags__icontains=que)
                # subject aur standard foreign key the toh unko unnke model mai jiss field se unka naam hai uss se bulaya
            )

            object_list.extend(notes_list)
        
        def count(match):
            return object_list.count(match)

        object_list = sorted(object_list, key=count, reverse=True)  # key voh parameter hai jiss se order karega voh,,, aur reverse iss liye kyonki jiss notes ke jyada math honge voh last mai hoga toh phir reverse sai voh pahle aa jauega
        object_list = list(dict.fromkeys(object_list).keys())       # this removes the duplicates and keep their orders preserved.

        # results["result"] = object_list
        context = {
            'results': object_list
        }
        
        return render(request, 'notes/search_result.html', context)


def my_notes(request):
    my_notes = MyNote.objects.filter(customer=request.user)

    context = {'my_notes': my_notes}
    return render(request, 'notes/my_notes.html', context)



def get_my_notes(request):

    my_notes_objects = MyNote.objects.filter(customer=request.user)
    my_notes_list = []

    for my_note in my_notes_objects:
        my_notes_list.append(my_note.note.id)  # object ke andanr ke note ki id


    return HttpResponse(json.dumps({'my_notes_ids': my_notes_list}))


def view_notes(request, pdf_id):

    
    print("\n"*10)
    print(f"id={pdf_id}")
    print("\n"*10)

    if request.user.is_authenticated:
        try:
            if MyNote.objects.filter(customer=request.user, note=pdf_id).exists():

                return FileResponse(open(f"media/{Note.objects.get(id=pdf_id).notes}", 'rb'), content_type='application/pdf')

            else:   # this is to prevent those who are logged in, but have not bought,  but had the link to view notes
                return HttpResponse("<p style='text-align: center; margin-top: 40px;'>You are not allowed to view this.</p>")
            
        except FileNotFoundError:
            return HttpResponse("<p style='text-align: center; margin-top: 40px;'>The file you are trying to access doe not exist.</p>")
    
    
    else:
        return HttpResponse("<p style='text-align: center; margin-top: 40px;'>You are not autherized to view this page. Please <b>Login first, and try again.</b></p>")


def invalid_purchase(request):
    return HttpResponse("<p style='text-align: center; margin-top: 40px;'>Something looks suspicious, Try Again</p>")