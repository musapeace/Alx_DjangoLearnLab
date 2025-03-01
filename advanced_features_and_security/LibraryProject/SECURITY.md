# Security Measures in LibraryProject

## 1. Secure Settings
- `DEBUG` is set to `False` to prevent sensitive data exposure.
- `SECURE_BROWSER_XSS_FILTER = True` to mitigate XSS attacks.
- `X_FRAME_OPTIONS = 'DENY'` to prevent clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` to prevent MIME-type sniffing attacks.
- `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` to ensure cookies are sent over HTTPS only.

## 2. CSRF Protection
- All forms include `{% csrf_token %}` to prevent CSRF attacks.

## 3. SQL Injection Prevention
- Django ORM is used instead of raw SQL queries to avoid injection risks.
- User input is validated before processing.

## 4. Content Security Policy (CSP)
- Configured CSP headers to limit allowed sources for scripts and styles.
