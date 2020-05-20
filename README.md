# NetBox Virtual Circuit Plugin

A plugin for [NetBox](https://github.com/netbox-community/netbox) that supports
Virtual Circuit management.

## Definitions

A Virtual Circuit is a circuit created by routing two or more VLANs together.

Each Virtual Circuit is identified by a name, a numeric ID (0-32767), along with
a context. Each Virtual Circuit must be assigned one of the following operational
statuses:
- Pending Configuration
- Configured
- Pending Deletion
- Configuration Error

When a VLAN is assigned to a Virtual Circuit, it can not exist in another Virtual
Circuit without first being removed.

## Installing

Since the plugin is published on
[PyPI](https://pypi.org/project/netbox-virtual-circuit-plugin/), simply issue:
```python
pip install netbox-virtual-circuit-plugin
```
to download and install it.

To enable to plugin, add the plugin's name to the `PLUGINS` list in
`configuration.py` like so:
```python
PLUGINS = ['netbox_virtual_circuit_plugin'] # Note that the name here use underscore, not hyphen.
```

Don't forget to restart NetBox to load the new plugin.

For more information about installing plugins, refer to [NetBox's
documentation
](https://netbox.readthedocs.io/en/stable/plugins/).

## Using

Once the plugin is installed correctly as instructed above, one can find the
**Virtual Circuit** section under **Plugins** navigation tab via NetBox UI
that is ready to use with correct *admin* permission.

As for REST API use cases, the 2 group endpoints are exposed at:
- `/api/plugins/virtual-circuit/virtual-circuits`
- `/api/plugins/virtual-circuit/vlans`

While the former one is for creating/retrieving/modifying/deleting Virtual
Circuits, the later one is for assigning and managing Virtual-Circuit-to-VLAN
connections. For more information, refer to `/api/docs` as it also conforms
to Swagger Specification for hosted visual documentations.

## Developing

Plugins are essentially self-contained Django apps which integrate with NetBox
to provide custom functionality. For more information, see [NetBox
documentation](https://netbox.readthedocs.io/en/stable/plugins/development/).

## Contributing

If you experience a bug, would like to ask a question, or request a feature,
open a new issue and provide as much context as possible. All contributions,
questions, and feedback are welcomed and appreciated.

## License

NetBox Virtual Circuit Plugin is licensed under GPLv3. See [LICENSE](LICENSE)
for more info.
