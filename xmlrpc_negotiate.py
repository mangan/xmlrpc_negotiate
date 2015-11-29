"HTTP Negotiate auth for XMLRPC"

import xmlrpclib

import kerberos


class SafeTransport(xmlrpclib.SafeTransport):
    "XMLRPC over HTTPS with Negotiate auth"
    def get_host_info(self, host):
        host, extra_headers, x509 = \
            xmlrpclib.SafeTransport.get_host_info(self, host)

        service = "HTTP@%s" % host
        _, client = kerberos.authGSSClientInit(service)
        kerberos.authGSSClientStep(client, "")
        token = kerberos.authGSSClientResponse(client)

        extra_headers = [("Authorization", "Negotiate %s" % token)]

        return host, extra_headers, x509
