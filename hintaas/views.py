'''
Created on Mar 31, 2014

@author: lauril
'''
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from testset.models import TestTemplate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from hintaas.models import  ServiceProvider, ServiceConsumer, Service

xml="""<CATALOG>
    <PLANT>
        <COMMON>Bloodroot</COMMON>
        <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$2.44</PRICE>
        <AVAILABILITY>031599</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Columbine</COMMON>
        <BOTANICAL>Aquilegia canadensis</BOTANICAL>
        <ZONE>3</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$9.37</PRICE>
        <AVAILABILITY>030699</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Marsh Marigold</COMMON>
        <BOTANICAL>Caltha palustris</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Sunny</LIGHT>
        <PRICE>$6.81</PRICE>
        <AVAILABILITY>051799</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Cowslip</COMMON>
        <BOTANICAL>Caltha palustris</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$9.90</PRICE>
        <AVAILABILITY>030699</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Dutchman's-Breeches</COMMON>
        <BOTANICAL>Dicentra cucullaria</BOTANICAL>
        <ZONE>3</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$6.44</PRICE>
        <AVAILABILITY>012099</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Ginger, Wild</COMMON>
        <BOTANICAL>Asarum canadense</BOTANICAL>
        <ZONE>3</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$9.03</PRICE>
        <AVAILABILITY>041899</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Hepatica</COMMON>
        <BOTANICAL>Hepatica americana</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$4.45</PRICE>
        <AVAILABILITY>012699</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Liverleaf</COMMON>
        <BOTANICAL>Hepatica americana</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$3.99</PRICE>
        <AVAILABILITY>010299</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Jack-In-The-Pulpit</COMMON>
        <BOTANICAL>Arisaema triphyllum</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$3.23</PRICE>
        <AVAILABILITY>020199</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Mayapple</COMMON>
        <BOTANICAL>Podophyllum peltatum</BOTANICAL>
        <ZONE>3</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$2.98</PRICE>
        <AVAILABILITY>060599</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Phlox, Woodland</COMMON>
        <BOTANICAL>Phlox divaricata</BOTANICAL>
        <ZONE>3</ZONE>
        <LIGHT>Sun or Shade</LIGHT>
        <PRICE>$2.80</PRICE>
        <AVAILABILITY>012299</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Phlox, Blue</COMMON>
        <BOTANICAL>Phlox divaricata</BOTANICAL>
        <ZONE>3</ZONE>
        <LIGHT>Sun or Shade</LIGHT>
        <PRICE>$5.59</PRICE>
        <AVAILABILITY>021699</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Spring-Beauty</COMMON>
        <BOTANICAL>Claytonia Virginica</BOTANICAL>
        <ZONE>7</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$6.59</PRICE>
        <AVAILABILITY>020199</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Trillium</COMMON>
        <BOTANICAL>Trillium grandiflorum</BOTANICAL>
        <ZONE>5</ZONE>
        <LIGHT>Sun or Shade</LIGHT>
        <PRICE>$3.90</PRICE>
        <AVAILABILITY>042999</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Wake Robin</COMMON>
        <BOTANICAL>Trillium grandiflorum</BOTANICAL>
        <ZONE>5</ZONE>
        <LIGHT>Sun or Shade</LIGHT>
        <PRICE>$3.20</PRICE>
        <AVAILABILITY>022199</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Violet, Dog-Tooth</COMMON>
        <BOTANICAL>Erythronium americanum</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$9.04</PRICE>
        <AVAILABILITY>020199</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Trout Lily</COMMON>
        <BOTANICAL>Erythronium americanum</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$6.94</PRICE>
        <AVAILABILITY>032499</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Adder's-Tongue</COMMON>
        <BOTANICAL>Erythronium americanum</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$9.58</PRICE>
        <AVAILABILITY>041399</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Anemone</COMMON>
        <BOTANICAL>Anemone blanda</BOTANICAL>
        <ZONE>6</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$8.86</PRICE>
        <AVAILABILITY>122698</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Grecian Windflower</COMMON>
        <BOTANICAL>Anemone blanda</BOTANICAL>
        <ZONE>6</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$9.16</PRICE>
        <AVAILABILITY>071099</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Bee Balm</COMMON>
        <BOTANICAL>Monarda didyma</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$4.59</PRICE>
        <AVAILABILITY>050399</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Bergamot</COMMON>
        <BOTANICAL>Monarda didyma</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$7.16</PRICE>
        <AVAILABILITY>042799</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Black-Eyed Susan</COMMON>
        <BOTANICAL>Rudbeckia hirta</BOTANICAL>
        <ZONE>Annual</ZONE>
        <LIGHT>Sunny</LIGHT>
        <PRICE>$9.80</PRICE>
        <AVAILABILITY>061899</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Buttercup</COMMON>
        <BOTANICAL>Ranunculus</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$2.57</PRICE>
        <AVAILABILITY>061099</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Crowfoot</COMMON>
        <BOTANICAL>Ranunculus</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$9.34</PRICE>
        <AVAILABILITY>040399</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Butterfly Weed</COMMON>
        <BOTANICAL>Asclepias tuberosa</BOTANICAL>
        <ZONE>Annual</ZONE>
        <LIGHT>Sunny</LIGHT>
        <PRICE>$2.78</PRICE>
        <AVAILABILITY>063099</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Cinquefoil</COMMON>
        <BOTANICAL>Potentilla</BOTANICAL>
        <ZONE>Annual</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$7.06</PRICE>
        <AVAILABILITY>052599</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Primrose</COMMON>
        <BOTANICAL>Oenothera</BOTANICAL>
        <ZONE>3 - 5</ZONE>
        <LIGHT>Sunny</LIGHT>
        <PRICE>$6.56</PRICE>
        <AVAILABILITY>013099</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Gentian</COMMON>
        <BOTANICAL>Gentiana</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Sun or Shade</LIGHT>
        <PRICE>$7.81</PRICE>
        <AVAILABILITY>051899</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Blue Gentian</COMMON>
        <BOTANICAL>Gentiana</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Sun or Shade</LIGHT>
        <PRICE>$8.56</PRICE>
        <AVAILABILITY>050299</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Jacob's Ladder</COMMON>
        <BOTANICAL>Polemonium caeruleum</BOTANICAL>
        <ZONE>Annual</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$9.26</PRICE>
        <AVAILABILITY>022199</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Greek Valerian</COMMON>
        <BOTANICAL>Polemonium caeruleum</BOTANICAL>
        <ZONE>Annual</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$4.36</PRICE>
        <AVAILABILITY>071499</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>California Poppy</COMMON>
        <BOTANICAL>Eschscholzia californica</BOTANICAL>
        <ZONE>Annual</ZONE>
        <LIGHT>Sun</LIGHT>
        <PRICE>$7.89</PRICE>
        <AVAILABILITY>032799</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Shooting Star</COMMON>
        <BOTANICAL>Dodecatheon</BOTANICAL>
        <ZONE>Annual</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$8.60</PRICE>
        <AVAILABILITY>051399</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Snakeroot</COMMON>
        <BOTANICAL>Cimicifuga</BOTANICAL>
        <ZONE>Annual</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$5.63</PRICE>
        <AVAILABILITY>071199</AVAILABILITY>
    </PLANT>
    <PLANT>
        <COMMON>Cardinal Flower</COMMON>
        <BOTANICAL>Lobelia cardinalis</BOTANICAL>
        <ZONE>2</ZONE>
        <LIGHT>Shade</LIGHT>
        <PRICE>$3.02</PRICE>
        <AVAILABILITY>022299</AVAILABILITY>
    </PLANT>
</CATALOG>"""



