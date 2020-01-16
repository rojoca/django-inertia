# django-inertia
Django Integration for Inertia JS

## Planning

Requirements to satisfy the InertiaJS protocol:

* POC
* Middleware to intercept inertia requests
* Serializer for inertia JSON responses
* Template for responses
* A way to bundle static assets - django-webpack-loader
* Build steps for JS (dev / prod)

## POC

* Create simple django app
* Create simple Vue app with inertia dependency
* Create middleware to intercept inertia requests
* Create serializer for inertia response
* Create template to handle inertia bootstrap stage (full page response)
* Evaluate hard / complex issues
