# 📄 Classe OMRScanner

A classe **OMRScanner** atua como **fachada principal** do sistema de leitura de folhas de respostas.

## 🧠 Responsabilidades
- Coordenar todas as etapas do processo de leitura da imagem da folha de respostas.
- Utilizar as outras classes (ImageLoader, ImagePreprocessor, etc.) para aplicar cada etapa do pipeline.
- Gerar o resultado final com nota e imagem corrigida.

## 🔧 Métodos
- `scan()`: executa todo o processo de leitura e avaliação.
- `get_result_image()`: retorna a imagem corrigida com marcações.
- `get_original_image()`: retorna a imagem original.

## 🧱 POO Aplicado
- Encapsulamento com propriedades (`@property`).
- Validações no `setter`.
- Herança indireta: usa objetos de classes com herança (ex: exceções).