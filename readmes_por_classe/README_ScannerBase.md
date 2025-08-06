
# 📄 Classe `ScannerBase`

A classe `ScannerBase` é uma classe abstrata que define a estrutura e o contrato básico para todos os scanners no sistema. Ela é usada para garantir que todas as subclasses implementem o método `scan()`.

---

## ✅ Responsabilidades

- Servir como **superclasse** para qualquer classe de scanner (ex: `OMRScanner`)
- Fornecer uma **interface padronizada** com o método abstrato `scan`
- Garantir consistência entre implementações diferentes de scanner

---

## 🧩 Métodos

### `scan(self)`
Método abstrato que deve ser implementado por qualquer subclasse. Representa a operação principal do scanner (ex: processamento de imagem, análise, etc).

---

## 🔐 Conceitos de POO Aplicados

| Conceito         | Aplicação                                                 |
|------------------|------------------------------------------------------------|
| **Herança**      | Serve como superclasse da `OMRScanner`                    |
| **Abstração**    | Força as subclasses a implementarem o método `scan()`     |
| **Polimorfismo** | Permite que outras classes possam implementar `scan()` de formas diferentes |

---

## 📦 Exemplo de Subclasse

```python
from omr.base import ScannerBase

class OMRScanner(ScannerBase):
    def scan(self):
        # lógica de leitura da folha e correção
        pass
```

---

## 🧠 Observações

Essa arquitetura permite que, no futuro, você implemente outros tipos de scanner (ex: de QR Code, de texto, de imagens médicas) sem precisar modificar o restante do sistema. Basta criar uma nova classe herdando de `ScannerBase`.
