# 🧠 ARCTURUS 9.9 PRO — Scientific Integrity Validator

## ⚡ O que é?

ARCTURUS 9.9 PRO é um sistema de validação científica que democratiza a avaliação profissional de estudos. Cole qualquer abstract e receba:

- Score de credibilidade (0.1 a 9.9)
- Red Flags (problemas metodológicos)
- Green Flags (pontos fortes)
- Recomendações educativas
- NEXUS VEREDICTUM (veredito final)

## 🔬 Como funciona?

1. Usuário cola o texto do estudo
2. ARCTURUS escaneia com regex inteligente
3. Detecta Red Flags e Green Flags
4. Calcula score não-linear (0.1-9.9)
5. Emite NEXUS VEREDICTUM

## 🎯 Detecta automaticamente:

### 🚨 RED FLAGS
- P-hacking (múltiplos p≈0.05)
- Amostra pequena (n<30)
- Conflito de interesse
- Dados não compartilhados
- Falta de grupo controle
- Linguagem exagerada

### ✅ GREEN FLAGS
- Pré-registro (ClinicalTrials.gov, PROSPERO)
- Dados abertos (GitHub, OSF)
- RCT (Randomized Controlled Trial)
- Meta-análise/Revisão sistemática
- Financiamento público
- Reconhecimento de limitações

## 👤 Criador

**Comandante Hebron** — Desenvolvido em um Samsung A70 + Notebook Lubuntu via orquestração de IAs.

*"Tecnologia com alma, dados com propósito, código com coração."*

## 🛠️ Tecnologia

- **Backend:** Python + Flask
- **Frontend:** HTML/CSS/JS (Cyberpunk UI)
- **Lógica:** Regex avançado + sistema de scoring
- **Hospedagem:** Replit / Railway / Vercel

## 📦 Instalação

```bash
pip install -r requirements.txt
python main.py
