# zhidd (zabbix hp ipmi disks discovery )
# by Dmitry Lavrukhin
# date 11.11.2019
This is simple Template to discover Hard Disk Drives on HP servers in Zabbix monitoring system by ipmi interface trough iLO
This is useful if you have many HP servers with different count of disk drives. In this case you can use my HP servers IPMI templates with excluded HDD sensors. Just Attach Two templates: One for Server Hardware, and one for Disk drives.
My HP IPMI Templates with no-HDD option located here: 
https://share.zabbix.com/owner/lawdt

to use this Template you must do this steps:
1. configure zabbix server with ipmi support end enable ipmi pollers (see zabbix documentation)
2. Correcly configure ipmi interface on nodes in zabbix web interface (also see zabbix documentation)
3. install ipmitool on zabbix server
4. install python on zabbix server
5. install python modules: argparse,sys,subprocess,re,json (see python documentation)
5. copy script to externalscripts directory on zabbix server (see ExternalScripts parameter in zabbix_server.conf)
6. Import Template to zabbix
7. Add templates to nodes
8. Define macroses {$ILO_IP}, {$ILO_USER}, {$ILO_PASSWORD} on node or template level.
9. Check zabbix server logs if something wrong on debug level 4.
