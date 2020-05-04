from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_virtual_circuit_plugin:list_virtual_circuits',
        link_text='List all virtual circuits',
        permissions=[],
    ),
)
