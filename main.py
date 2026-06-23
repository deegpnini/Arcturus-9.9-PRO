from flask import Flask, render_template, request, jsonify
import re
import json
from datetime import datetime

app = Flask(__name__)

class Arcturus999:
    def __init__(self):
        self.version = "9.9 D7D Edition"
        self.frequency = 439
        self.creator = "Comandante Hebron"
        
        self.red_flags = {
            'p_hacking': {
                'pattern': r'p\s*[=<>]\s*0\.0[45]\d*',
                'penalty': -2.5,
                'label': 'P-hacking suspeito',
                'description': 'Múltiplos valores p próximos de 0.05 indicam possível manipulação.'
            },
            'small_sample': {
                'pattern': r'n\s*[=<>]\s*\d{1,2}[,)]',
                'penalty': -2.0,
                'label': 'Amostra pequena',
                'description': 'n < 30: poder estatístico limitado.'
            },
            'conflict_interest': {
                'pattern': r'(financ|funded|support|sponsor).*(company|inc\.|ltd|corp)',
                'penalty': -2.0,
                'label': 'Conflito de interesse',
                'description': 'Financiamento comercial pode introduzir viés.'
            },
            'exaggeration': {
                'pattern': r'(revolution|breakthrough|miracle|cure|unprecedented)',
                'penalty': -1.5,
                'label': 'Linguagem exagerada',
                'description': 'Termos como "revolucionário" indicam viés de comunicação.'
            }
        }
        
        self.green_flags = {
            'preregistered': {
                'pattern': r'(preregistered|clinicaltrials\.gov)',
                'bonus': +1.5,
                'label': 'Pré-registro',
                'description': 'Estudo pré-registrado reduz risco de p-hacking.'
            },
            'open_data': {
                'pattern': r'(data.*available|github\.com|osf\.)',
                'bonus': +1.2,
                'label': 'Dados abertos',
                'description': 'Dados abertos permitem verificação independente.'
            },
            'rct': {
                'pattern': r'(randomized.*controlled|RCT|double.*blind)',
                'bonus': +1.5,
                'label': 'Estudo randomizado controlado',
                'description': 'RCT é padrão-ouro para inferência causal.'
            },
            'meta_analysis': {
                'pattern': r'(meta-analysis|systematic review)',
                'bonus': +2.5,
                'label': 'Meta-análise',
                'description': 'Meta-análise é topo da pirâmide de evidências.'
            }
        }

    def analyze(self, text):
        if not text or len(text.strip()) < 20:
            return {'error': 'Texto muito curto. Insira um abstract científico (mínimo 20 caracteres).'}
        
        text_lower = text.lower()
        red_detected = {}
        green_detected = {}
        
        for flag, config in self.red_flags.items():
            if re.findall(config['pattern'], text_lower):
                red_detected[flag] = {
                    'label': config['label'],
                    'penalty': config['penalty'],
                    'description': config['description']
                }
        
        for flag, config in self.green_flags.items():
            if re.findall(config['pattern'], text_lower):
                green_detected[flag] = {
                    'label': config['label'],
                    'bonus': config['bonus'],
                    'description': config['description']
                }
        
        base_score = 5.0
        total_score = base_score
        
        for flag, data in red_detected.items():
            total_score += data['penalty']
        for flag, data in green_detected.items():
            total_score += data['bonus']
        
        total_score = max(0.1, min(9.9, total_score))
        total_score = round(total_score, 1)
        
        veredictum = self.emitir_veredicto(total_score)
        
        return {
            'arcturus_score': total_score,
            'veredictum': veredictum,
            'red_flags': red_detected,
            'green_flags': green_detected,
            'metadata': {
                'version': self.version,
                'frequency': f"{self.frequency} Hz",
                'creator': self.creator
            }
        }
    
    def emitir_veredicto(self, score):
        if score >= 9.0:
            return {'categoria': 'EXCELÊNCIA CIENTÍFICA ⭐', 'cor': '#00ff88', 'descricao': 'Metodologia robusta e transparente.'}
        elif score >= 7.5:
            return {'categoria': 'ALTA QUALIDADE ✅', 'cor': '#00aaff', 'descricao': 'Metodologia sólida com pequenas melhorias possíveis.'}
        elif score >= 6.0:
            return {'categoria': 'QUALIDADE MODERADA ⚠️', 'cor': '#ffaa00', 'descricao': 'Algumas fragilidades metodológicas.'}
        elif score >= 4.0:
            return {'categoria': 'PROBLEMAS SIGNIFICATIVOS 🚨', 'cor': '#ff5500', 'descricao': 'Múltiplas bandeiras vermelhas.'}
        else:
            return {'categoria': 'DEFICIÊNCIAS GRAVES 🔴', 'cor': '#ff4444', 'descricao': 'Sérios problemas metodológicos.'}

arcturus = Arcturus999()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Envie {"text": "seu abstract aqui"}'}), 400
    result = arcturus.analyze(data['text'].strip())
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result)

@app.route('/api/examples')
def get_examples():
    return jsonify({
        'good': 'Randomized controlled trial with 847 patients. Pre-registered study. Double-blind design. Results: p<0.001. Funded by NIH. Data publicly available.',
        'medium': 'Observational study with 5,432 participants. Association found (p=0.006). Government funded. Data available upon request.',
        'bad': 'Revolutionary breakthrough tested on 18 volunteers. Cure rate 95% (p=0.048). Funded by SupplementCorp. Lead researcher is company CEO.'
    })

@app.route('/api/status')
def status():
    return jsonify({
        'system': 'ARCTURUS 9.9 PRO',
        'status': 'OPERATIONAL',
        'version': arcturus.version,
        'frequency': f"{arcturus.frequency} Hz",
        'creator': arcturus.creator
    })

if __name__ == '__main__':
    print("🧠 ARCTURUS 9.9 PRO")
    print(f"Criador: {arcturus.creator}")
    app.run(host='0.0.0.0', port=5000, debug=True)
