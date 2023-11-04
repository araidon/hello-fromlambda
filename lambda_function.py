import json
import io
#import logging
#from fdk import response

print('Loading function')

# handlerの引数変更、event -> dataに変更
#def lambda_handler(event, context):
#def handler(ctx, data: io.BytesIO = None):
def lambda_handler(ctx, data: io.BytesIO = None):

    try:
        event = json.loads(data.getvalue())
        #print("Received event: " + json.dumps(event, indent=2))
        print("value1 = " + event['key1'])
        print("value2 = " + event['key2'])
        print("value3 = " + event['key3'])
    except (Exception, ValueError) as ex:
        print("error pasrsing json payload" + str(ex))
#        logging.getLogger().info('error parsing json payload: ' + str(ex))

    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')