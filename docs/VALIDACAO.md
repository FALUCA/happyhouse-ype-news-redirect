# Validacao

## Antes do deploy

1. Execute `python3 -m unittest discover -s tests -p 'test_*.py' -v`.
2. Faca backup do `.htaccess` atual e compare o diff.
3. Confirme `mod_rewrite` ativo, `AllowOverride` e precedencia das regras.
4. Confira que o servidor de destino possui os arquivos nos caminhos esperados.

## Depois do deploy

Confira o cabecalho `Location` sem seguir automaticamente o redirecionamento:

```bash
curl -I 'https://hhdigital.com.br/clientes/ype/noticiasdasemana/2026/0801/index.html'
curl -I 'https://hhdigital.com.br/clientes/ype/noticiasdasemana/2025/123/123.html'
curl -I 'https://hhdigital.com.br/ype/noticiasdasemana/2024/456/images/index_01.jpg'
```

Os dois ultimos exemplos verificam apenas a regra de roteamento, nao a existencia dos arquivos.

- O retorno esperado na origem e `301` com `Location` apontando para o mesmo caminho relativo no destino.
- Valide o status final no destino separadamente. `403` e `404` no destino nao sao corrigidos por uma regra de redirecionamento na origem.
- A pasta de destino diferente da origem requer um inventario explicito; a regra generica nao descobre arquivos remotos.
