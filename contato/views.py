from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm

def contato_view(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            try:
                form.sendEmail()
                messages.success(request, 'Mensagem enviada com sucesso!')
                return redirect('contato:sucesso')
            except Exception as e:
                messages.error(request, f'Erro ao enviar mensagem: {str(e)}')
    else:
        form = ContatoForm()
    
    return render(request, 'contato/contato.html', {'form': form})

def sucesso_view(request):
    return render(request, 'contato/sucesso.html')
