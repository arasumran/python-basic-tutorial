from prometheus_client import Info
from prometheus_client.twisted import MetricsResource
from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

IN_PROGRESS = Info("connection_requests_result", 'this is None lan')


def app():
    try:
        import ftplib
        f = ftplib.FTP()
        f.connect("10.133.151.9", 23, timeout=2)
        f.login("atlantis", "q1w2e3r4")
        IN_PROGRESS.info({'status': 'OK'})
    except:
        IN_PROGRESS.info({'status': 'ERROR'})


if __name__ == '__main__':
    while True:
        root = Resource()
        root.putChild(b'metrics', MetricsResource())
        factory = Site(root)
        reactor.listenTCP(4545, factory)
        reactor.run()
        app()
