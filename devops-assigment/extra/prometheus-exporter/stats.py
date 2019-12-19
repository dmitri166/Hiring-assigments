from prometheus_client.core import (
    GaugeMetricFamily, REGISTRY
)
import prometheus_client
import random


class Exporter:
    def collect(self):
        demo = GaugeMetricFamily('flask_demo_metric',
                                 'total cost for sms on endpoint',
                                 labels=['demo_label'])

        demo.add_metric(['some_random_label'],
                        random.randint(0, 1000))

        yield demo

# Local testing
if __name__ == '__main__':
    from prometheus_client.exposition import generate_latest
    print(generate_latest(REGISTRY).decode('utf-8'))

REGISTRY.register(Exporter())
app = prometheus_client.make_wsgi_app()
