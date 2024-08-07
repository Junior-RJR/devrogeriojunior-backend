from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_response(message):
    message = message.lower()
    
    if 'olá' in message or 'oi' in message:
        return 'Olá! Como posso ajudar você hoje?'
    
    elif 'ola' in message or 'oii' in message:
        return 'Olá! Como posso ajudar você hoje?'
    
    elif 'quem é você' in message or 'quem é voce' in message:
        return 'Eu sou um chatbot criado pelo Junior, que posso responder a perguntas sobre o currículo e outras coisas referente a ele =)'
    
    elif 'habilidades' in message or 'skills' in message:
        return 'Junior tem habilidades em HTML5, CSS3, JavaScript, TypeScript, React, Node.js, Python, PHP, e utiliza a Metodologia Ágil Scrum.'
    
    elif 'experiência' in message or 'experiencia' in message:
        return 'Junior tem experiência em desenvolvimento de aplicativos e sites, incluindo projetos como RJR-Docs, Infor-mais e Pastelaria Maza.'
    
    elif 'contato' in message:
        return 'Você pode entrar em contato comigo através do e-mail: devrogeriojunior@gmail.com ou pelo telefone: (11) 94625-2220.'
    
    elif 'redes sociais' in message:
        return 'Você pode me encontrar nas seguintes redes sociais: Linkedin ( www.linkedin.com/in/rogério-junior )'
    
    elif 'site' in message and 'tecnologia' in message:
        return 'O site foi desenvolvido utilizando React para o front-end e Python para o backend.'
    
    elif 'chatbot' in message and 'tecnologia' in message:
        return 'O chatbot foi desenvolvido com Python e integrado ao site usando uma API.'
    
    elif 'framework' in message:
        return 'Eu utilizei o framework React para a construção do site e Python para a criação das funcionalidades do chatbot.'
    
    elif 'funcionalidades' in message or 'o que o chatbot pode fazer' in message:
        return 'O chatbot pode responder a perguntas frequentes, fornecer informações de contato, detalhes sobre redes sociais e explicar as tecnologias usadas no site.'
    
    elif 'sobre mim' in message or 'quem é você' in message:
        return 'Eu sou o RJR-Bot, o assistente virtual do site. Estou aqui para ajudar com informações e responder às suas perguntas!'
    
    elif 'propósito' in message:
        return 'Meu propósito é fornecer informações rápidas e úteis sobre o site, o desenvolvedor e outros detalhes relevantes.'
    
    elif 'site' in message and 'novidades' in message:
        return 'Sim, fique atento às nossas redes sociais para as últimas novidades e atualizações!'
    
    elif 'ajuda' in message:
        return 'Se você precisar de mais ajuda, entre em contato conosco pelo e-mail devrogeriojunior@gmail.com.'
    
    elif 'mais informações' in message:
        return 'Você pode encontrar mais informações em nosso site ou entrando em contato através das nossas redes sociais e e-mail.'
    
    elif 'estrutura do site' in message:
        return 'O site é estruturado com um front-end em React, que oferece uma interface dinâmica, e um backend em Python que gerencia a lógica e os dados.'
    
    elif 'biblioteca' in message:
        return 'Sim, usei bibliotecas como Axios para requisições HTTP e Flask para criar o backend em Python.'
    
    else:
        return 'Desculpe, não entendi sua pergunta. Pode reformular?'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    message = data.get('message')
    response = generate_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
