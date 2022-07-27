from module.client_api import ClientApi
from module.gocq_api import GocqApi
from module.server_api import ServerApi


class SimplePlugin:
    def __init__(self, api: GocqApi, client: ClientApi, server: ServerApi):
        """实例初始化

        此处仅用作初始化插件信息，建议不要处理其他代码，以免发生异常情况
        """
        self.api = api
        self.client = client
        self.server = server
        self.name = '简单插件'
        self.description = '这是一个插件模板'
        self.version = '#error#'

    def on_initialize(self):
        """插件初始化，你可以在这里初始化一些依赖"""
        ...
        return self  # 务必返回self

    def on_enable(self):
        """插件被启用"""
        ...
        return self  # 务必返回self

    def on_before_disable(self):
        """插件将被禁用，你还可以处理一些事情"""
        ...
        return self  # 务必返回self

    def on_disable(self):
        """插件已被禁用，可以用于清理一些资源"""
        ...
        return self  # 务必返回self

    def on_connect(self):
        """已连接到KenkoGo服务器"""
        ...
        return self  # 务必返回self

    def on_disconnect(self):
        """已断开服务器连接"""
        ...
        return self  # 务必返回self

    def on_message(self, message: dict):
        """收到 go-cqhttp 消息"""
        ...
        return True  # 返回True表示消息将被传递给下一个插件，返回False表示消息被拦截
