from django.forms import ModelForm
from .models import Torneio, CategoriaTorneio, Match  # Substitua com o modelo correspondente

class FormTorneio(ModelForm):
    class Meta:
        model = Torneio
        #fields = ['name', 'loja', 'categoria', 'duelists', 'data_inicio', 'data_fim', 'finalizado', 'protocolo', 'num_rodadas']
        #fields = '__all__'
        exclude = ['duelists', 'finalizado', 'protocolo', 'num_rodadas', 'winner']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['name'].widget.attrs.update({'class': 'form-control'})
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            self.fields[field].widget.attrs.update({'placeholder': field})
        choices = list()
        for i,j in self.fields['categoria'].choices:
            categoria = CategoriaTorneio.objects.filter(titulo=j)
            #print(categoria)
            if len(categoria) > 0:
                pass
                choices.append((i.value, categoria[0].get_titulo_display()))
        self.fields['categoria'].choices = choices
