# happyhouse-ype-news-redirect
Regras Apache `mod_rewrite` para preservar os acessos historicos as newsletters da Ypê hospedadas temporariamente pela HappyHouse, redirecionando-os do **servidor de origem** para o **servidor de destino**.

**Versao:** 1.4.2

## Comportamento
- `/clientes/ype/noticiasdasemana/ANO/EDICAO/arquivo` e `/ype/noticiasdasemana/ANO/EDICAO/arquivo` sao redirecionados para `/noticiasdasemana/ANO/EDICAO/arquivo` no servidor de destino.
- Preserva o nome do arquivo e os caminhos de imagens, CSS e JavaScript, independentemente do ano.
- `/ype/` aponta primeiro para `/clientes/ype/`; a raiz `/clientes/ype/` aponta para a pagina inicial do destino.
- Nao ha mapeamento presumido de edicoes para pastas diferentes.
- A conversao opcional `index.html` para `EDICAO.html` esta **comentada** e nao deve ser ativada sem inventario validado.

## Estrutura
- `.htaccess`: regras a serem mescladas ao arquivo do DocumentRoot do servidor de origem.
- `tests/redirects.csv`: casos de teste de redirecionamento.
- `tests/test_redirects.py`: verificacoes estaticas das regras.
- `.github/workflows/validate.yml`: execucao automatica dos testes em push e pull request.
- `docs/INSTALACAO.md`: implantacao.
- `docs/VALIDACAO.md`: verificacoes antes e depois da publicacao.

## Testes locais
```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```
Os testes simulam a correspondencia das regras e **nao** substituem a validacao no Apache real. Erros HTTP 403 no destino exigem verificacao no servidor de destino.

## Publicacao no GitHub
Descompacte o ZIP, abra a pasta `ype-news-redirect-github-v1.4.2` e execute:

```bash
git add .
git commit -m "chore: atualiza redirecionamentos Ype para v1.4.2"
git push
```
Nao substitua integralmente o `.htaccess` existente em producao sem antes mesclar suas demais regras.
