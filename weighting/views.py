import string
from django.shortcuts import render, redirect
from django.contrib import messages
from weighting.algorithm.ahp import AhpWeight
from .models import Responden, WeightRFM, WeightLRFM

# Create your views here.

def index(request):
    context = {
        'title' : 'Weighting'
    }

    if request.POST:
        request.session['name'] = request.POST.get('name')
        request.session['education'] = request.POST.get('education')
        request.session['birth_date'] = request.POST.get('birth_date')
        request.session['gender'] = request.POST.get('gender')
        request.session['name_company'] = request.POST.get('name_company')
        request.session['business_field'] = request.POST.get('business_field')
        request.session['position'] = request.POST.get('position')
        request.session['experience'] = request.POST.get('experience')

    if request.session.has_key("name"):
        context['name'] =  request.session['name']
        context['education'] =  request.session['education']
        context['birth_date'] =  request.session['birth_date']
        context['name_company'] =  request.session['name_company']
        context['business_field'] =  request.session['business_field']
        context['position'] =  request.session['position']
        context['experience'] =  request.session['experience']

        return redirect('weighting:rfm')

    return render (request, 'weighting/index.html', context)

def rfm(request):
    context = {
        'title' : 'RFM'
    }

    if request.POST.get('score3'):
        data_input = {}
        data_input[request.POST.get('input1')] = int(request.POST.get('score1'))
        data_input[request.POST.get('input2')] = int(request.POST.get('score2'))
        data_input[request.POST.get('input3')] = int(request.POST.get('score3'))
        criteria = ['r','f','m']
        ahp = AhpWeight(data_input, criteria)
        if(ahp.consistency_ratio < 0.1):
            weight = ahp.final_weight
            request.session['rfm_r'] = weight['r']
            request.session['rfm_f'] = weight['f']
            request.session['rfm_m'] = weight['m']
            request.session['rfm_score'] = str(ahp.comparison_matrix)
            messages.info(request, 'success')
            return redirect('weighting:lrfm')
        else:
            messages.info(request, 'Please re-submit, because consintency ration more than 0.1')
            return redirect('weighting:rfm')
            
    if request.session.has_key("name"):
        context['responden'] = True

    return render (request, 'weighting/rfm.html', context)

def lrfm(request):
    context = {
        'title' : 'LRFM'
    }

    if request.POST.get('score6'):
        data_input = {}
        data_input[request.POST.get('input1')] = int(request.POST.get('score1'))
        data_input[request.POST.get('input2')] = int(request.POST.get('score2'))
        data_input[request.POST.get('input3')] = int(request.POST.get('score3'))
        data_input[request.POST.get('input4')] = int(request.POST.get('score4'))
        data_input[request.POST.get('input5')] = int(request.POST.get('score5'))
        data_input[request.POST.get('input6')] = int(request.POST.get('score6'))
        criteria = ['l','r','f','m']

        ahp = AhpWeight(data_input, criteria)
        if(ahp.consistency_ratio < 0.1):
            weight = ahp.final_weight
            request.session['lrfm_l'] = weight['l']
            request.session['lrfm_r']= weight['r']
            request.session['lrfm_f']= weight['f']
            request.session['lrfm_m']= weight['m']
            request.session['lrfm_score']= str(ahp.comparison_matrix)

            responden = Responden(
                None,
                request.session['name'],
                request.session['education'], 
                request.session['birth_date'],
                request.session['gender'], 
                request.session['name_company'], 
                request.session['business_field'],
                request.session['position'],
                request.session['experience']
            )
            responden.save()

            current_user = Responden.objects.filter(name = request.session['name']).values()
            rfm = WeightRFM(
                None,
                current_user[0]['id_responden'],
                request.session['rfm_r'], 
                request.session['rfm_f'], 
                request.session['rfm_m'], 
                request.session['rfm_score'], 

            )
            rfm.save()

            lrfm = WeightLRFM(
                None,
                current_user[0]['id_responden'],
                request.session['lrfm_l'], 
                request.session['lrfm_r'], 
                request.session['lrfm_f'], 
                request.session['lrfm_m'], 
                request.session['lrfm_score'], 

            )
            lrfm.save()

            messages.info(request, 'success')
            context['lrfm_l'] = request.session['lrfm_l']

            for key in list(request.session.keys()):
                del request.session[key]
        else:
            messages.info(request, 'Please re-submit, because consintency ration more than 0.1')
            return redirect('weighting:lrfm')

    if request.session.has_key("rfm_r"):
        context['rfm'] = True

    return render (request, 'weighting/lrfm.html', context)