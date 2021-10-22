# Exemplo de recebimento de _webhooks_ do _marketplace_ do Consulta Remédios

Exemplo em Python de um sistema que recebe _webhooks_ de pedidos do _marketplace_ do Consulta Remédios. A documentação oficial da API e dos _webhooks_ do sistema de _marketplace_ pode ser encontrada [aqui](https://developers.consultaremedios.com.br/marketplace/api/index.html).

Este código foi criado para servir de exemplo aos desenvolvedores das lojas, redes ou integradores de como receber notificações enviadas pelo sistema de _marketplace_. Sugere-se que ele seja usado como referência para a implementação, mas não como base. Este código é fornecido sem garantia.

## Visão geral

O sistema de _marketplace_ do Consulta Remédios dispõe de ferramentas padrão para integração com sistemas das lojas, redes e integradores. Estas ferramentas têm como objetivo manter o estoque e o preço dos produtos disponíveis no _marketplace_ em sincronia com o sistema da loja, bem como manter a lista de pedidos da loja em sincronia com os feitos no _marketplace_. Para tal, é disponibilizada uma API e um mecanismo de envio de notificações (_webhooks_). Sempre que há um novo pedido ou uma alteração (atualização ou cancelamento) em um pedido existente, o sistema de _marketplace_ envia uma notificação usando este mecanismo. A notificação tem a forma de uma requisição HTTP com método `POST`, que é enviada para um URL fixo definido na configuração da loja dentro do sistema de _marketplace_.

## Estrutura do código

Este projeto foi desenvolvido em Python e implementa um servidor construído usando a biblioteca _Flask_. O servidor implementa uma única rota (`/notification`) responsável por receber os _webhooks_. Ao receber um _webhook_, o servidor imprime uma mensagem em console com o número do pedido e o tipo do evento.

A biblioteca _Flask_ permite construir um servidor de forma modular, registrando rotas parciais em objetos especiais denominados _"blueprints"_. O servidor de exemplo foi construído com base neste paradigma.

O módulo `consulta_remedios_webhooks` expõe uma única função, `create_flask_blueprint`, que cria um _blueprint_ que implementa a rota que recebe a notificação. O _blueprint_ é criado com base em uma função de _callback_ que será invocada sempre que o _webhook_ receber uma notificação.

## Executando localmente

Para instalar as dependências, sugere-se criar um ambiente virtual e ativá-lo. Sendo em um ambiente virutal ou não, use o comando a seguir para instalar as dependências:

    pip install -r requirements.txt

Para executar a aplicação, basta executar:

    python app.py

## Licença

Este código é liberado sob a licença MIT. A licença encontra-se no arquivo `LICENSE.txt`.
