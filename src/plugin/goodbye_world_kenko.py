from assets.cq_code import CqCode
from assets.simple_plugin import SimplePlugin
from module.client_api import ClientApi
from module.gocq_api import GocqApi
from module.server_api import ServerApi


class GoodbyeWorld(SimplePlugin):
    def __init__(self, api: GocqApi, client: ClientApi, server: ServerApi):
        super().__init__(api, client, server)
        self.api = api
        self.client = client
        self.server = server
        self.name = '再见，世界！'
        self.description = '这还是一个插件示例'
        self.version = '1.2.3'

    def on_message(self, message: dict) -> bool:
        return True  # 返回True表示消息将被传递给下一个插件，否则表示消息被拦截