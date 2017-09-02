from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import LPForm
from .models import GeographicLP, ElectricityPrice, UsersLP
from django.db.models import Q
import numpy as np
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import components
import pandas as pd
import numpy as np

@login_required
def LPFormView(request) :
    
    if request.method == 'POST' :
        form = LPForm(request.POST)
        
        if form.is_valid() :
            region = form.cleaned_data['location']
            power = form.cleaned_data['power']
            bill = form.cleaned_data['bill']
            form.save()           

            consumption = (bill - ElectricityPrice.objects.get(em_power = power).sub_price)/ElectricityPrice.objects.get(em_power = power).kWh_price
            n = 365
            
            lp = GeographicLP.objects.get(region = region).data
            lp = consumption/n * lp
            
            mu = 0
            dtd = 0.1
            ts = 0.1
            dP_dtd = np.random.normal(mu, dtd, size=365)
            dP_ts = np.random.normal(mu, ts, size=8760)
            
            for j in range(365) :
                for k in range(24*j, 24*j+24, 1) :
                    lp[k] = (1+dP_dtd[j])*lp[k]
                    lp[k] = (1+dP_ts[k])*lp[k]
                    if lp[k] > power * 0.8 :
                        lp[k] = power * 0.8
                        
            userLP = UsersLP.objects.filter(Q(location=region) & Q(power=power) & Q(bill=bill))[0]
            userLP.user = request.user.email
            userLP.load_profile = lp
            userLP.consumption = consumption
            userLP.save()
            return redirect('results_lp')
    else :
        try :
            userLP = UsersLP.objects.get(user = request.user.email)
            form = LPForm(instance=userLP)
            userLP.delete()
        except :
            form = LPForm()
    return render(request, 'courbe_de_charge/form.html', {'form' : form})


@login_required
def Results(request) :
    
    user = request.user.username
    userLP = UsersLP.objects.get(user=request.user.email)
    data = userLP.load_profile
    consumption = str(userLP.consumption)[:4]

    plot = figure()
    plot.line([i for i in range(len(data))], data)
    plot.xaxis.axis_label = 'Heures'
    plot.yaxis.axis_label = 'Puissance (kWh)'
    script, div = components(plot, CDN)

    return render(request, 'courbe_de_charge/results.html', {'script': script, 'div': div, 'user': user, 'conso' : consumption})
