kubectl delete configmap tasks || echo ''
kubectl create configmap tasks --from-file=tasks.py

