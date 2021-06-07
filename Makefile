docker:
	docker build -t 551134495857.dkr.ecr.us-east-1.amazonaws.com/caishen_dashboard:latest -f Dockerfile .
	aws --profile caishen ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 551134495857.dkr.ecr.us-east-1.amazonaws.com/caishen_dashboard
	docker push 551134495857.dkr.ecr.us-east-1.amazonaws.com/caishen_dashboard:latest
