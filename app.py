from flask import Flask

from consulta_remedios_webhooks import create_flask_blueprint

app = Flask(__name__)

def handle_webhook(event_type, order_number, state=None, timestamp=None, **kwargs):
    print('##########')
    print(' EVENT TYPE: ' + event_type)
    print(' ORDER_NUMBER: ' + order_number)

webhooks_blueprint = create_flask_blueprint('/notification', handle_webhook)

app.register_blueprint(webhooks_blueprint)

if __name__ == '__main__':
    app.run(port=1234)
