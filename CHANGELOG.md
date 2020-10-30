# Changelog

## [Unreleased](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/tree/HEAD)

[Full Changelog](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/compare/v1.4.0...HEAD)

**Implemented enhancements:**

- `vlan\_of` related name is awkward [\#41](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/41)

## [v1.4.0](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/tree/v1.4.0) (2020-10-30)

[Full Changelog](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/compare/v1.1.0...v1.4.0)

**Implemented enhancements:**

- Add a box for Virtual Circuits in the tenant information screen. [\#40](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/40)

**Closed issues:**

- Include device in VLAN list next to interface [\#42](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/42)
- netbox:: ChangeLoggedModel has moved location and is now in extras [\#37](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/37)

**Merged pull requests:**

- Update VCVLAN related name [\#46](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/46) ([hoanhan101](https://github.com/hoanhan101))
- Inject Virtual Circuit counts to Tenant screen [\#45](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/45) ([hoanhan101](https://github.com/hoanhan101))
- Include VLAN's interface parent [\#44](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/44) ([hoanhan101](https://github.com/hoanhan101))

## [v1.1.0](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/tree/v1.1.0) (2020-09-22)

[Full Changelog](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/compare/v1.0.0...v1.1.0)

**Fixed bugs:**

- Plugin fails jsonschema/open api validation [\#34](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/34)

**Closed issues:**

- Setup GitHub Actions pipeline [\#30](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/30)

**Merged pull requests:**

- Fix NetBox 2.9.3 compatibility issues [\#38](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/38) ([hoanhan101](https://github.com/hoanhan101))

## [v1.0.0](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/tree/v1.0.0) (2020-08-21)

[Full Changelog](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/compare/v0.3.1...v1.0.0)

**Implemented enhancements:**

- Add VCID plugin info inside "Change Log" [\#31](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/31)

**Merged pull requests:**

- Fix swagger missing id [\#35](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/35) ([hoanhan101](https://github.com/hoanhan101))
- Include change log [\#32](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/32) ([hoanhan101](https://github.com/hoanhan101))
- Set VCID's range from 1 to 4294967295 [\#28](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/28) ([hoanhan101](https://github.com/hoanhan101))

## [v0.3.1](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/tree/v0.3.1) (2020-07-30)

[Full Changelog](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/compare/v0.3.0...v0.3.1)

## [v0.3.0](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/tree/v0.3.0) (2020-07-21)

[Full Changelog](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/compare/v0.2.1...v0.3.0)

**Fixed bugs:**

- VCID modeling problem [\#23](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/23)

**Closed issues:**

- Add `Deleted` status [\#26](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/26)

**Merged pull requests:**

- Run makemigrations in Django and produce a migration file locally [\#29](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/29) ([hoanhan101](https://github.com/hoanhan101))
- Update status to better reflect the provisioning process [\#27](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/27) ([hoanhan101](https://github.com/hoanhan101))
- Include docs in source distribution [\#25](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/25) ([hoanhan101](https://github.com/hoanhan101))

## [v0.2.1](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/tree/v0.2.1) (2020-07-07)

[Full Changelog](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/compare/v0.2.0...v0.2.1)

**Closed issues:**

- Breaks Swagger API [\#22](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/22)

**Merged pull requests:**

- Add command for creating and pushing a tag with the current version [\#21](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/21) ([hoanhan101](https://github.com/hoanhan101))

## [v0.2.0](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/tree/v0.2.0) (2020-06-18)

[Full Changelog](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/compare/e795f6529d5e6f76c1d541f0bfae8c650f0cc7a7...v0.2.0)

**Closed issues:**

- Plugin netbox-virtual-circuit-plugin does not provide a 'config' variable. [\#8](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/issues/8)

**Merged pull requests:**

- Flesh out UI view [\#20](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/20) ([hoanhan101](https://github.com/hoanhan101))
- Check for existing Virtual-Circuit-to-VLAN connection before creating one [\#19](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/19) ([hoanhan101](https://github.com/hoanhan101))
- Expand `vlans` field inside a virtual circuit object response [\#15](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/15) ([hoanhan101](https://github.com/hoanhan101))
- Add unit tests [\#14](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/14) ([hoanhan101](https://github.com/hoanhan101))
- Setup the local development environment with docker-compose [\#13](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/13) ([hoanhan101](https://github.com/hoanhan101))
- Update README [\#12](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/12) ([ndom91](https://github.com/ndom91))
- Create and assign a Virtual Circuit to multiple VLANs in a single API request [\#11](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/11) ([hoanhan101](https://github.com/hoanhan101))
- Add more details on how-to install and enable the plugin [\#10](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/10) ([hoanhan101](https://github.com/hoanhan101))
- Include netbox\_virtual\_circuit\_plugin in source distributions [\#7](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/7) ([hoanhan101](https://github.com/hoanhan101))
- Include html template files in source distributions [\#6](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/6) ([hoanhan101](https://github.com/hoanhan101))
- Add documentation [\#4](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/4) ([hoanhan101](https://github.com/hoanhan101))
- Create GNU GPLv3 [\#3](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/3) ([hoanhan101](https://github.com/hoanhan101))
- Flesh out REST API endpoints [\#2](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/2) ([hoanhan101](https://github.com/hoanhan101))
- Initial works for supporting Virtual Circuit [\#1](https://github.com/vapor-ware/netbox-virtual-circuit-plugin/pull/1) ([hoanhan101](https://github.com/hoanhan101))



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
