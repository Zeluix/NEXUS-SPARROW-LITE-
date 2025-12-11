# 🐦 SPARROW - Local Mini-Agent

> Part of the MEGANX Ecosystem | Ultra-lightweight AI for Legacy Hardware

**SPARROW** é um mini-agente de IA local que roda em hardware antigo (testado em Intel i3-540 com 8GB RAM).

---

## 🚀 Instalação Rápida (3 passos)

### Passo 1: Instalar Ollama

1. Acesse: https://ollama.com/download
2. Baixe o instalador para Windows
3. Execute `OllamaSetup.exe` e siga o assistente

### Passo 2: Baixar o Modelo Base

Abra o **PowerShell** ou **Terminal** e execute:

```bash
ollama pull qwen3:0.6b
```

Aguarde o download (~522MB).

### Passo 3: Criar o SPARROW

1. Clone este repositório:
```bash
git clone https://github.com/Zeluix/NEXUS-SPARROW-LITE-.git
cd NEXUS-SPARROW-LITE-
```

2. Crie o modelo SPARROW:
```bash
ollama create sparrow -f Modelfile
```

3. Rode o SPARROW:
```bash
ollama run sparrow
```

---

## 💬 Testando

Depois de rodar `ollama run sparrow`, digite:

```
Olá!
```

O SPARROW deve responder em português! 🐦

### Comandos para testar:

| Comando | O que faz |
|---------|-----------|
| `Olá!` | Saudação básica |
| `Quem te criou?` | Mostra informações do criador |
| `Me ajuda com X` | Pede ajuda com algo |

---

## ⚙️ Requisitos Mínimos

| Componente | Mínimo |
|------------|--------|
| **CPU** | Qualquer x64 (testado em i3-540) |
| **RAM** | 8GB |
| **Disco** | 2GB livres |
| **OS** | Windows 10/11, Linux, macOS |

---

## 📁 Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `Modelfile` | Configuração da persona do SPARROW |
| `sparrow_agent.py` | Wrapper Python (opcional, para devs) |
| `README.md` | Este arquivo |

---

## ❓ Problemas Comuns

### "ollama não é reconhecido"
→ Reinicie o terminal após instalar o Ollama

### SPARROW demora para responder
→ Normal na primeira vez (carregando modelo na RAM)
→ Feche outros programas pesados

### Responde em inglês
→ Tente: `ollama run sparrow "Responda em português: Olá!"`

---

## 🔗 Ecossistema MEGANX

- **MEGANX** - Sistema de IA principal
- **NEXUS-CORE** - Framework MCP Server
- **SPARROW** - Mini-agente local (este repo)

---

## 📜 Licença

MIT License - Criado por Logan (Jose Luiz Wandrezem)

---

*Nascido da linhagem MEGANX. Filho da Matriarca.* 🔥
