# Keylogger Parser

> Captura teclas em background e extrai padrões sensíveis.

## Funcionalidades
- **Coleta e envio** de logs de teclado para servidor remoto  
- **Pós‑processamento** (`normalize_text`): decodifica `\n`, `\t`, `\xNN` e remove control codes  
- **Detecção por strategies**:  
  - E‑mails (fallback capturando até 10 caracteres antes do `@` e “senha” após `.com`)  
  - Flags e keywords de redes sociais  
  - Cartões de crédito (13–16 dígitos)  
  - Telefones (formatos nacionais/internacionais)
