# Site da Engenheira Gislaine Teles

Este é um site completo desenvolvido em Django para a engenheira Gislaine Teles, especializada em diagnóstico, vistorias de entrega de chaves, vistorias para síndico e laudos técnicos.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
gislaine_site/
├── venv/                      # Ambiente virtual Python
├── gislaine_engenharia/       # Configurações principais do projeto Django
│   ├── settings.py            # Configurações do Django, incluindo email
│   ├── urls.py                # URLs principais
│   └── ...
├── home/                      # Aplicativo da página inicial
│   ├── templates/home/        # Templates da página inicial
│   ├── views.py               # Views da página inicial
│   └── ...
├── contato/                   # Aplicativo de contato
│   ├── templates/contato/     # Templates da página de contato
│   ├── forms.py               # Formulário de contato
│   ├── views.py               # Views da página de contato
│   └── ...
├── static/                    # Arquivos estáticos
│   ├── css/                   # Folhas de estilo
│   ├── js/                    # Scripts JavaScript
│   ├── img/                   # Imagens
│   └── video/                 # Vídeos
├── media/                     # Arquivos de mídia enviados pelos usuários
│   ├── img/                   # Imagens enviadas
│   └── video/                 # Vídeos enviados
├── manage.py                  # Script de gerenciamento do Django
└── requirements.txt           # Dependências do projeto
```

## Funcionalidades

- **Página Inicial**: Apresentação da profissional, serviços, portfólio, depoimentos e botão de WhatsApp para contato rápido.
- **Página de Contato**: Formulário para envio de mensagens diretamente para o email da profissional.
- **Design Responsivo**: Layout adaptável para dispositivos móveis e desktop.
- **Envio de Email**: Configuração completa para envio de emails através do formulário de contato.

## Requisitos

- Python 3.8+
- Django 5.2.1
- Pillow 11.2.1

## Instalação

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/gislaine-teles-site.git
cd gislaine-teles-site
```

2. Crie e ative um ambiente virtual:
```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente para o email (ou edite diretamente no settings.py):
```
export EMAIL_HOST_USER=seu-email@gmail.com
export EMAIL_HOST_PASSWORD=sua-senha-de-app
```

5. Execute as migrações:
```
python manage.py migrate
```

6. Crie um superusuário (opcional):
```
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

8. Acesse o site em http://127.0.0.1:8000/

## Personalização

### Imagens e Vídeos
- Substitua as imagens em `static/img/` por fotos reais da engenheira e seus projetos
- Substitua o vídeo em `static/video/` pelo vídeo institucional real

### Informações de Contato
- Atualize o número de WhatsApp no template `home/templates/home/index.html`
- Atualize os emails e telefones nos templates e no arquivo `settings.py`

### Cores e Estilos
- As cores principais podem ser modificadas no arquivo `static/css/style.css`

## Implantação

Para implantar em produção:

1. Configure as configurações de produção no `settings.py`:
   - Defina `DEBUG = False`
   - Atualize `ALLOWED_HOSTS`
   - Configure um banco de dados adequado para produção

2. Colete os arquivos estáticos:
```
python manage.py collectstatic
```

3. Implante usando um servidor WSGI como Gunicorn e um servidor web como Nginx.

## Suporte

Para dúvidas ou suporte, entre em contato com o desenvolvedor.

## Licença

Este projeto é de uso exclusivo da engenheira Gislaine Teles.
