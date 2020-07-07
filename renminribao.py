import frida, sys
import time



test_sky = """
    Java.perform(function(){
        var cir = Java.use('com.peopledaily.common.utils.encrtption.MD5Helper'); 
        cir.getMD5Str.implementation = function(c){
            console.log("加密参数: " + c);
            var s = this.getMD5Str(c);
            console.log("返回结果: " + s);
            return s;
        }
    })

"""


def read_file_all(file):
    fp = open(file, encoding='utf-8')
    text = fp.read()
    fp.close()
    return text

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


def opp():
    process = frida.get_usb_device().attach('com.peopledailychina.activity')
    # jss = read_file_all('hash.js')
    # script = process.create_script(test_sky)
    script = process.create_script(test_sky)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()


# def hook_prepare():
#     process = frida.get_usb_device().attach('com.sankuai.meituan')
#     script = process.create_script(test_sky)
#     script.on('message', on_message)
#     script.load()
#     print('hook_prepare is ok')
#     return script


# hook_prepare()
if __name__ == "__main__":
    opp()