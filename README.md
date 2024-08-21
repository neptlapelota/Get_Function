# Descrição do Código:
Este script em Python é utilizado para ler os primeiros 20 subdomínios de um arquivo de texto, e para cada subdomínio, realiza uma requisição HTTP GET ao servidor correspondente, utilizando o domínio base exemplo.com. O código exibe o código de status HTTP de cada requisição e trata eventuais erros de conexão, evitando que o script pare em caso de falha.

# Estrutura do Código:
Função function():

Abre o arquivo subdomains-top1million-5000.txt em modo de leitura.
Lê os primeiros 20 subdomínios e os armazena em uma lista.
Retorna a lista de subdomínios.
Requisições HTTP:

Para cada subdomínio na lista, constrói uma URL no formato http://<subdominio>.exemplo.com.
Realiza uma requisição HTTP GET utilizando o módulo requests.
Exibe o código de status HTTP de cada requisição.
Caso ocorra um erro (como falha de conexão ou resolução de DNS), o erro é tratado e uma mensagem de erro é exibida.

# Localização do Arquivo
O arquivo subdomains-top1million-5000.txt está localizado no diretório E:\FIAP\PROGRAMAÇÃO\google clone\.py\Nova pasta\. Certifique-se de que o caminho do arquivo está correto e que o arquivo existe no local indicado.

# Como Utilizar:
Certifique-se de que o arquivo subdomains-top1million-5000.txt está presente no diretório especificado no código.
Altere o domínio base "exemplo.com" para o domínio de interesse que você deseja testar com os subdomínios.
Execute o script. Ele exibirá os códigos de status HTTP para cada subdomínio acessado ou uma mensagem de erro em caso de falha.

# Exemplo de saída:
![image](https://github.com/user-attachments/assets/955d468e-d0ae-407a-9bda-36fdaa8d1a21)

# Requisitos
Python 3.x
Biblioteca requests instalada (pip install requests)
Um arquivo de texto contendo uma lista de subdomínios localizado no caminho especificado no código.
# Tratamento de Erros
O código utiliza um bloco try/except para capturar e tratar possíveis erros de requisição, como falhas de conexão, resolução de DNS ou problemas no servidor. Isso garante que o programa continue a execução mesmo que uma ou mais requisições falhem.

# Personalização
Domínio Base: Você pode alterar o domínio base "exemplo.com" na linha que constrói a URL, substituindo-o pelo domínio de sua escolha.
Quantidade de Subdomínios: Se desejar testar mais ou menos subdomínios, basta modificar o valor passado para [:20] no código para o número desejado.
