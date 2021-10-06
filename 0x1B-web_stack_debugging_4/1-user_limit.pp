# does some debugging
exec {'debugger':
path    => ['/bin/', '/sbin/', '/usr/bin/'],
command => 'echo -n > /etc/security/limits.conf',
}
