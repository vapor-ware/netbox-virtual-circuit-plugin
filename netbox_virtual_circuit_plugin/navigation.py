from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_virtual_circuit_plugin:list_virtual_circuits',
        link_text='Virtual Circuits',
        permissions=[],
        buttons=(
            # Link to the admin view to add a virtual circuit if user has "add_virtualcircuit" permission.
            PluginMenuButton(
                link='admin:netbox_virtual_circuit_plugin_virtualcircuit_add',
                title='Add a new virtual circuit',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_virtual_circuit_plugin.add_virtualcircuit']
            ),
            # Links to the admin view to assign a virtual circuit to a VLAN if user has the "add_virtualcircuitvlan" permission.
            PluginMenuButton(
                link='admin:netbox_virtual_circuit_plugin_virtualcircuitvlan_add',
                title='Assign a virtual circuit to a VLAN',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.BLUE,
                permissions=['netbox_virtual_circuit_plugin.add_virtualcircuitvlan']
            ),
        )
    ),
)
