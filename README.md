# Install

- Add 'django_contact' app to INSTALLED_APPS

- Add Email settings to settings.py

```python
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'email_host_user'
EMAIL_HOST_PASSWORD = 'password_goes_here'
EMAIL_PORT = 587
```

- Add RECIPIENTS_LIST list or tuple of recipients email in settings.py