# Security Notes for LibraryProject

This file documents the security configuration and why each setting is used.

## Django settings
- `DEBUG = False` in production to avoid leaking debug info.
- `ALLOWED_HOSTS` must list the production hostnames.
- `X_FRAME_OPTIONS = "DENY"` prevents clickjacking.
- `SECURE_BROWSER_XSS_FILTER = True` and `SECURE_CONTENT_TYPE_NOSNIFF = True` enable browser protections.
- `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` ensure cookies are only sent over HTTPS.

## CSRF protection
- All forms include `{% csrf_token %}`.
- Views that modify data are protected with `@permission_required` and `@login_required` as needed.

## Input validation & SQL safety
- Use Django `forms` for validation (see `bookshelf/forms.py`).
- Use the Django ORM (parameterized). Avoid raw SQL or use parameter substitution.

## Content Security Policy
- Use `django-csp` or the provided `SimpleCSPMiddleware` to set CSP headers to mitigate XSS.
- Test CSP in stages; start with `report-only` mode if supported.

## Permissions & Groups
- Custom permissions on the `Book` model: `can_view`, `can_create`, `can_edit`, `can_delete`.
- Groups created: `Viewers`, `Editors`, `Admins`.

## Testing
- Manually test access with users in different groups.
- Use Django tests to assert permission enforcement for critical actions.




HTTPS & Secure Headers review
-----------------------------
- HTTPS enforcement: SECURE_SSL_REDIRECT = True ensures all HTTP requests redirected to HTTPS.
- HSTS: SECURE_HSTS_SECONDS=31536000 with includeSubdomains and preload flags configured; only enabled when HTTPS is stable.
- Cookie security: SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE set to True so cookies are sent only over HTTPS.
- Proxy awareness: SECURE_PROXY_SSL_HEADER set so Django recognizes secure requests behind nginx/load balancer.
- Clickjacking & MIME sniffing: X_FRAME_OPTIONS="DENY", SECURE_CONTENT_TYPE_NOSNIFF=True.
- Deployment: Nginx is configured to redirect HTTP to HTTPS and proxy to Django. TLS certs are provided by Let's Encrypt via certbot.
- Testing: verify redirects and headers using curl; run certbot renew --dry-run to confirm renewal works.
Potential improvements:
- Add HTTP Public Key Pinning (HPKP) is deprecated and not recommended.
- Add multi-layer rate limiting (nginx or CDN) for endpoints like login and search.
- Consider using a WAF / CDN (Cloudflare, AWS CloudFront) fronting the app for DDoS and extra TLS features.
