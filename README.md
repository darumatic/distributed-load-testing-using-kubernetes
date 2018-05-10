## Distributed Load Testing Using Kubernetes

This tutorial demonstrates how to conduct distributed load testing using [Kubernetes](http://kubernetes.io) and includes a sample web application, Docker image, and Kubernetes controllers/services. 


## Deploy Controllers and Services

Before deploying the `locust-master` and `locust-worker` controllers, update each to point to the location of your deployed sample web application. Set the `TARGET_HOST` environment variable found in the `spec.template.spec.containers.env` field to your sample web application URL.

    - name: TARGET_HOST
      value: http://example.com


