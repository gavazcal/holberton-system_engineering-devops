# Creates a file
file { 'holberton':
  ensure  => file,
  path    => '/tmp/holberton',
  mode    => '0774',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
