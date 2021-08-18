# PROGRAM.PY
> O script mencionado faz uma busca por instâncias EC2 em execução na sua região e retorna algumas informações básicas sobre a instância, VPC e Security Group da mesma.

## Instalação

_Não há necessidade de fazer instalação do script, apenas ter o ambiente configurado conforme os pré requisitos listados logo abaixo. Todos os testes e uso foram feitos no ambiente linux, portanto os próximos passos é considerando que esteja utilizando o SO mencionado ou o WSL2._

### Pré Requisitos do ambiente

* Ter o AWS CLI instalado e configurado na sua máquina com sua 'aws_access_key_id', 'aws_secret_access_key' e 'region'
    * Instalar AWS CLI: https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-install.html
    * Configurar AWS CLI: https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html
* Ter o Python3 e a biblioteca BOTO3 instalados
    * Instalar Python3: https://docs.aws.amazon.com/pt_br/parallelcluster/latest/ug/install-linux-python.html
    * Instalar BOTO3: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation

## Uso

1. Fazer download do arquivo 'program.py' e salvar na pasta de sua preferência.
2. Abrir o terminal Linux ou o WSL se for o seu caso.
3. Navegar até o diretório onde salvou o arquivo.
4. Estando no diretório do arquivo, executar o comando:

```sh
python3 program.py
```

## Contribuição

1. Fork (<https://github.com/nivaldogodinho/tellMeEC2.git>)
2. Crie sua branch de recursos (`git checkout -b feature`)
3. Commit suas modificações (`git commit -am 'Adicionando recursos'`)
4. Push para a branch (`git push origin feature`)
5. Crie um novo Pull Request

## Aviso

```sh
A informação sobre SUBNET ROUTE TABLE estão imprecisas, o mesmo está sendo verificado e será disponibilizado nova versão do script com a correção do problema!
```