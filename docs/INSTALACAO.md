# Instalacao e validacao - v1.4.2

1. Faca backup do `.htaccess` existente no DocumentRoot do servidor de origem.
2. Mescle o bloco de regras deste pacote ao `.htaccess` existente, antes de regras genericas de roteamento. Nao sobrescreva regras de outros projetos.
3. Confirme que `mod_rewrite` e `AllowOverride` permitem a execucao das regras.
4. Teste as URLs de 2023, 2024, 2025 e 2026, inclusive arquivos HTML, imagens, CSS e JS.
5. Confirme que os arquivos existem e estao acessiveis no servidor de destino. Um HTTP 403 no destino nao pode ser corrigido pelo redirecionamento de origem.

## Comportamento

- `/ype/` redireciona para `/clientes/ype/` na origem e, em seguida, para a raiz do destino.
- `/clientes/ype/noticiasdasemana/2026/0801/index.html` redireciona para `/noticiasdasemana/2026/0801/index.html` no destino.
- `/clientes/ype/noticiasdasemana/2026/528/528.html` redireciona para `/noticiasdasemana/2026/528/528.html` no destino.
- A regra opcional `index.html` -> `<edicao>.html` permanece **desativada**: nao existe inventario que comprove esse padrao para todas as edicoes. Ela deve ser habilitada apenas com escopo validado.
- Mudancas de pasta no destino (por exemplo, `/528/528.html` publicado como `/529/528.html`) exigem mapeamento das divergencias reais; nao podem ser inferidas pela regra generica.

## Testes sugeridos

```bash
curl -I 'https://hhdigital.com.br/clientes/ype/noticiasdasemana/2026/0801/index.html'
curl -I 'https://hhdigital.com.br/clientes/ype/noticiasdasemana/2026/528/528.html'
curl -I 'https://hhdigital.com.br/ype/noticiasdasemana/2025/123/index.html'
```

Verifique o cabecalho `Location` e, separadamente, o codigo HTTP do destino. Os exemplos nao garantem que todos esses arquivos existam.

## Publicacao no GitHub

O arquivo `.htaccess` deste repositorio e a versao operacional de referencia. Em producao, mescle o bloco de regras ao `.htaccess` existente e preserve as regras de outros projetos.
