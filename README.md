# Alerta de Ingressos

Este projeto monitora a página de ingressos e avisa, com barulho, quando eles estiverem disponíveis.

## Requisitos
- Python 3
- Google Chrome

## Instalação
1. Clone este repositório.
2. Instale o Python 3.
3. Crie o ambiente virtual com este comando:
   ```
   python3 -m venv .venv
   ```
4. Ative a venv e instale as dependências com estes comandos:
   ```
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
5. Certifique-se de que o arquivo `beep_sound.mp3` está na pasta do projeto.

## Como usar
1. Execute o script automatizado com o seguinte comando:
   ```
   ./run.sh
   ```
2. Digite seu email e senha quando solicitado.
3. O programa irá monitorar a página e avisar quando o ingresso estiver disponível.

## Observações
- Não compartilhe seus dados pessoais.
- O uso deste script é por sua conta e risco.
