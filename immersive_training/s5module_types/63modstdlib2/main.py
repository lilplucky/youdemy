"""
┌─[root@ZERXIS]─[/home/hulbert/Desktop/youdemy/immersive_training/s5module_types/62modules_stdlib1]
└──╼ #python
Python 3.11.2 (main, Sep 14 2024, 03:00:30) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import platform
>>> x = dir(platform)
>>> x
['_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_comparable_version', '_component_re', '_default_architecture', '_follow_symlinks', '_get_machine_win32', '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser', '_java_getprop', '_libc_search', '_mac_ver_xml', '_node', '_norm_version', '_os_release_cache', '_os_release_candidates', '_os_release_line', '_os_release_unescape', '_parse_os_release', '_platform', '_platform_cache', '_pypy_sys_version_parser', '_sys_version', '_sys_version_cache', '_sys_version_parser', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank', '_ver_output', '_ver_stages', 'architecture', 'collections', 'freedesktop_os_release', 'functools', 'itertools', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']
>>> y = platform.system()
>>> y
'Linux'
>>> help('modules') 

Please wait a moment while I gather a list of all available modules...

No menu prefix found, MenuLibre will not function properly.
No menu prefix found, MenuLibre will not function properly.
/usr/lib/python3/dist-packages/_distutils_hack/__init__.py:33: UserWarning: Setuptools is replacing distutils.
  warnings.warn("Setuptools is replacing distutils.")
Cryptodome          _tracemalloc        h2                  requests_toolbelt
DbgPlugInDiggers    _typing             hashlib             resource
LibAppArmor         _uuid               heapq               rfc3986
OpenSSL             _warnings           hmac                rfc3987
PIL                 _weakref            hpack               rich
PyQt5               _weakrefset         html                rlcompleter
PySide2             _xxsubinterpreters  html5lib            runpy
UICommon            _xxtestfuzz         http                samba
VBoxAuth            _yaml               httpcore            sched
VBoxAuthSimple      _zoneinfo           httplib2            secrets
VBoxDD              abc                 httpx               select
VBoxDD2             aifc                hyperframe          selectors
VBoxDDU             antigravity         idna                setproctitle
VBoxDbg             anyio               imaplib             setuptools
VBoxDragAndDropSvc  apparmor            imghdr              shelve
VBoxDxVk            apt                 imp                 shiboken2
VBoxGuestControlSvc apt_inst            importlib           shlex
VBoxGuestPropSvc    apt_pkg             inspect             shutil
VBoxHeadless        aptsources          io                  signal
VBoxHostChannel     argparse            ipaddress           simplejson
VBoxKeyboard        array               itertools           site
VBoxLibSsh          asgiref             itsdangerous        sitecustomize
VBoxNetDHCP         asn1crypto          jinja2              six
VBoxNetNAT          ast                 json                smtpd
VBoxRT              asynchat            jsonpointer         smtplib
VBoxSVGA3D          asyncio             jsonschema          sndhdr
VBoxSharedClipboard asyncore            jwt                 sniffio
VBoxSharedFolders   atexit              kaitaistruct        socket
VBoxVMM             attr                keyword             socketio
VBoxXPCOM           attrs               ldap3               socketserver
VBoxXPCOMC          audioop             ldb                 socks
VBoxXPCOMIPCD       babel               lib2to3             sockshandler
VirtualBoxVM        base64              libevdev            softwareproperties
__future__          bdb                 libmat2             sortedcontainers
__hello__           bidict              libvboxjxpcom       soupsieve
__phello__          binascii            linecache           spwd
_abc                bisect              locale              sqlite3
_aix_support        blinker             logging             sre_compile
_ast                blueman             lxml                sre_constants
_asyncio            brotli              lzma                sre_parse
_bisect             bs4                 mailbox             ssl
_blake2             builtins            mailcap             stat
_blueman            bz2                 main                statistics
_bootsubprocess     cProfile            markdown_it         stem
_brotli             cairo               markupsafe          string
_bz2                calendar            marshal             stringprep
_cffi_backend       certifi             math                struct
_codecs             cgi                 mdurl               subprocess
_codecs_cn          cgitb               mechanize           sunau
_codecs_hk          chardet             menulibre           symtable
_codecs_iso2022     charset_normalizer  menulibre_lib       sys
_codecs_jp          chunk               mimetypes           sysconfig
_codecs_kr          click               mitmproxy           syslog
_codecs_tw          cmath               mmap                tabnanny
_collections        cmd                 modulefinder        talloc
_collections_abc    code                msgpack             tarfile
_compat_pickle      codecs              multiprocessing     tdb
_compression        codeop              mutagen             telnetlib
_contextvars        collections         nacl                tempfile
_crypt              colorama            neovim              terminatorlib
_csv                colorsys            netifaces           termios
_ctypes             compileall          netrc               test
_ctypes_test        compose             nis                 texttable
_curses             concurrent          nntplib             textwrap
_curses_panel       configobj           notify2             this
_datetime           configparser        ntp                 threading
_dbm                contextlib          ntpath              time
_dbus_bindings      contextvars         nturl2path          timeit
_dbus_glib_bindings copy                numbers             tkinter
_decimal            copyreg             nyx                 token
_distutils_hack     crypt               oauthlib            tokenize
_distutils_system_mod cryptography        olefile             tomllib
_elementtree        csv                 onionshare          torbrowser_launcher
_functools          ctypes              onionshare_cli      tornado
_hashlib            curl                opcode              trace
_heapq              curses              operator            traceback
_imp                dataclasses         optparse            tracemalloc
_io                 datetime            os                  tty
_json               dbm                 ossaudiodev         turtle
_ldb_text           dbus                packaging           types
_locale             deb822              passlib             typing
_lsprof             debconf             pathlib             typing_extensions
_lzma               debian              pdb                 ufw
_markupbase         debian_bundle       pickle              unicodedata
_md5                debianbts           pickletools         unidecode
_multibytecodec     decimal             pip                 unittest
_multiprocessing    difflib             pipes               uno
_opcode             dis                 pkg_resources       unohelper
_operator           distro              pkgutil             uritemplate
_osx_support        distutils           platform            urllib
_pickle             dns                 plistlib            urllib3
_posixshmem         docker              png                 urwid
_posixsubprocess    dockerpty           poplib              uu
_py_abc             docopt              posix               uuid
_pydecimal          doctest             posixpath           validate
_pyio               dotenv              pprint              vboxapi
_pyrsistent_version email               profile             vboxshell
_queue              encodings           pstats              venv
_random             engineio            psutil              wadllib
_ruamel_yaml        ensurepip           pty                 warnings
_sha1               enum                publicsuffix2       wave
_sha256             errno               pvectorc            weakref
_sha3               eventlet            pwd                 webbrowser
_sha512             faulthandler        py_compile          webcolors
_signal             fcntl               pyasn1              webencodings
_sitebuiltins       filecmp             pyclbr              websocket
_socket             fileinput           pycurl              websockets
_sqlite3            flask               pydoc               werkzeug
_sre                flask_socketio      pydoc_data          wheel
_ssl                fnmatch             pyexpat             wsgiref
_stat               fractions           pygments            wsproto
_statistics         ftplib              pygtkcompat         xapp
_string             functools           pyinotify           xdrlib
_strptime           gc                  pynvim              xml
_struct             genericpath         pyparsing           xmlrpc
_symtable           getopt              pyperclip           xxlimited
_sysconfigdata__linux_x86_64-linux-gnu getpass             pyrsistent          xxlimited_35
_sysconfigdata__x86_64-linux-gnu gettext             pysimplesoap        xxsubtype
_tdb_text           gevent              pytz                yaml
_testbuffer         geventwebsocket     pyudev              yt_dlp
_testcapi           gi                  qrcode              zipapp
_testclinic         glob                queue               zipfile
_testimportmultiple gpg                 quopri              zipimport
_testinternalcapi   graphlib            random              zlib
_testmultiphase     greenlet            re                  zoneinfo
_thread             grp                 readline            zope
_threading_local    gyp                 reportbug           zstandard
_tkinter            gzip                reprlib             
_tokenize           h11                 requests            

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

>>> 
"""
import platform
x = dir(platform)
x

y = platform.system()
y
help('modules') #max one parameter
