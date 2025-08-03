# 🧾 Scanner de Folha de Respostas com OMR (Optical Mark Recognition)

Sistema acadêmico desenvolvido com **Python**, **Django** e **OpenCV** que permite o **upload e correção automática de folhas de múltipla escolha** via Web.

---

## 🎯 Objetivo do Projeto

Permitir que professores ou instituições escaneiem imagens de folhas de resposta e recebam:
- A nota final do aluno com base em um gabarito
- A visualização da folha com as respostas corretas marcadas

---

## 📸 Funcionalidades

- Upload de imagem de folha de respostas
- Processamento com OpenCV e OMR
- Correção automática com base em gabarito configurável
- Exibição da nota e da imagem corrigida na interface web
- Tratamento de erros durante o envio e processamento

---

## ⚙️ Tecnologias Utilizadas

- Python 3.12
- Django 4.x
- OpenCV
- NumPy
- imutils
- Pillow
- HTML5 e CSS3 (interface)

---

## 📦 Conceitos de POO Aplicados

| Conceito | Aplicação no Projeto |
|---------|-----------------------|
| **Encapsulamento** | Atributos e métodos privados (`_atributo`, `__metodo`) nas classes do pacote `omr` |
| **Herança**        | Exceções personalizadas herdando de `Exception` (como `OMRException`) |
| **Modularização**  | Código dividido em pacotes: `omr`, `omr_web`, cada um com responsabilidade própria |
| **Abstração**      | Classes como `ImageLoader`, `DocumentDetector`, `AnswerEvaluator` isolam funcionalidades |
| **Polimorfismo**   | Pode ser aplicado ao substituir estratégias de avaliação, transformação ou leitura futuramente |
| **Atributos públicos/protegidos/privados** | Como exigido no projeto, alguns atributos foram tornados públicos para visualização; outros permanecem protegidos para encapsulamento da lógica interna |

---

## 🧪 Estrutura de Diretórios

```
scanner_omr/
├── manage.py
├── scanner_django/        # Configurações do projeto Django
├── omr/                   # Pacote com as classes de processamento OMR
├── omr_web/               # App Django (views, forms, templates, static)
│   ├── templates/
│   │   └── omr_web/upload.html
│   ├── static/
│   │   └── omr_web/style.css
│   └── forms.py
├── README.md
```

---

## 🛠️ Como Executar Localmente

### 1. Clone o projeto
```bash
git clone https://github.com/Lucaslps10/scanner_omr.git
cd scanner_omr
```

### 2. Ative o ambiente virtual
```bash
ambiente\Scripts\activate  # Windows
```

### 3. Instale os requisitos
```bash
pip install -r requirements.txt
```

### 4. Execute o servidor
```bash
python manage.py runserver
```

### 5. Acesse no navegador
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## ✅ Exemplo de Gabarito Padrão

```python
{0: 1, 1: 4, 2: 0, 3: 3, 4: 1}
```

Você pode alterar o dicionário diretamente na instância da classe `OMRScanner`.

---

## 🧠 Considerações Finais

Este projeto foi estruturado com foco em:
- Clareza no uso de orientação a objetos
- Separação de responsabilidades
- Tratamento de exceções amigável
- Facilidade de uso via interface web

---

## 🪪 Licença

Uso acadêmico e educacional. Código aberto sob [MIT License](https://opensource.org/licenses/MIT).
