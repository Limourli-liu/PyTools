from Autolnstaller import keepInstalled
keepInstalled({'baidu-aip'})
from aip import AipOcr
from conf import Conf

""" 你的 APPID AK SK """
with Conf('baiduOCR') as conf:
    APP_ID = conf['key']['APP_ID']
    API_KEY = conf['key']['API_KEY'] 
    SECRET_KEY = conf['key']['SECRET_KEY']
    options = dict(conf['options'])

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def BaiduOCR(image, options=options):
    if isinstance(image, str):
        results = client.basicGeneralUrl(image, options)
    else:
        results = client.basicGeneral(image, options)
    if 'error_code' in results:
        print (f'BaiduOCR error {results["error_code"]} {results["error_msg"]}')
        return ''
    return ''.join(line['words'] for line in results['words_result'] if 'words' in line)