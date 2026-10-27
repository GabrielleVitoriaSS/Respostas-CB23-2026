# Relatório — Gabrielle Vitoria dos Santos Silva (3230)

Relatório do projeto, preenchido na sua branch. Cada marco acrescenta a sua seção. Responda com as suas palavras e com
os números da sua execução; cada resposta cabe em até 6 linhas, além das tabelas.

## Marco 1

### Ambiente

O repositório foi clonado primeiro em máquina no IMPATECH, em que os códigos indicados funcionaram.

Verifiquei que os códigos para criação do ambiente virtual não funcionavam no ambiente Windows na máquina pessoal. 
Executando, também, no terminal do VSCode, inicialmente do diretório do projeto, foi necessário sair da pasta.

```powershell
cd .. # sai da pasta do projeto
python --version # utiliza python ao invés de python3 como comando
python -m venv prog2-venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\prog2-venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install numpy

Get-Command python # verifica venv
```

Na monitoria de 19/10, realizei commits durante a aula para acompanhar o monitor, mas retornei ao commit antes da monitoria para criar meu próprio código, criando uma branch de rascunho para anotações.

```powershell
git switch projeto_3230 
git log --oneline -n 10 # verifica ultimos commits
git branch monitoria 
git reset --hard 388d88a
git log --oneline -n 3
git push --force origin projeto_3230
git push -u origin monitoria
```

Saída do equivalente ao which python (Get-Command python):

```text
CommandType     Name                                               Version    Source            
-----------     ----                                               -------    ------            
Application     python.exe                                         3.13.51... C:\Users\Usuari...
```

Verificando, então, o Source:  
```text
(prog2-venv) PS C:\Users\Usuario\OneDrive\Desktop\Respostas-CB23-2026> (Get-Command python).Source
C:\Users\Usuario\OneDrive\Desktop\prog2-venv\Scripts\python.exe
```

Saída da Etapa 0:   

```text
=== Etapa 0: ambiente ===
Python 3.13.5 | NumPy 2.5.4 | fornecido 3.0
```


### R1 — Expressões regulares

<!-- Uma string que re.match aceita e re.fullmatch rejeita com o padrão de tag; consequência para valida_tag. -->

### R2 — Linhas inválidas

<!-- Por que ler_log devolve as linhas descartadas; uma situação real em que descartar em silêncio esconderia um problema. -->

### R3 — Late binding

<!-- Por que errados["PT102"](4095) dá 409,5 e por que a sua criar_conversores não tem o problema. -->

### R4 — Escala nominal

<!-- Hipótese para a diferença da Etapa 2(f) e onde, no código da base, está a explicação. -->

### R5 — Previsão × medição (Etapa 3)

Previsões registradas no commit: <!-- cole o hash curto do commit de previsões -->

| Grandeza | Previsão | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` | 4| |
| Tempo do laço / tempo vetorizado | 10| |
| Tempo da compreensão / tempo do laço | 0.5| |

<!-- Explique a maior diferença entre previsão e medição; por que uint16 * 20 dá 16364; que dtype você escolheria para contagens e para kPa. -->

### R6 — Tipos da SerieTemporal (Etapa 4d)

| Expressão | Tipo previsto | Tipo observado |
| --- | --- | --- |
| `s + s` | array SerieTemporal| |
| `s[1:]` | array SerieTemporal| |
| `s * 2` | array SerieTemporal| |
| `s.sum()` | float| |
| `s[0]` | float| |

<!-- Explique o resultado que mais surpreendeu você. -->

### R7 — Issue #4

<!-- Sintoma; o teste de regressão (nome); a causa, em termos da soma acumulada; a correção; por que os testes de aceitação não pegaram o defeito; mais um caso que eles não cobrem e qual teste seu o cobre. -->
