import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20190711 import sms_client, models
def send(PhoneNumber,code,time):
    try:
        cred = credential.Credential("AKIDmgtp5LNhTt6CH8wb1hHUM1zgJqBGwhMQ", "BzZdLnV0nddIjvudFwWZNn0wwjHazAyd")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "sms.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = sms_client.SmsClient(cred, "", clientProfile)

        req = models.SendSmsRequest()
        params = {
            "PhoneNumberSet": [ PhoneNumber ],
            "TemplateParamSet": [code, time],
            "TemplateID": "848436",
            "SmsSdkAppid": "1400476949",
            "Sign": "望尽阑珊"
        }
        req.from_json_string(json.dumps(params))

        resp = client.SendSms(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)