def home(request):
    if not request.user.is_authenticated():
        return redirect('accounts/login/?next=%s' % request.path)
    else:
        return render_to_response('content.html',dict(test="heelloooo",user=request.user),
                              context_instance=RequestContext(request))

@login_required
def template(request, action):
    if action == 'list':
        tmpl = TestTemplate.objects.all()
        return render_to_response('template_list.html',dict(
                                                            template_list=tmpl,
                                                            data="oki!"),
                                   RequestContext(request))
    elif action == 'new':
        return render_to_response('show_xml.html',dict(content=xml),RequestContext(request))
    elif action == 'edit':
        return render_to_response('content.html',dict(test="EDIT template"),RequestContext(request))
    else:
        return render_to_response('content.html',dict(test="Not Implemented"),RequestContext(request))

@login_required  
def services(request, action):
    services = []
    service_type=action
    if action == request.user.username:
        try:
            services += ServiceProvider.objects.filter(user=request.user.get_profile().pk)
            print len(services)
        except Exception:
            pass
        try:
            services +=ServiceConsumer.objects.filter(user=request.user.get_profile().pk)
            print len(services)
        except Exception:
            pass
    elif action == 'all':
        services = getAllServices()
    return render_to_response('services.html',dict(service_type=service_type,service=services),
                              RequestContext(request))  
@login_required
def inter(request, action):
    from hintaas.models import Interoperability
    obj = Interoperability.objects.all()
    return render_to_response('interoperability_list.html',dict(
                                                            inter_list=obj,
                                                            data="oki!"),
                                   RequestContext(request))

@login_required
def serviceAdd(request):
    from forms import ServiceCreateForm, ServiceProviderForm, ServiceConsumerForm
    if(request.method == 'POST'):
        data = request.POST.copy()
        data['user']=request.user.get_profile().pk #service is assigned to profile!
        if request.POST.get('provider'):
            form = ServiceProviderForm(data)
        else:
            form = ServiceConsumerForm(data)
        if form.is_valid():
            sub = form.save(commit=False)       
            sub.save()
            if request.POST.has_key('submit_add'):
                return redirect('/service/add/')
            else:
                return HttpResponse('<script type="text/javascript">window.close()</script>')
        else:
            return render(request, 'hintaas/form.html', {'ServiceCreate':form, 'request' : request})

    else:
        sub = Service()
        subform = ServiceCreateForm(instance=sub)
        return render(request, 'hintaas/form.html', {'ServiceCreate':subform, 'request' : request})
    
def getAllServices():
    from models import ServiceProvider, ServiceConsumer
    services = []
    try:
        services +=  ServiceProvider.objects.all() 
        services +=  ServiceConsumer.objects.all() 
    except Exception:
        pass
    
    return services
        
          
def analytics(request):
    return render_to_response('analytics.html',dict(test="Analytics"),RequestContext(request))