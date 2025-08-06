# 🎨 Classe ImagePreprocessor

Aplica transformações iniciais na imagem (grayscale, blur, bordas).

## 🧠 Responsabilidades
- Converter a imagem original para tons de cinza.
- Aplicar desfoque (blur).
- Detectar bordas com Canny.

## 🔧 Métodos
- `process()`: executa todos os passos de pré-processamento.
- `get_gray()`, `get_edged()`: retornam os resultados.