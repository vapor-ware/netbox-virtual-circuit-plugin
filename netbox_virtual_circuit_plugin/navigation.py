from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_virtual_circuit_plugin:virtual_circuit_list',
        link_text='Virtual Circuits',
        permissions=[],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_virtual_circuit_plugin:virtual_circuit_add',
                title='Add a new virtual circuit',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_virtual_circuit_plugin.add_virtualcircuit']
            ),
            PluginMenuButton(
                link='plugins:netbox_virtual_circuit_plugin:virtual_circuit_vlan_add',
                title='Assign a virtual circuit to a VLAN',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.BLUE,
                permissions=['netbox_virtual_circuit_plugin.add_virtualcircuitvlan']
            ),
        )
    ),
)
