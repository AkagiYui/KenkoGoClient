from assets.simple_plugin import SimplePlugin


class TestPlugin(SimplePlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = '测试插件'
        self.description = '该插件仅作调试用处'
        self.version = 'Test Only'

    def on_message(self, message: dict) -> bool:
        if message['post_type'] == 'message':
            msg: str = message['raw_message']
            if msg == 'tsa1':
                from assets.cq_code import CqCode
                message['message'] = CqCode.record_local('dyy.mp3')
                self.api.send_msg(message)
        return True  # 返回True表示消息将被传递给下一个插件，否则表示消息被拦截
