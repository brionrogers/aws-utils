# AWS 
## Fargate
aws ecs execute-command --region $AWS_REGION --profile $AWS_SSO_PROFILE_FROM_CONFIG --cluster $CLUSTER_NAME --task $TASK_ARN_FROM_CLUSTER --container $CONTAINER_NAME_FROM_TASK --command bash --interactive
aws ecs update-service --region $AWS_REGION --profile $AWS_SSO_PROFILE_FROM_CONFIG --force-new-deployment --service my-$TASK_NAME --cluster $CLUSTER_NAME

# Curl
## Make a curl request that requires a cookie
curl -b cookie.txt -c cookie.txt -X POST "<AUTHENTICATION URL>" -H  "accept: application/json" -H  "SOMEHEADER: SOMEVALUE" -H  "X-Auth-Password: <password>" -H  "X-Auth-Username: <username>"
curl --cookie cookie.txt --cookie-jar cookie.txt -X POST "<SOME AUTHENTICATED ENDPOINT>" -H  "accept: application/json" -H  ""
