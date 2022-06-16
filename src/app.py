from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.event_handler import ALBResolver, CORSConfig

tracer = Tracer()
logger = Logger()
app = ALBResolver(cors=CORSConfig(max_age=1))

@app.get("/hello")
@tracer.capture_method
def get_hello_universe():
    return {"message": "hello universe"}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.APPLICATION_LOAD_BALANCER)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
