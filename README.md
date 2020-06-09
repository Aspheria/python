# python


1) Temos o logo (em anexo) no centro / cima da página;
2) Teremos um formulário com Nome, E-mail e Telefone.
3) No nome teremos a limitação de 35 chars;
4) No campo e-mail precisamos ter a validação de e-mail;
5) Telelefone ele precisa se formar conforme vai sendo escrito: (11) 98496-0773 (opção com nove número) ou (11) 2626-0382 (opção com 8 números);
6) Precisamos ter um botão de enviar;
7) Usaremos a API do Cloudinary onde esses campos Nome, Telefone e Email digitados e enviados serão "impressos" nos campos delimitados na arte (em anexo - PRINT_PRIME_ARTE.png)
API: https://cloudinary.com/documentation/image_transformations#image_and_text_overlays
7) Após essa "impressão" digital o usuário pode salvar o arquivo com essa arte "PRINT_PRIME_ARTE.png" e os nomes impressos nos campos delimitados.
8) Se possível use a API com Python, mas não é obrigatório.
9) Você pode hospedar o site no https://www.heroku.com/ ou qualquer outro lugar de sua preferência.

//flask shell
//flask run

appdirs==1.4.4
astroid==2.3.3
autopep8==1.5.3
certifi==2020.4.5.1
click==7.1.2
colorama==0.4.3
distlib==0.3.0
filelock==3.0.12
Flask==1.1.2
gunicorn==20.0.4
isort==4.3.21
itsdangerous==1.1.0
Jinja2==2.11.2
lazy-object-proxy==1.4.3
MarkupSafe==1.1.1
mccabe==0.6.1
pipenv==2020.6.2
pycodestyle==2.6.0
pylint==2.4.4
six==1.14.0
toml==0.10.1
virtualenv==20.0.21
virtualenv-clone==0.5.4
Werkzeug==1.0.1
wrapt==1.11.2
