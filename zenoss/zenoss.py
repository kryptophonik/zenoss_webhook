from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

class ZenossWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        if 'environment' not in payload:
            raise ValueError('Environment must be set.')

        status = payload['state'].lower()
        if status == '0':
            severity = payload['severity'].lower()
        elif status == '1':
            severity = payload['severity'].lower()
            status = 'ack'
        elif status == '4':
            severity = 'ok'
        elif status == '5':
            severity = 'cleared'
        elif payload['severity'].lower() == 'info':
            severity = 'informational'
            status = 'open'
        else:
            severity = payload['severity'].lower()
            status = 'open'

        attributes = dict()
        if 'incident_url' in payload:
            attributes['event_url'] = '<a href="%s" target="_blank">Event URL</a>' % payload['event_url']
        if 'runbook_url' in payload:
            attributes['runBook'] = '<a href="%s" target="_blank">Runbook URL</a>' % payload['runbook_url']

        return Alert(
            resource=payload['resource'],
            event=payload['event'],
            environment='Production',
            severity=severity,
            status=status,
            service=[payload['service']],
            group=payload['group'],
            text=payload['test'],
            tags=['{}:{}'.format(key, value) for (key, value) in payload['targets'][0]['labels'].items()],
            attributes=attributes,
            origin=payload['origin'],
            event_type=payload['event_type'].lower(),
            raw_data=payload
        )
