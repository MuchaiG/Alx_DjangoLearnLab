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

