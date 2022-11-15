# django-subdomains

A simple application to get which subdomain the django project has been accessed.

## Installation

- `pip install -e git+https://github.com/gabrielloliveira/django-subdomains`

## Configuration

- Set any subdomain access in allowed hosts = `ALLOWED_HOSTS=[".example.com"]`
- Add `subdomains` in `INSTALLED_APPS`
- Run `migration` command
- Put `subdomains.middleware.SubddomainMiddleware` in `MIDDLEWARE` settings

## Usage

The `SubddomainMiddleware` will set the subdomain attribute inside the request object. 
The value of the subdomain attribute can be a Subdomain or None instance.

Example of use:

```python
class Company(models.Model):
    name = models.CharField(max_lenght=255)
    subdomain = models.OneToOne(
        "subdomains.Subdomain", 
        on_delete=models.CASCADE, 
    )
```

Then, every time you get a request, you can do something like this:

```python
def index(request):
    company = request.subdomain.company
    return HttpResponse(f"{company}")
```

