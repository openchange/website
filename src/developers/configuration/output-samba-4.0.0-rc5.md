# Output: Starting OpenChange with Samba 4.0.0-rc5 server #

The listing below shows a sample output of `samba 4.0.0 rc5` release
server starting with OpenChange.

    0.     $ sudo PYTHONPATH=$PYTHONPATH /usr/local/samba/sbin/samba -d3 -i -M single
    1.     lpcfg_load: refreshing parameters from /usr/local/samba/etc/smb.conf
    2.     params.c:pm_process() - Processing configuration file "/usr/local/samba/etc/smb.conf"
    3.     samba version 4.0.0rc5 started.
    4.     Copyright Andrew Tridgell and the Samba Team 1992-2012
    5.     GENSEC backend 'gssapi_spnego' registered
    6.     GENSEC backend 'gssapi_krb5' registered
    7.     GENSEC backend 'gssapi_krb5_sasl' registered
    8.     GENSEC backend 'schannel' registered
    9.     GENSEC backend 'spnego' registered
    10.    GENSEC backend 'ntlmssp' registered
    11.    GENSEC backend 'krb5' registered
    12.    GENSEC backend 'fake_gssapi_krb5' registered
    13.    NTPTR backend 'simple_ldb'
    14.    NTVFS backend 'default' for type 1 registered
    15.    NTVFS backend 'posix' for type 1 registered
    16.    NTVFS backend 'unixuid' for type 1 registered
    17.    NTVFS backend 'unixuid' for type 3 registered
    18.    NTVFS backend 'unixuid' for type 2 registered
    19.    NTVFS backend 'cifs' for type 1 registered
    20.    NTVFS backend 'smb2' for type 1 registered
    21.    NTVFS backend 'simple' for type 1 registered
    22.    NTVFS backend 'cifsposix' for type 1 registered
    23.    NTVFS backend 'default' for type 3 registered
    24.    NTVFS backend 'default' for type 2 registered
    25.    NTVFS backend 'nbench' for type 1 registered
    26.    PROCESS_MODEL 'single' registered
    27.    PROCESS_MODEL 'standard' registered
    28.    PROCESS_MODEL 'prefork' registered
    29.    PROCESS_MODEL 'onefork' registered
    30.    AUTH backend 'sam' registered
    31.    AUTH backend 'sam_ignoredomain' registered
    32.    AUTH backend 'anonymous' registered
    33.    AUTH backend 'winbind' registered
    34.    AUTH backend 'winbind_wbclient' registered
    35.    AUTH backend 'name_to_ntstatus' registered
    36.    AUTH backend 'unix' registered
    37.    SHARE backend [classic] registered.
    38.    SHARE backend [ldb] registered.
    39.    ldb_wrap open of privilege.ldb
    40.    samba: using 'single' process model
    41.    DCERPC endpoint server 'rpcecho' registered
    42.    DCERPC endpoint server 'epmapper' registered
    43.    DCERPC endpoint server 'remote' registered
    44.    DCERPC endpoint server 'srvsvc' registered
    45.    DCERPC endpoint server 'wkssvc' registered
    46.    DCERPC endpoint server 'unixinfo' registered
    47.    DCERPC endpoint server 'samr' registered
    48.    DCERPC endpoint server 'winreg' registered
    49.    DCERPC endpoint server 'netlogon' registered
    50.    DCERPC endpoint server 'dssetup' registered
    51.    DCERPC endpoint server 'lsarpc' registered
    52.    DCERPC endpoint server 'backupkey' registered
    53.    DCERPC endpoint server 'spoolss' registered
    54.    DCERPC endpoint server 'drsuapi' registered
    55.    DCERPC endpoint server 'browser' registered
    56.    DCERPC endpoint server 'eventlog6' registered
    57.    DCERPC endpoint server 'dnsserver' registered
    58.    DCERPC endpoint server 'exchange_emsmdb' registered
    59.    DCERPC endpoint server 'exchange_nsp' registered
    60.    DCERPC endpoint server 'exchange_ds_rfr' registered
    61.    DCERPC endpoint server 'mapiproxy' registered
    62.    MAPIPROXY module 'downgrade' registered
    63.    MAPIPROXY module 'cache' registered
    64.    MAPIPROXY module 'pack' registered
    65.    MAPIPROXY module 'dummy' registered
    66.    MAPIPROXY server 'exchange_ds_rfr' registered
    67.    MAPIPROXY server 'exchange_nsp' registered
    68.    MAPIPROXY server 'exchange_emsmdb' registered
    69.    MAPIPROXY server mode enabled
    70.    MAPIPROXY proxy mode disabled
    71.    mapiproxy_server_load 'exchange_nsp' (OpenChange NSPI server)
    72.    dcesrv_exchange_nsp_init
    73.    mapiproxy_server_load 'exchange_emsmdb' (OpenChange EMSMDB server)
    74.    mapiproxy_server_load 'exchange_ds_rfr' (OpenChange RFR server)
    75.    dreplsrv_partition[CN=Configuration,DC=oc,DC=local] loaded
    76.    dreplsrv_partition[CN=Schema,CN=Configuration,DC=oc,DC=local] loaded
    77.    dreplsrv_partition[DC=oc,DC=local] loaded
    78.    dreplsrv_partition[DC=DomainDnsZones,DC=oc,DC=local] loaded
    79.    dreplsrv_partition[DC=ForestDnsZones,DC=oc,DC=local] loaded
    80.    ldb_wrap open of secrets.ldb
    81.    ldb_wrap open of idmap.ldb
    82.    kccsrv_partition[DC=oc,DC=local] loaded
    83.    kccsrv_partition[CN=Configuration,DC=oc,DC=local] loaded
    84.    kccsrv_partition[CN=Schema,CN=Configuration,DC=oc,DC=local] loaded
    85.    kccsrv_partition[DC=DomainDnsZones,DC=oc,DC=local] loaded
    86.    kccsrv_partition[DC=ForestDnsZones,DC=oc,DC=local] loaded
    87.    Calling DNS name update script
    88.    Calling SPN name update script
    89.    /usr/local/samba/sbin/smbd: smbd version 4.0.0rc5 started.
    90.    /usr/local/samba/sbin/smbd: Copyright Andrew Tridgell and the Samba Team 1992-2012
    91.    /usr/local/samba/sbin/smbd: standard input is not a socket, assuming -D option
    92.    Terminating connection - 'wbsrv_call_loop: tstream_read_pdu_blob_recv() - NT_STATUS_CONNECTION_DISCONNECTED'
    93.    single_terminate: reason[wbsrv_call_loop: tstream_read_pdu_blob_recv() - NT_STATUS_CONNECTION_DISCONNECTED]
    94.    /usr/local/samba/sbin/smbd: Unable to open printcap file /etc/printcap for read!
    95.    Child /usr/local/samba/sbin/samba_spnupdate exited with status 0 - Success
    96.    Completed SPN update check OK
