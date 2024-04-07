import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2024-04-04-16-55-08-513'

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['image_data']) ## TODO: fill in)

    # Instantiate a Predictor
    predictor = sagemaker.predictor.RealTimePredictor(ENDPOINT)## TODO: fill in

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image)## TODO: fill in
    
    # We return the data back to the Step Function    
    event["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }