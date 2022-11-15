from subdomains.models import Subdomain


class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        dns = host.split(".")

        # Get subdomain instance
        subdomain = dns[0] if len(dns) > 1 else None
        instance = Subdomain.objects.filter(subdomain=subdomain).first()
        setattr(request, "subdomain", instance)

        response = self.get_response(request)

        return response
