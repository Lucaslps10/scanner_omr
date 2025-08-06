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

## 📚 Conceitos de POO Aplicados

| Conceito             | Aplicação Concreta                                                                 |
|----------------------|------------------------------------------------------------------------------------|
| **Encapsulamento**   | Uso de atributos protegidos (`_atributo`) e `@property` para acesso controlado     |
| **Herança**          | Classe `OMRScanner` herda de `ScannerBase` (classe abstrata)                       |
| **Abstração**        | `ScannerBase` define interface obrigatória para qualquer scanner                   |
| **Modularização**    | Cada classe tem um arquivo próprio no pacote `omr`, com responsabilidade isolada   |
| **Tratamento de exceções** | Uso da classe `OMRException` personalizada e `try/except` em cada etapa do processo |
| **Getters e setters**| Usados através de `@property` em `OMRScanner`, com validações de tipo              |
| **Polimorfismo**     | Possibilidade de criar outros scanners herdando de `ScannerBase`                   |


---

## 🧪 Estrutura de Diretórios

```
scanner_omr/
├── manage.py
├── ambiente/ # Ambiente virtual (não versionar)
├── scanner_django/ # Configurações principais do Django
│ └── settings.py
│ └── urls.py
├── omr/ # Pacote com as classes de processamento OMR
│ ├── scanner_base.py # Classe abstrata base
│ ├── omr_scanner.py # Fachada principal (herda de ScannerBase)
│ ├── image_loader.py
│ ├── image_preprocessor.py
│ ├── document_detector.py
│ ├── perspective_transformer.py
│ ├── thresholding.py
│ ├── bubble_detector.py
│ ├── answer_evaluator.py
│ ├── answer_key.py
│ └── exceptions.py
├── omr_web/ # Aplicativo Django com views, templates e models
│ ├── views.py
│ ├── forms.py
│ ├── models.py
│ ├── urls.py
│ ├── templates/
│ │ └── omr_web/
│ │ └── upload.html
│ ├── static/
│ │ └── omr_web/
│ │ └── style.css
├── media/ # Imagens enviadas e corrigidas (criado em tempo de execução)
├── README.md
├── requirements.txt
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
