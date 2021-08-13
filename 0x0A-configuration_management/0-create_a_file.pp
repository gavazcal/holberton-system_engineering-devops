# Creates a file
file { 'holberton':
  path    => '/tmp/holberton',
  ensure  => file,
  mode    => '0774',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
