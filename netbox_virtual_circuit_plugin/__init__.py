from extras.plugins import PluginConfig


class VirtualCircuitConfig(PluginConfig):
    """This class defines attributes for the NetBox Virtual Circuit Plugin."""

    name = 'netbox_virtual_circuit_plugin'
    verbose_name = 'Virtual Circuit'
    description = 'Netbox Virtual Circuit Plugin'
    version = '0.1'
    base_url = 'virtual-circuit'
    author = 'Hoanh An'
    author_email = 'hoanh@vapor.io'
    required_settings = []
    default_settings = {}
    caching_config = {}


config = VirtualCircuitConfig
