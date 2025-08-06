# 📐 Classe DocumentDetector

Detecta o contorno principal da folha de respostas.

## 🧠 Responsabilidades
- Detectar os contornos da imagem.
- Selecionar o maior contorno com 4 vértices (a folha).

## 🔧 Métodos
- `find_contours()`: encontra todos os contornos.
- `detect_document()`: retorna o contorno principal (folha).