# Output: Setting Profile with OpenChange server #

The listing below shows sample server side output of OpenChange user
lookup as performed using `mapiprofile` utility for JohnDoe user.

    0.     Registered PRECOG<00> with 192.168.102.48 on interface 192.168.102.255
    1.     Registered PRECOG<03> with 192.168.102.48 on interface 192.168.102.255
    2.     Registered PRECOG<20> with 192.168.102.48 on interface 192.168.102.255
    3.     Registered OC<1b> with 192.168.102.48 on interface 192.168.102.255
    4.     Registered OC<1c> with 192.168.102.48 on interface 192.168.102.255
    5.     Registered OC<00> with 192.168.102.48 on interface 192.168.102.255
    6.     Terminating connection - 'NT_STATUS_CONNECTION_DISCONNECTED'
    7.     single_terminate: reason[NT_STATUS_CONNECTION_DISCONNECTED]
    8.     Got NTLMSSP neg_flags=0x60088205
    9.     Got user=[JohnDoe] domain=[OC] workstation=[precog] len1=24 len2=126
    10.    auth_check_password_send: Checking password for unmapped user [OC]\[JohnDoe]@[precog]
    11.    auth_check_password_send: mapped user is: [OC]\[JohnDoe]@[precog]
    12.    NTLMSSP Sign/Seal - Initialising with flags:
    13.    Got NTLMSSP neg_flags=0x60088205
    14.         RfrGetNewDSA: struct RfrGetNewDSA
    15.            in: struct RfrGetNewDSA
    16.                ulFlags                  : 0x00000000 (0)
    17.                pUserDN                  : *
    18.                    pUserDN                  : ''
    19.                ppszUnused               : NULL
    20.                ppszServer               : *
    21.                    ppszServer               : NULL
    22.         RfrGetNewDSA: struct RfrGetNewDSA
    23.            out: struct RfrGetNewDSA
    24.                ppszUnused               : NULL
    25.                ppszServer               : *
    26.                    ppszServer               : *
    27.                        ppszServer               : 'precog.oc.local'
    28.                result                   : MAPI_E_SUCCESS (0x0)
    29.    Terminating connection - 'NT_STATUS_CONNECTION_DISCONNECTED'
    30.    single_terminate: reason[NT_STATUS_CONNECTION_DISCONNECTED]
    31.    dcesrv_exchange_nsp_unbind
    32.    dcesrv_exchange_emsmdb_unbind
    33.    Terminating connection - 'NT_STATUS_CONNECTION_DISCONNECTED'
    34.    single_terminate: reason[NT_STATUS_CONNECTION_DISCONNECTED]
    35.    Kerberos: AS-REQ JohnDoe@OC.LOCAL from ipv4:192.168.102.48:56480 for krbtgt/OC.LOCAL@OC.LOCAL
    36.    Kerberos: No preauth found, returning PREAUTH-REQUIRED -- JohnDoe@OC.LOCAL
    37.    Kerberos: AS-REQ JohnDoe@OC.LOCAL from ipv4:192.168.102.48:49238 for krbtgt/OC.LOCAL@OC.LOCAL
    38.    Kerberos: Client sent patypes: encrypted-timestamp
    39.    Kerberos: Looking for PKINIT pa-data -- JohnDoe@OC.LOCAL
    40.    Kerberos: Looking for ENC-TS pa-data -- JohnDoe@OC.LOCAL
    41.    Kerberos: ENC-TS Pre-authentication succeeded -- JohnDoe@OC.LOCAL using arcfour-hmac-md5
    42.    Kerberos: AS-REQ authtime: 2012-11-22T18:35:59 starttime: unset endtime: 2012-11-23T04:35:59 renew till: unset
    43.    Kerberos: Client supported enctypes: aes256-cts-hmac-sha1-96, aes128-cts-hmac-sha1-96, des3-cbc-sha1, des3-cbc-md5, arcfour-hmac-md5, using arcfour-hmac-md5/arcfour-hmac-md5
    44.    Kerberos: Requested flags: forwardable
    45.    Kerberos: TGS-REQ JohnDoe@OC.LOCAL from ipv4:192.168.102.48:48661 for exchangeAB/PRECOG.OC.LOCAL@OC.LOCAL [canonicalize]
    46.    Kerberos: Searching referral for PRECOG.OC.LOCAL
    47.    Kerberos: Server not found in database: exchangeAB/PRECOG.OC.LOCAL@OC.LOCAL: no such entry found in hdb
    48.    Kerberos: Failed building TGS-REP to ipv4:192.168.102.48:48661
    49.    Kerberos: TGS-REQ JohnDoe@OC.LOCAL from ipv4:192.168.102.48:58621 for exchangeAB/PRECOG.OC.LOCAL@OC.LOCAL
    50.    Kerberos: Server not found in database: exchangeAB/PRECOG.OC.LOCAL@OC.LOCAL: no such entry found in hdb
    51.    Kerberos: Failed building TGS-REP to ipv4:192.168.102.48:58621
    52.    Kerberos: TGS-REQ JohnDoe@OC.LOCAL from ipv4:192.168.102.48:42779 for exchangeAB/PRECOG.OC.LOCAL@OC.LOCAL [canonicalize]
    53.    Kerberos: Searching referral for PRECOG.OC.LOCAL
    54.    Kerberos: Server not found in database: exchangeAB/PRECOG.OC.LOCAL@OC.LOCAL: no such entry found in hdb
    55.    Kerberos: Failed building TGS-REP to ipv4:192.168.102.48:42779
    56.    Kerberos: TGS-REQ JohnDoe@OC.LOCAL from ipv4:192.168.102.48:32834 for exchangeAB/PRECOG.OC.LOCAL@OC.LOCAL
    57.    Kerberos: Server not found in database: exchangeAB/PRECOG.OC.LOCAL@OC.LOCAL: no such entry found in hdb
    58.    Kerberos: Failed building TGS-REP to ipv4:192.168.102.48:32834
    59.    Got NTLMSSP neg_flags=0x60088205
    60.    Got user=[JohnDoe] domain=[OC] workstation=[precog] len1=24 len2=126
    61.    auth_check_password_send: Checking password for unmapped user [OC]\[JohnDoe]@[precog]
    62.    auth_check_password_send: mapped user is: [OC]\[JohnDoe]@[precog]
    63.    NTLMSSP Sign/Seal - Initialising with flags:
    64.    Got NTLMSSP neg_flags=0x60088205
    65.         NspiBind: struct NspiBind
    66.            in: struct NspiBind
    67.                dwFlags                  : 0x00000000 (0)
    68.                       0: fAnonymousLogin          
    69.                pStat                    : *
    70.                    pStat: struct STAT
    71.                        SortType                 : SortTypeDisplayName (0)
    72.                        ContainerID              : 0x00000000 (0)
    73.                        CurrentRec               : MID_BEGINNING_OF_TABLE (0)
    74.                        Delta                    : 0
    75.                        NumPos                   : 0x00000000 (0)
    76.                        TotalRecs                : 0x00000000 (0)
    77.                        CodePage                 : 0x000004e4 (1252)
    78.                        TemplateLocale           : 0x00000409 (1033)
    79.                        SortLocale               : 0x00000409 (1033)
    80.                mapiuid                  : *
    81.                    mapiuid                  : 00000000-0000-0000-0000-000000000000
    82.    dcesrv_exchange_nsp_dispatch
    83.    Creating new session
    84.         NspiBind: struct NspiBind
    85.            out: struct NspiBind
    86.                mapiuid                  : *
    87.                    mapiuid                  : 118f90d9-86be-46dd-845b-e1912c828b7b
    88.                handle                   : *
    89.                    handle: struct policy_handle
    90.                        handle_type              : 0x00000000 (0)
    91.                        uuid                     : f734441b-1f31-4ee8-8be4-4143bc88130a
    92.                result                   : MAPI_E_SUCCESS (0x0)
    93.         NspiGetSpecialTable: struct NspiGetSpecialTable
    94.            in: struct NspiGetSpecialTable
    95.                handle                   : *
    96.                    handle: struct policy_handle
    97.                        handle_type              : 0x00000000 (0)
    98.                        uuid                     : f734441b-1f31-4ee8-8be4-4143bc88130a
    99.                dwFlags                  : 0x00000000 (0)
    100.                      0: NspiAddressCreationTemplates
    101.                      0: NspiUnicodeStrings       
    102.               pStat                    : *
    103.                   pStat: struct STAT
    104.                       SortType                 : SortTypeDisplayName (0)
    105.                       ContainerID              : 0x00000000 (0)
    106.                       CurrentRec               : MID_BEGINNING_OF_TABLE (0)
    107.                       Delta                    : 0
    108.                       NumPos                   : 0x00000000 (0)
    109.                       TotalRecs                : 0x00000000 (0)
    110.                       CodePage                 : 0x000004e4 (1252)
    111.                       TemplateLocale           : 0x00000409 (1033)
    112.                       SortLocale               : 0x00000409 (1033)
    113.               lpVersion                : *
    114.                   lpVersion                : 0x00000000 (0)
    115.   dcesrv_exchange_nsp_dispatch
    116.   exchange_nsp: NspiGetSpecialTable (0xC)
    117.   Hierarchy Table requested
    118.        NspiGetSpecialTable: struct NspiGetSpecialTable
    119.           out: struct NspiGetSpecialTable
    120.               lpVersion                : *
    121.                   lpVersion                : 0x00000001 (1)
    122.               ppRows                   : *
    123.                   ppRows                   : *
    124.                       ppRows: struct PropertyRowSet_r
    125.                           cRows                    : 0x00000006 (6)
    126.                           aRow: ARRAY(6)
    127.                               aRow: struct PropertyRow_r
    128.                                   Reserved                 : 0x00000000 (0)
    129.                                   cValues                  : 0x00000006 (6)
    130.                                   lpProps                  : *
    131.                                       lpProps: ARRAY(6)
    132.                                           lpProps: struct PropertyValue_r
    133.                                               ulPropTag                : PidTagEntryId (0xFFF0102)
    134.                                               dwAlignPad               : 0x00000000 (0)
    135.                                               value                    : union PROP_VAL_UNION(case 258)
    136.                                               bin                      : Binary_r cb=30
    137.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    138.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 00        +/...... ..../.
    139.                                           lpProps: struct PropertyValue_r
    140.                                               ulPropTag                : PidTagContainerFlags (0x36000003)
    141.                                               dwAlignPad               : 0x00000000 (0)
    142.                                               value                    : union PROP_VAL_UNION(case 3)
    143.                                               l                        : 0x00000009 (9)
    144.                                           lpProps: struct PropertyValue_r
    145.                                               ulPropTag                : PidTagDepth (0x30050003)
    146.                                               dwAlignPad               : 0x00000000 (0)
    147.                                               value                    : union PROP_VAL_UNION(case 3)
    148.                                               l                        : 0x00000000 (0)
    149.                                           lpProps: struct PropertyValue_r
    150.                                               ulPropTag                : PidTagAddressBookContainerId (0xFFFD0003)
    151.                                               dwAlignPad               : 0x00000000 (0)
    152.                                               value                    : union PROP_VAL_UNION(case 3)
    153.                                               l                        : 0x00000000 (0)
    154.                                           lpProps: struct PropertyValue_r
    155.                                               ulPropTag                : PidTagDisplayName_Error (0x3001000A)
    156.                                               dwAlignPad               : 0x00000000 (0)
    157.                                               value                    : union PROP_VAL_UNION(case 10)
    158.                                               err                      : MAPI_E_SUCCESS (0x0)
    159.                                           lpProps: struct PropertyValue_r
    160.                                               ulPropTag                : PidTagAddressBookIsMaster (0xFFFB000B)
    161.                                               dwAlignPad               : 0x00000000 (0)
    162.                                               value                    : union PROP_VAL_UNION(case 11)
    163.                                               b                        : 0x00 (0)
    164.                               aRow: struct PropertyRow_r
    165.                                   Reserved                 : 0x00000000 (0)
    166.                                   cValues                  : 0x00000006 (6)
    167.                                   lpProps                  : *
    168.                                       lpProps: ARRAY(6)
    169.                                           lpProps: struct PropertyValue_r
    170.                                               ulPropTag                : PidTagEntryId (0xFFF0102)
    171.                                               dwAlignPad               : 0x00000000 (0)
    172.                                               value                    : union PROP_VAL_UNION(case 258)
    173.                                               bin                      : Binary_r cb=67
    174.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    175.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    176.   [0020] 64 3D 30 33 41 41 39 37   42 42 45 41 41 45 34 34   d=03AA97 BBEAAE44
    177.   [0030] 33 39 38 46 37 36 37 30   42 31 41 31 31 44 39 36   398F7670 B1A11D96
    178.   [0040] 36 42 00                                          6B. 
    179.                                           lpProps: struct PropertyValue_r
    180.                                               ulPropTag                : PidTagContainerFlags (0x36000003)
    181.                                               dwAlignPad               : 0x00000000 (0)
    182.                                               value                    : union PROP_VAL_UNION(case 3)
    183.                                               l                        : 0x00000009 (9)
    184.                                           lpProps: struct PropertyValue_r
    185.                                               ulPropTag                : PidTagDepth (0x30050003)
    186.                                               dwAlignPad               : 0x00000000 (0)
    187.                                               value                    : union PROP_VAL_UNION(case 3)
    188.                                               l                        : 0x00000000 (0)
    189.                                           lpProps: struct PropertyValue_r
    190.                                               ulPropTag                : PidTagAddressBookContainerId (0xFFFD0003)
    191.                                               dwAlignPad               : 0x00000000 (0)
    192.                                               value                    : union PROP_VAL_UNION(case 3)
    193.                                               l                        : 0x00001b29 (6953)
    194.                                           lpProps: struct PropertyValue_r
    195.                                               ulPropTag                : PidTagDisplayName_string8 (0x3001001E)
    196.                                               dwAlignPad               : 0x00000000 (0)
    197.                                               value                    : union PROP_VAL_UNION(case 30)
    198.                                               lpszA                    : *
    199.                                                   lpszA                    : 'All Address Lists'
    200.                                           lpProps: struct PropertyValue_r
    201.                                               ulPropTag                : PidTagAddressBookIsMaster (0xFFFB000B)
    202.                                               dwAlignPad               : 0x00000000 (0)
    203.                                               value                    : union PROP_VAL_UNION(case 11)
    204.                                               b                        : 0x00 (0)
    205.                               aRow: struct PropertyRow_r
    206.                                   Reserved                 : 0x00000000 (0)
    207.                                   cValues                  : 0x00000007 (7)
    208.                                   lpProps                  : *
    209.                                       lpProps: ARRAY(7)
    210.                                           lpProps: struct PropertyValue_r
    211.                                               ulPropTag                : PidTagEntryId (0xFFF0102)
    212.                                               dwAlignPad               : 0x00000000 (0)
    213.                                               value                    : union PROP_VAL_UNION(case 258)
    214.                                               bin                      : Binary_r cb=67
    215.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    216.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    217.   [0020] 64 3D 41 30 44 45 44 43   32 32 37 34 42 36 34 32   d=A0DEDC 2274B642
    218.   [0030] 44 38 42 39 43 36 37 42   44 41 41 46 44 43 30 37   D8B9C67B DAAFDC07
    219.   [0040] 45 45 00                                          EE. 
    220.                                           lpProps: struct PropertyValue_r
    221.                                               ulPropTag                : PidTagContainerFlags (0x36000003)
    222.                                               dwAlignPad               : 0x00000000 (0)
    223.                                               value                    : union PROP_VAL_UNION(case 3)
    224.                                               l                        : 0x0000000b (11)
    225.                                           lpProps: struct PropertyValue_r
    226.                                               ulPropTag                : PidTagDepth (0x30050003)
    227.                                               dwAlignPad               : 0x00000000 (0)
    228.                                               value                    : union PROP_VAL_UNION(case 3)
    229.                                               l                        : 0x00000001 (1)
    230.                                           lpProps: struct PropertyValue_r
    231.                                               ulPropTag                : PidTagAddressBookContainerId (0xFFFD0003)
    232.                                               dwAlignPad               : 0x00000000 (0)
    233.                                               value                    : union PROP_VAL_UNION(case 3)
    234.                                               l                        : 0x00001b2a (6954)
    235.                                           lpProps: struct PropertyValue_r
    236.                                               ulPropTag                : PidTagDisplayName_string8 (0x3001001E)
    237.                                               dwAlignPad               : 0x00000000 (0)
    238.                                               value                    : union PROP_VAL_UNION(case 30)
    239.                                               lpszA                    : *
    240.                                                   lpszA                    : 'All Contacts'
    241.                                           lpProps: struct PropertyValue_r
    242.                                               ulPropTag                : PidTagAddressBookIsMaster (0xFFFB000B)
    243.                                               dwAlignPad               : 0x00000000 (0)
    244.                                               value                    : union PROP_VAL_UNION(case 11)
    245.                                               b                        : 0x00 (0)
    246.                                           lpProps: struct PropertyValue_r
    247.                                               ulPropTag                : PidTagAddressBookParentEntryId (0xFFFC0102)
    248.                                               dwAlignPad               : 0x00000000 (0)
    249.                                               value                    : union PROP_VAL_UNION(case 258)
    250.                                               bin                      : Binary_r cb=67
    251.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    252.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    253.   [0020] 64 3D 30 33 41 41 39 37   42 42 45 41 41 45 34 34   d=03AA97 BBEAAE44
    254.   [0030] 33 39 38 46 37 36 37 30   42 31 41 31 31 44 39 36   398F7670 B1A11D96
    255.   [0040] 36 42 00                                          6B. 
    256.                               aRow: struct PropertyRow_r
    257.                                   Reserved                 : 0x00000000 (0)
    258.                                   cValues                  : 0x00000007 (7)
    259.                                   lpProps                  : *
    260.                                       lpProps: ARRAY(7)
    261.                                           lpProps: struct PropertyValue_r
    262.                                               ulPropTag                : PidTagEntryId (0xFFF0102)
    263.                                               dwAlignPad               : 0x00000000 (0)
    264.                                               value                    : union PROP_VAL_UNION(case 258)
    265.                                               bin                      : Binary_r cb=67
    266.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    267.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    268.   [0020] 64 3D 38 32 30 35 42 33   35 35 32 44 44 31 34 41   d=8205B3 552DD14A
    269.   [0030] 39 36 42 41 43 41 44 43   31 36 30 44 45 44 30 41   96BACADC 160DED0A
    270.   [0040] 31 38 00                                          18. 
    271.                                           lpProps: struct PropertyValue_r
    272.                                               ulPropTag                : PidTagContainerFlags (0x36000003)
    273.                                               dwAlignPad               : 0x00000000 (0)
    274.                                               value                    : union PROP_VAL_UNION(case 3)
    275.                                               l                        : 0x0000000b (11)
    276.                                           lpProps: struct PropertyValue_r
    277.                                               ulPropTag                : PidTagDepth (0x30050003)
    278.                                               dwAlignPad               : 0x00000000 (0)
    279.                                               value                    : union PROP_VAL_UNION(case 3)
    280.                                               l                        : 0x00000001 (1)
    281.                                           lpProps: struct PropertyValue_r
    282.                                               ulPropTag                : PidTagAddressBookContainerId (0xFFFD0003)
    283.                                               dwAlignPad               : 0x00000000 (0)
    284.                                               value                    : union PROP_VAL_UNION(case 3)
    285.                                               l                        : 0x00001b2b (6955)
    286.                                           lpProps: struct PropertyValue_r
    287.                                               ulPropTag                : PidTagDisplayName_string8 (0x3001001E)
    288.                                               dwAlignPad               : 0x00000000 (0)
    289.                                               value                    : union PROP_VAL_UNION(case 30)
    290.                                               lpszA                    : *
    291.                                                   lpszA                    : 'All Groups'
    292.                                           lpProps: struct PropertyValue_r
    293.                                               ulPropTag                : PidTagAddressBookIsMaster (0xFFFB000B)
    294.                                               dwAlignPad               : 0x00000000 (0)
    295.                                               value                    : union PROP_VAL_UNION(case 11)
    296.                                               b                        : 0x00 (0)
    297.                                           lpProps: struct PropertyValue_r
    298.                                               ulPropTag                : PidTagAddressBookParentEntryId (0xFFFC0102)
    299.                                               dwAlignPad               : 0x00000000 (0)
    300.                                               value                    : union PROP_VAL_UNION(case 258)
    301.                                               bin                      : Binary_r cb=67
    302.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    303.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    304.   [0020] 64 3D 30 33 41 41 39 37   42 42 45 41 41 45 34 34   d=03AA97 BBEAAE44
    305.   [0030] 33 39 38 46 37 36 37 30   42 31 41 31 31 44 39 36   398F7670 B1A11D96
    306.   [0040] 36 42 00                                          6B. 
    307.                               aRow: struct PropertyRow_r
    308.                                   Reserved                 : 0x00000000 (0)
    309.                                   cValues                  : 0x00000007 (7)
    310.                                   lpProps                  : *
    311.                                       lpProps: ARRAY(7)
    312.                                           lpProps: struct PropertyValue_r
    313.                                               ulPropTag                : PidTagEntryId (0xFFF0102)
    314.                                               dwAlignPad               : 0x00000000 (0)
    315.                                               value                    : union PROP_VAL_UNION(case 258)
    316.                                               bin                      : Binary_r cb=67
    317.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    318.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    319.   [0020] 64 3D 44 39 45 37 44 36   34 31 39 34 46 42 34 32   d=D9E7D6 4194FB42
    320.   [0030] 44 45 39 30 38 35 34 43   43 39 35 35 30 42 33 41   DE90854C C9550B3A
    321.   [0040] 42 45 00                                          BE. 
    322.                                           lpProps: struct PropertyValue_r
    323.                                               ulPropTag                : PidTagContainerFlags (0x36000003)
    324.                                               dwAlignPad               : 0x00000000 (0)
    325.                                               value                    : union PROP_VAL_UNION(case 3)
    326.                                               l                        : 0x0000000b (11)
    327.                                           lpProps: struct PropertyValue_r
    328.                                               ulPropTag                : PidTagDepth (0x30050003)
    329.                                               dwAlignPad               : 0x00000000 (0)
    330.                                               value                    : union PROP_VAL_UNION(case 3)
    331.                                               l                        : 0x00000001 (1)
    332.                                           lpProps: struct PropertyValue_r
    333.                                               ulPropTag                : PidTagAddressBookContainerId (0xFFFD0003)
    334.                                               dwAlignPad               : 0x00000000 (0)
    335.                                               value                    : union PROP_VAL_UNION(case 3)
    336.                                               l                        : 0x00001b2c (6956)
    337.                                           lpProps: struct PropertyValue_r
    338.                                               ulPropTag                : PidTagDisplayName_string8 (0x3001001E)
    339.                                               dwAlignPad               : 0x00000000 (0)
    340.                                               value                    : union PROP_VAL_UNION(case 30)
    341.                                               lpszA                    : *
    342.                                                   lpszA                    : 'All Users'
    343.                                           lpProps: struct PropertyValue_r
    344.                                               ulPropTag                : PidTagAddressBookIsMaster (0xFFFB000B)
    345.                                               dwAlignPad               : 0x00000000 (0)
    346.                                               value                    : union PROP_VAL_UNION(case 11)
    347.                                               b                        : 0x00 (0)
    348.                                           lpProps: struct PropertyValue_r
    349.                                               ulPropTag                : PidTagAddressBookParentEntryId (0xFFFC0102)
    350.                                               dwAlignPad               : 0x00000000 (0)
    351.                                               value                    : union PROP_VAL_UNION(case 258)
    352.                                               bin                      : Binary_r cb=67
    353.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    354.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    355.   [0020] 64 3D 30 33 41 41 39 37   42 42 45 41 41 45 34 34   d=03AA97 BBEAAE44
    356.   [0030] 33 39 38 46 37 36 37 30   42 31 41 31 31 44 39 36   398F7670 B1A11D96
    357.   [0040] 36 42 00                                          6B. 
    358.                               aRow: struct PropertyRow_r
    359.                                   Reserved                 : 0x00000000 (0)
    360.                                   cValues                  : 0x00000007 (7)
    361.                                   lpProps                  : *
    362.                                       lpProps: ARRAY(7)
    363.                                           lpProps: struct PropertyValue_r
    364.                                               ulPropTag                : PidTagEntryId (0xFFF0102)
    365.                                               dwAlignPad               : 0x00000000 (0)
    366.                                               value                    : union PROP_VAL_UNION(case 258)
    367.                                               bin                      : Binary_r cb=67
    368.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    369.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    370.   [0020] 64 3D 37 46 46 46 39 41   44 42 45 39 38 34 34 31   d=7FFF9A DBE98441
    371.   [0030] 38 39 42 44 45 44 45 41   39 31 37 43 46 42 33 36   89BDEDEA 917CFB36
    372.   [0040] 43 32 00                                          C2. 
    373.                                           lpProps: struct PropertyValue_r
    374.                                               ulPropTag                : PidTagContainerFlags (0x36000003)
    375.                                               dwAlignPad               : 0x00000000 (0)
    376.                                               value                    : union PROP_VAL_UNION(case 3)
    377.                                               l                        : 0x0000000b (11)
    378.                                           lpProps: struct PropertyValue_r
    379.                                               ulPropTag                : PidTagDepth (0x30050003)
    380.                                               dwAlignPad               : 0x00000000 (0)
    381.                                               value                    : union PROP_VAL_UNION(case 3)
    382.                                               l                        : 0x00000001 (1)
    383.                                           lpProps: struct PropertyValue_r
    384.                                               ulPropTag                : PidTagAddressBookContainerId (0xFFFD0003)
    385.                                               dwAlignPad               : 0x00000000 (0)
    386.                                               value                    : union PROP_VAL_UNION(case 3)
    387.                                               l                        : 0x00001b2d (6957)
    388.                                           lpProps: struct PropertyValue_r
    389.                                               ulPropTag                : PidTagDisplayName_string8 (0x3001001E)
    390.                                               dwAlignPad               : 0x00000000 (0)
    391.                                               value                    : union PROP_VAL_UNION(case 30)
    392.                                               lpszA                    : *
    393.                                                   lpszA                    : 'Public Folders'
    394.                                           lpProps: struct PropertyValue_r
    395.                                               ulPropTag                : PidTagAddressBookIsMaster (0xFFFB000B)
    396.                                               dwAlignPad               : 0x00000000 (0)
    397.                                               value                    : union PROP_VAL_UNION(case 11)
    398.                                               b                        : 0x00 (0)
    399.                                           lpProps: struct PropertyValue_r
    400.                                               ulPropTag                : PidTagAddressBookParentEntryId (0xFFFC0102)
    401.                                               dwAlignPad               : 0x00000000 (0)
    402.                                               value                    : union PROP_VAL_UNION(case 258)
    403.                                               bin                      : Binary_r cb=67
    404.   [0000] 00 00 00 00 DC A7 40 C8   C0 42 10 1A B4 B9 08 00   ......@. .B......
    405.   [0010] 2B 2F E1 82 01 00 00 00   00 01 00 00 2F 67 75 69   +/...... ..../gui
    406.   [0020] 64 3D 30 33 41 41 39 37   42 42 45 41 41 45 34 34   d=03AA97 BBEAAE44
    407.   [0030] 33 39 38 46 37 36 37 30   42 31 41 31 31 44 39 36   398F7670 B1A11D96
    408.   [0040] 36 42 00                                          6B. 
    409.               result                   : MAPI_E_SUCCESS (0x0)
    410.        NspiGetMatches: struct NspiGetMatches
    411.           in: struct NspiGetMatches
    412.               handle                   : *
    413.                   handle: struct policy_handle
    414.                       handle_type              : 0x00000000 (0)
    415.                       uuid                     : f734441b-1f31-4ee8-8be4-4143bc88130a
    416.               Reserved                 : 0x00000000 (0)
    417.               pStat                    : *
    418.                   pStat: struct STAT
    419.                       SortType                 : SortTypeDisplayName (0)
    420.                       ContainerID              : 0x00000000 (0)
    421.                       CurrentRec               : MID_BEGINNING_OF_TABLE (0)
    422.                       Delta                    : 0
    423.                       NumPos                   : 0x00000000 (0)
    424.                       TotalRecs                : 0x00000000 (0)
    425.                       CodePage                 : 0x000004e4 (1252)
    426.                       TemplateLocale           : 0x00000409 (1033)
    427.                       SortLocale               : 0x00000409 (1033)
    428.               pReserved                : NULL
    429.               Reserved2                : 0x00000000 (0)
    430.               Filter                   : *
    431.                   Filter: struct Restriction_r
    432.                       rt                       : RES_PROPERTY (4)
    433.                       res                      : union RestrictionUnion_r(case 4)
    434.                       resProperty: struct PropertyRestriction_r
    435.                           relop                    : 0x00000004 (4)
    436.                           ulPropTag                : PidTagAnr (0x360C001F)
    437.                           lpProp                   : *
    438.                               lpProp: struct PropertyValue_r
    439.                                   ulPropTag                : PidTagAnr (0x360C001F)
    440.                                   dwAlignPad               : 0x00000000 (0)
    441.                                   value                    : union PROP_VAL_UNION(case 31)
    442.                                   lpszW                    : *
    443.                                       lpszW                    : 'JohnDoe'
    444.               lpPropName               : NULL
    445.               ulRequested              : 0x00001388 (5000)
    446.               pPropTags                : *
    447.                   pPropTags: struct SPropTagArray
    448.                       cValues                  : 0x0000000c (12)
    449.                       aulPropTag: ARRAY(12)
    450.                           aulPropTag               : PidTagDisplayName_string8 (0x3001001E)
    451.                           aulPropTag               : PidTagBusinessTelephoneNumber_string8 (0x3A08001E)
    452.                           aulPropTag               : PidTagOfficeLocation_string8 (0x3A19001E)
    453.                           aulPropTag               : PidTagTitle_string8 (0x3A17001E)
    454.                           aulPropTag               : PidTagCompanyName_string8 (0x3A16001E)
    455.                           aulPropTag               : PidTagAccount_string8 (0x3A00001E)
    456.                           aulPropTag               : PidTagAddressType_string8 (0x3002001E)
    457.                           aulPropTag               : PidTagEntryId (0xFFF0102)
    458.                           aulPropTag               : PidTagObjectType (0xFFE0003)
    459.                           aulPropTag               : PidTagDisplayType (0x39000003)
    460.                           aulPropTag               : PidTagInstanceKey (0xFF60102)
    461.                           aulPropTag               : PidTagEmailAddress_string8 (0x3003001E)
    462.   dcesrv_exchange_nsp_dispatch
    463.   exchange_nsp: NspiGetMatches (0x5)
    464.        NspiGetMatches: struct NspiGetMatches
    465.           out: struct NspiGetMatches
    466.               pStat                    : *
    467.                   pStat: struct STAT
    468.                       SortType                 : SortTypeDisplayName (0)
    469.                       ContainerID              : 0x00000000 (0)
    470.                       CurrentRec               : MID_BEGINNING_OF_TABLE (0)
    471.                       Delta                    : 0
    472.                       NumPos                   : 0x00000000 (0)
    473.                       TotalRecs                : 0x00000000 (0)
    474.                       CodePage                 : 0x000004e4 (1252)
    475.                       TemplateLocale           : 0x00000409 (1033)
    476.                       SortLocale               : 0x00000409 (1033)
    477.               ppOutMIds                : *
    478.                   ppOutMIds                : *
    479.                       ppOutMIds: struct PropertyTagArray_r
    480.                           cValues                  : 0x00000001 (1)
    481.                           aulPropTag: ARRAY(1)
    482.                               aulPropTag               : 0x00005001 (20481)
    483.               ppRows                   : *
    484.                   ppRows                   : *
    485.                       ppRows: struct PropertyRowSet_r
    486.                           cRows                    : 0x00000001 (1)
    487.                           aRow: ARRAY(1)
    488.                               aRow: struct PropertyRow_r
    489.                                   Reserved                 : 0x00000000 (0)
    490.                                   cValues                  : 0x0000000c (12)
    491.                                   lpProps                  : *
    492.                                       lpProps: ARRAY(12)
    493.                                           lpProps: struct PropertyValue_r
    494.                                               ulPropTag                : PidTagDisplayName_string8 (0x3001001E)
    495.                                               dwAlignPad               : 0x00000000 (0)
    496.                                               value                    : union PROP_VAL_UNION(case 30)
    497.                                               lpszA                    : *
    498.                                                   lpszA                    : 'JohnDoe'
    499.                                           lpProps: struct PropertyValue_r
    500.                                               ulPropTag                : PidTagBusinessTelephoneNumber_Error (0x3A08000A)
    501.                                               dwAlignPad               : 0x00000000 (0)
    502.                                               value                    : union PROP_VAL_UNION(case 10)
    503.                                               err                      : MAPI_E_NOT_FOUND (0x8004010F)
    504.                                           lpProps: struct PropertyValue_r
    505.                                               ulPropTag                : PidTagOfficeLocation_Error (0x3A19000A)
    506.                                               dwAlignPad               : 0x00000000 (0)
    507.                                               value                    : union PROP_VAL_UNION(case 10)
    508.                                               err                      : MAPI_E_NOT_FOUND (0x8004010F)
    509.                                           lpProps: struct PropertyValue_r
    510.                                               ulPropTag                : PidTagTitle_Error (0x3A17000A)
    511.                                               dwAlignPad               : 0x00000000 (0)
    512.                                               value                    : union PROP_VAL_UNION(case 10)
    513.                                               err                      : MAPI_E_NOT_FOUND (0x8004010F)
    514.                                           lpProps: struct PropertyValue_r
    515.                                               ulPropTag                : PidTagCompanyName_Error (0x3A16000A)
    516.                                               dwAlignPad               : 0x00000000 (0)
    517.                                               value                    : union PROP_VAL_UNION(case 10)
    518.                                               err                      : MAPI_E_NOT_FOUND (0x8004010F)
    519.                                           lpProps: struct PropertyValue_r
    520.                                               ulPropTag                : PidTagAccount_string8 (0x3A00001E)
    521.                                               dwAlignPad               : 0x00000000 (0)
    522.                                               value                    : union PROP_VAL_UNION(case 30)
    523.                                               lpszA                    : *
    524.                                                   lpszA                    : 'JohnDoe'
    525.                                           lpProps: struct PropertyValue_r
    526.                                               ulPropTag                : PidTagAddressType_string8 (0x3002001E)
    527.                                               dwAlignPad               : 0x00000000 (0)
    528.                                               value                    : union PROP_VAL_UNION(case 30)
    529.                                               lpszA                    : *
    530.                                                   lpszA                    : 'EX'
    531.                                           lpProps: struct PropertyValue_r
    532.                                               ulPropTag                : PidTagEntryId (0xFFF0102)
    533.                                               dwAlignPad               : 0x00000000 (0)
    534.                                               value                    : union PROP_VAL_UNION(case 258)
    535.                                               bin                      : Binary_r cb=32
    536.   [0000] 87 00 00 00 D9 90 8F 11   BE 86 DD 46 84 5B E1 91   ........ ...F.[..
    537.   [0010] 2C 82 8B 7B 01 00 00 00   00 00 00 00 01 50 00 00   ,..{.... .....P..
    538.                                           lpProps: struct PropertyValue_r
    539.                                               ulPropTag                : PidTagObjectType (0xFFE0003)
    540.                                               dwAlignPad               : 0x00000000 (0)
    541.                                               value                    : union PROP_VAL_UNION(case 3)
    542.                                               l                        : 0x00000006 (6)
    543.                                           lpProps: struct PropertyValue_r
    544.                                               ulPropTag                : PidTagDisplayType (0x39000003)
    545.                                               dwAlignPad               : 0x00000000 (0)
    546.                                               value                    : union PROP_VAL_UNION(case 3)
    547.                                               l                        : 0x00000000 (0)
    548.                                           lpProps: struct PropertyValue_r
    549.                                               ulPropTag                : PidTagInstanceKey (0xFF60102)
    550.                                               dwAlignPad               : 0x00000000 (0)
    551.                                               value                    : union PROP_VAL_UNION(case 258)
    552.                                               bin                      : Binary_r cb=4
    553.   [0000] 01 50 00 00                                       .P.. 
    554.                                           lpProps: struct PropertyValue_r
    555.                                               ulPropTag                : PidTagEmailAddress_string8 (0x3003001E)
    556.                                               dwAlignPad               : 0x00000000 (0)
    557.                                               value                    : union PROP_VAL_UNION(case 30)
    558.                                               lpszA                    : *
    559.                                                   lpszA                    : '/o=First Organization/ou=First Administrative Group/cn=Recipients/cn=JohnDoe'
    560.               result                   : MAPI_E_SUCCESS (0x0)
    561.        NspiQueryRows: struct NspiQueryRows
    562.           in: struct NspiQueryRows
    563.               handle                   : *
    564.                   handle: struct policy_handle
    565.                       handle_type              : 0x00000000 (0)
    566.                       uuid                     : f734441b-1f31-4ee8-8be4-4143bc88130a
    567.               dwFlags                  : 0x00000000 (0)
    568.                      0: fSkipObjects             
    569.                      0: fEphID                   
    570.               pStat                    : *
    571.                   pStat: struct STAT
    572.                       SortType                 : SortTypeDisplayName (0)
    573.                       ContainerID              : 0x00000000 (0)
    574.                       CurrentRec               : UNKNOWN_ENUM_VALUE (20481)
    575.                       Delta                    : 0
    576.                       NumPos                   : 0x00000000 (0)
    577.                       TotalRecs                : 0x00000001 (1)
    578.                       CodePage                 : 0x000004e4 (1252)
    579.                       TemplateLocale           : 0x00000409 (1033)
    580.                       SortLocale               : 0x00000409 (1033)
    581.               dwETableCount            : 0x00000001 (1)
    582.               lpETable                 : *
    583.                   lpETable: ARRAY(1)
    584.                       lpETable                 : 0x00005001 (20481)
    585.               Count                    : 0x00000001 (1)
    586.               pPropTags                : *
    587.                   pPropTags: struct SPropTagArray
    588.                       cValues                  : 0x00000007 (7)
    589.                       aulPropTag: ARRAY(7)
    590.                           aulPropTag               : PidTagDisplayName_string8 (0x3001001E)
    591.                           aulPropTag               : PidTagEmailAddress_string8 (0x3003001E)
    592.                           aulPropTag               : PidTagDisplayType (0x39000003)
    593.                           aulPropTag               : PidTagAddressBookHomeMessageDatabase (0x8006001F)
    594.                           aulPropTag               : PidTagAttachNumber (0xE210003)
    595.                           aulPropTag               : UNKNOWN_ENUM_VALUE (0x6613101E)
    596.                           aulPropTag               : PidTagAddressBookProxyAddresses_string8 (0x800F101E)
    597.   dcesrv_exchange_nsp_dispatch
    598.   exchange_nsp: NspiQueryRows (0x3)
    599.        NspiQueryRows: struct NspiQueryRows
    600.           out: struct NspiQueryRows
    601.               pStat                    : *
    602.                   pStat: struct STAT
    603.                       SortType                 : SortTypeDisplayName (0)
    604.                       ContainerID              : 0x00000000 (0)
    605.                       CurrentRec               : MID_END_OF_TABLE (2)
    606.                       Delta                    : 0
    607.                       NumPos                   : 0x00000000 (0)
    608.                       TotalRecs                : 0x00000001 (1)
    609.                       CodePage                 : 0x000004e4 (1252)
    610.                       TemplateLocale           : 0x00000409 (1033)
    611.                       SortLocale               : 0x00000409 (1033)
    612.               ppRows                   : *
    613.                   ppRows                   : *
    614.                       ppRows: struct PropertyRowSet_r
    615.                           cRows                    : 0x00000001 (1)
    616.                           aRow: ARRAY(1)
    617.                               aRow: struct PropertyRow_r
    618.                                   Reserved                 : 0x00000000 (0)
    619.                                   cValues                  : 0x00000007 (7)
    620.                                   lpProps                  : *
    621.                                       lpProps: ARRAY(7)
    622.                                           lpProps: struct PropertyValue_r
    623.                                               ulPropTag                : PidTagDisplayName_string8 (0x3001001E)
    624.                                               dwAlignPad               : 0x00000000 (0)
    625.                                               value                    : union PROP_VAL_UNION(case 30)
    626.                                               lpszA                    : *
    627.                                                   lpszA                    : 'JohnDoe'
    628.                                           lpProps: struct PropertyValue_r
    629.                                               ulPropTag                : PidTagEmailAddress_string8 (0x3003001E)
    630.                                               dwAlignPad               : 0x00000000 (0)
    631.                                               value                    : union PROP_VAL_UNION(case 30)
    632.                                               lpszA                    : *
    633.                                                   lpszA                    : '/o=First Organization/ou=First Administrative Group/cn=Recipients/cn=JohnDoe'
    634.                                           lpProps: struct PropertyValue_r
    635.                                               ulPropTag                : PidTagDisplayType (0x39000003)
    636.                                               dwAlignPad               : 0x00000000 (0)
    637.                                               value                    : union PROP_VAL_UNION(case 3)
    638.                                               l                        : 0x00000000 (0)
    639.                                           lpProps: struct PropertyValue_r
    640.                                               ulPropTag                : PidTagAddressBookHomeMessageDatabase (0x8006001F)
    641.                                               dwAlignPad               : 0x00000000 (0)
    642.                                               value                    : union PROP_VAL_UNION(case 31)
    643.                                               lpszW                    : *
    644.                                                   lpszW                    : '/o=First Organization/ou=First Administrative Group/cn=Configuration/cn=Servers/cn=PRECOG/cn=Microsoft Private MDB'
    645.                                           lpProps: struct PropertyValue_r
    646.                                               ulPropTag                : PidTagAttachNumber_Error (0xE21000A)
    647.                                               dwAlignPad               : 0x00000000 (0)
    648.                                               value                    : union PROP_VAL_UNION(case 10)
    649.                                               err                      : MAPI_E_NOT_FOUND (0x8004010F)
    650.                                           lpProps: struct PropertyValue_r
    651.                                               ulPropTag                : UNKNOWN_ENUM_VALUE (0x6613000A)
    652.                                               dwAlignPad               : 0x00000000 (0)
    653.                                               value                    : union PROP_VAL_UNION(case 10)
    654.                                               err                      : MAPI_E_NOT_FOUND (0x8004010F)
    655.                                           lpProps: struct PropertyValue_r
    656.                                               ulPropTag                : PidTagAddressBookProxyAddresses_string8 (0x800F101E)
    657.                                               dwAlignPad               : 0x00000000 (0)
    658.                                               value                    : union PROP_VAL_UNION(case 4126)
    659.                                               MVszA: struct StringArray_r
    660.                                                   cValues                  : 0x00000004 (4)
    661.                                                   lppszA                   : *
    662.                                                       lppszA: ARRAY(4)
    663.                                                           lppszA                   : *
    664.                                                               lppszA                   : '=EX:/o=First Organization/ou=First Administrative Group/cn=Recipients/cn=JohnDoe'
    665.                                                           lppszA                   : *
    666.                                                               lppszA                   : 'smtp:postmaster@oc.local'
    667.                                                           lppszA                   : *
    668.                                                               lppszA                   : 'X400:c=US;a= ;p=First Organizati;o=Exchange;s=JohnDoe'
    669.                                                           lppszA                   : *
    670.                                                               lppszA                   : 'SMTP:JohnDoe@oc.local'
    671.               result                   : MAPI_E_SUCCESS (0x0)
    672.        NspiDNToMId: struct NspiDNToMId
    673.           in: struct NspiDNToMId
    674.               handle                   : *
    675.                   handle: struct policy_handle
    676.                       handle_type              : 0x00000000 (0)
    677.                       uuid                     : f734441b-1f31-4ee8-8be4-4143bc88130a
    678.               Reserved                 : 0x00000000 (0)
    679.               pNames                   : *
    680.                   pNames: struct StringsArray_r
    681.                       Count                    : 0x00000001 (1)
    682.                       Strings: ARRAY(1)
    683.                           Strings                  : *
    684.                               Strings                  : '/o=First Organization/ou=First Administrative Group/cn=Configuration/cn=Servers/cn=PRECOG'
    685.   dcesrv_exchange_nsp_dispatch
    686.   exchange_nsp: NspiDNToMId (0x7)
    687.        NspiDNToMId: struct NspiDNToMId
    688.           out: struct NspiDNToMId
    689.               ppMIds                   : *
    690.                   ppMIds                   : *
    691.                       ppMIds: struct PropertyTagArray_r
    692.                           cValues                  : 0x00000001 (1)
    693.                           aulPropTag: ARRAY(1)
    694.                               aulPropTag               : 0x00001b2e (6958)
    695.               result                   : MAPI_E_SUCCESS (0x0)
    696.        NspiGetProps: struct NspiGetProps
    697.           in: struct NspiGetProps
    698.               handle                   : *
    699.                   handle: struct policy_handle
    700.                       handle_type              : 0x00000000 (0)
    701.                       uuid                     : f734441b-1f31-4ee8-8be4-4143bc88130a
    702.               dwFlags                  : 0x00000000 (0)
    703.               pStat                    : *
    704.                   pStat: struct STAT
    705.                       SortType                 : SortTypeDisplayName (0)
    706.                       ContainerID              : 0x00000000 (0)
    707.                       CurrentRec               : UNKNOWN_ENUM_VALUE (6958)
    708.                       Delta                    : 0
    709.                       NumPos                   : 0x00000000 (0)
    710.                       TotalRecs                : 0x00000000 (0)
    711.                       CodePage                 : 0x000004e4 (1252)
    712.                       TemplateLocale           : 0x00000409 (1033)
    713.                       SortLocale               : 0x00000409 (1033)
    714.               pPropTags                : *
    715.                   pPropTags: struct SPropTagArray
    716.                       cValues                  : 0x00000001 (1)
    717.                       aulPropTag: ARRAY(1)
    718.                           aulPropTag               : PidTagAddressBookNetworkAddress_string8 (0x8170101E)
    719.   dcesrv_exchange_nsp_dispatch
    720.   exchange_nsp: NspiGetProps (0x9)
    721.        NspiGetProps: struct NspiGetProps
    722.           out: struct NspiGetProps
    723.               ppRows                   : *
    724.                   ppRows                   : *
    725.                       ppRows: struct PropertyRow_r
    726.                           Reserved                 : 0x00000000 (0)
    727.                           cValues                  : 0x00000001 (1)
    728.                           lpProps                  : *
    729.                               lpProps: ARRAY(1)
    730.                                   lpProps: struct PropertyValue_r
    731.                                       ulPropTag                : PidTagAddressBookNetworkAddress_string8 (0x8170101E)
    732.                                       dwAlignPad               : 0x00000000 (0)
    733.                                       value                    : union PROP_VAL_UNION(case 4126)
    734.                                       MVszA: struct StringArray_r
    735.                                           cValues                  : 0x00000006 (6)
    736.                                           lppszA                   : *
    737.                                               lppszA: ARRAY(6)
    738.                                                   lppszA                   : *
    739.                                                       lppszA                   : 'ncacn_vns_spp:PRECOG'
    740.                                                   lppszA                   : *
    741.                                                       lppszA                   : 'netbios:PRECOG'
    742.                                                   lppszA                   : *
    743.                                                       lppszA                   : 'ncacn_np:PRECOG'
    744.                                                   lppszA                   : *
    745.                                                       lppszA                   : 'ncacn_spx:PRECOG'
    746.                                                   lppszA                   : *
    747.                                                       lppszA                   : 'ncacn_ip_tcp:precog.oc.local'
    748.                                                   lppszA                   : *
    749.                                                       lppszA                   : 'ncalrpc:PRECOG'
    750.               result                   : MAPI_E_SUCCESS (0x0)
    751.        NspiUnbind: struct NspiUnbind
    752.           in: struct NspiUnbind
    753.               handle                   : *
    754.                   handle: struct policy_handle
    755.                       handle_type              : 0x00000000 (0)
    756.                       uuid                     : f734441b-1f31-4ee8-8be4-4143bc88130a
    757.               Reserved                 : 0x00000000 (0)
    758.   dcesrv_exchange_nsp_dispatch
    759.   [dcesrv_NspiUnbind:211]: Session found and released
    760.        NspiUnbind: struct NspiUnbind
    761.           out: struct NspiUnbind
    762.               handle                   : *
    763.                   handle: struct policy_handle
    764.                       handle_type              : 0x00000000 (0)
    765.                       uuid                     : f734441b-1f31-4ee8-8be4-4143bc88130a
    766.               result                   : MAPI_E_SUCCESS (0x0)
    767.   Terminating connection - 'NT_STATUS_CONNECTION_DISCONNECTED'
    768.   single_terminate: reason[NT_STATUS_CONNECTION_DISCONNECTED]
    769.   dcesrv_exchange_nsp_unbind
    770.   dcesrv_exchange_emsmdb_unbind

