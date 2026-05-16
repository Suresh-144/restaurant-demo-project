<img width="1920" height="1020" alt="Screenshot 2026-02-14 182023" src="https://github.com/user-attachments/assets/3559e0ff-3428-4434-ae5b-829b700b324a" />

how to deploy this application using argoCD ?

STEP-1:
CREATE CLUSTER USING KOPS/eks

STEP-2:
INSTALL HELM:

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3

chmod 700 get_helm.sh

./get_helm.sh

helm version

STEP-3:
INSTALL ARGO CD USING HELM

helm repo add argo-cd https://argoproj.github.io/argo-helm

helm repo update

kubectl create namespace argocd

helm install argocd argo-cd/argo-cd -n argocd

kubectl get all -n argocd


STEP-4:

EXPOSE ARGOCD SERVER:

kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'

kubectl get all -n argocd

NOTE: GIVE OR CHECK SG FOR PORTS


COPY PASTE DNS TO BROWSER

ADVANCE

LOGIN PAGE

username: admin

passowd:


TO GET ARGO CD PASSWORD:


kubectl -n argocd get secret argocd-initial-admin-secret -o yaml

decode the above secret (echo -n "data" | base64 -d)

The above command to provide password to access argo cd

IN REAL FOR DEV &TEST ENV WE CAN USE 100% AUTOMATED DEPLOYENTS

FOR PRODUCTION WE PERFER SEMI-AUTOMATED.
 

NEW APP

NAME: APP1

PROJECT NAME: default

Sync Policy: Manual

REPO: https://github.com/suresh-144/restaurant-k8s-files.git

PATH: ./

CLUSTER URL: https://kubernetes.default.svc

NAMESPACE: default

CREATE


SYNC

SYNCHRONIZE

you get a loadbalancer dns in service run the dns in browser you get the output