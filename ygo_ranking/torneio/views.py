from django.shortcuts import render,get_object_or_404
from .forms import FormTorneio
from django.http import HttpResponse, FileResponse 
from .models import Torneio 
from fpdf import FPDF
from io import BytesIO
# Create your views here.
def novo_torneio(request):
    if request.method == "GET":
        meu_form = FormTorneio()
        return render(request, 'novo_torneio.html', {'form':meu_form})
    elif request.method == "POST":
        if request.user.is_staff:
            meu_form = FormTorneio(request.POST)
            if meu_form.is_valid():
                meu_form.save()
                return HttpResponse("Torneio criado com sucesso")
            else:
                return render(request, 'novo_torneio.html', {'form':meu_form})
def listar_torneio(request):
    if request.method == "GET":
        torneios = Torneio.objects.all()
        return render(request, 'listar_torneio.html', {"torneios" : torneios})
def acessar_torneio(request,identificador):
    torneio = get_object_or_404(Torneio, identificador=identificador)
    return render(request, 'acessar_torneio.html', {"torneio" : torneio})

def gerar_os(request,identificador):
    torneio = get_object_or_404(Torneio, identificador=identificador)
    pdf =  FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(200, 10, txt=f'- {torneio.name} -',ln=1, align='C', fill=True)
    pdf.cell(200, 10, txt=f'~{torneio.loja}~',ln=1, align='C', fill=True)
    
    pdf.cell(200, 10, txt=f'- Data para inscrição -> {torneio.data_inicio} - {torneio.data_fim}',ln=1, align='C', fill=True)
    pdf.cell(200, 10, txt=f'Duelistas Inscritos ({torneio.duelists.count()})', ln=1, align='C', fill=True)
    pdf.cell(200, 10, txt='-', ln=1, align='C')
    for duelist in torneio.duelists.all():
        pdf.cell(200, 10, txt=f'- {duelist.nickname} - {duelist.cossyId}', ln=1, align='C', fill=True)
    pdf.cell(200, 10, txt='-', ln=1, align='C')
    pdf_content = pdf.output(dest='S').encode('latin-1')
    pdf_bytes = BytesIO(pdf_content)
    #pdf.output(identificador+".pdf")
    #para fazer download direto usar parametro as_attachment=True
    return FileResponse(pdf_bytes, as_attachment=True,filename=f'{identificador}.pdf')