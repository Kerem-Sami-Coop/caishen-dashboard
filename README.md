# Building and Deploying the Container
Run the following
```bash
make docker
```

# Local Testing
To test locally run the following 
```bash
docker build -t 551134495857.dkr.ecr.us-east-1.amazonaws.com/caishen_dashboard:latest -f Dockerfile .
docker run --rm -it -p 8050:8050 551134495857.dkr.ecr.us-east-1.amazonaws.com/caishen_dashboard:latest
```
Check `127.0.0.1:8050` address to check the result