import json
import boto3

def lambda_handler(event, context):
    bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')
    
    model_id = 'us.amazon.nova-micro-v1:0'
    prompt = "Responda apenas: A integracao entre AWS Lambda e Amazon Bedrock esta OK."
    
    body = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 50,
            "temperature": 0.3
        }
    })
    
    try:
        response = bedrock.invoke_model(
            body=body,
            modelId=model_id,
            accept='application/json',
            contentType='application/json'
        )
        
        response_body = json.loads(response.get('body').read())
        output_text = response_body['output']['message']['content'][0]['text']
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'response': output_text.strip()})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
