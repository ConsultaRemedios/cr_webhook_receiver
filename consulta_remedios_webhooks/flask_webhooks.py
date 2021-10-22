def create_blueprint(route, callback):
    """
    Creates a Flask blueprint (see: <https://flask.palletsprojects.com/en/2.0.x/api/#flask.Blueprint>) which receives
    webhooks triggered by the Consulta Remédios marketplace system. 
    
    The provided callback should take two positional arguments (the event type and the order number) and a number of
    named arguments (currently, depending on the event type, the event timestamp and the order state).
    """

    from flask import Blueprint, request, Response, json
    from http import HTTPStatus

    blueprint = Blueprint('webhooks', __name__)

    def handle_notification():
        try:
            event_body = request.json
            event_type = event_body.get('event')
            order_number = ''
            other_params = {}
            if event_body.get('data') is not None:
                order_number = event_body['data'].get('order_number')
                for key in ['state', 'timestamp']:
                    value = event_body['data'].get(key)
                    if value is not None:
                        other_params[key] = value
            order_number = order_number or ''
            callback(event_type, order_number, **other_params)
            return Response(
                json.dumps({ 'result': 'SUCCESS' }),
                status=HTTPStatus.OK,
                mimetype='application/json',
            )
        except:
            return Response(
                json.dumps({ 'result': 'ERROR', 'error_type': 'INTERNAL_ERROR' }),
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
                mimetype='application/json',
            )

    blueprint.route(route, methods=['POST'])(handle_notification)

    return blueprint
