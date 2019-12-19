# Assignment used for DevOps position
This task is intended for candidates applying for a DevOps position at the OnlineCity DevOps team. 
The assignment is built around the technologies and stack used in the production environments of the team, and the problem is a toy version of some of the tasks we face.


![Interview](./interview-gopher.png)


## The problem
Many of our services has some sort of an API towards our customers. We need to have allot of monitoring for our service, so we can keep an eye on RPS and faulty requests.

For this task we have made a small Flask applikation that, enables the user to upload a file to the applikation.


## The sample code
We have provided the code for a simple Flask app and an example envoy deployment.

### Prerequisits
You need to have a minikube our another kubernetes cluster available and be able to use `kubectl`

### Local testing
To start up a minikube cluster [Have to install minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)

### Deploy on Kubernetes
Firstly you need to build the Docker image and push it to some image registry that your cluster has access to. 
```
kubectl apply -f flask-app/manifests/flask-app.yaml
kubectl expose deployment app --type=NodePort
minikube service app
```

## Your Task
We would like you to extend this system to be more functional and make the system more "production ready".
You find some mandatory task from part 1 you should do first. Afterwards you choose one or more larger task from part 2 and 3. 

### Part 1 - The mandatory part
Deploy an Envoy proxy infront of the Flask app to handle all the requests. 

* Deploy prometheus to scrape envoy metrics and create a route in envoy to handle requests to prometheus.
* Only some file extensions are allow and some new that would fit in.

### Part 2 - The optional operations
Beyond the mandatory part we would like you to extend our service in some way. 
Choose one or more larger task from below:
* Add some sort of storage solution for the app. At the moment files are being uploaded to the pod and when the has been restart or deleted files are gone. 
* Add TLS encryption to envoy, either use Let's Encypt or what you can come up with.
* Deploy Grafana and route trafic from envoy to it. Create a dashboard and use some of the metrics from envoy.


### Part 3 - The optional coding
Beyond the mandatory part we would like you to extend our service in some way. 
Choose one or more larger task from below:
* The Flask app listens on port 5000 by default, make it possible to set the port as an `ENV` from the deployment file. 
* Create a prometheus exporter that counts the amount of files uploaded. You can find an example in the extra folder.
* Benchmark the applikation, create a script that uploads allot of files or something else that you think would put load on the applikation.