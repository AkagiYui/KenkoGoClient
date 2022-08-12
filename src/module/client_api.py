import traceback

from module.global_dict import Global
from module.logger_ex import LoggerEx, LogLevel


class ClientApi:
    """Client API"""

    def __init__(self, name=None):
        self.name = name or traceback.extract_stack()[-2].name
        self.log = LoggerEx(f'{self.__class__.__name__} {name}')
        if Global().debug_mode:
            self.log.set_level(LogLevel.DEBUG)

    @staticmethod
    def get_info() -> dict:
        """获取Client的信息"""
        return Global().information

    def disconnect(self) -> None:
        """断开连接"""
        self.log.debug('Disconnecting...')
        kenko_go = Global().kenko_go
        kenko_go.stop_websocket()
        self.log.debug('Disconnected.')

    def connect(self) -> None:
        """连接"""
        self.log.debug('Connecting...')
        kenko_go = Global().kenko_go
        kenko_go.start_websocket()
        self.log.debug('Connected.')

    def get_plugins(self) -> list:
        """获取插件列表"""
        self.log.debug('Getting plugins...')
        plugin_manager = Global().plugin_manager
        plugins = plugin_manager.plugin_list
        self.log.debug('Got plugins.')
        return plugins
