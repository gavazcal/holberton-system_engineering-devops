# Executes a killmenow comman
exec { 'pkill':
  command => '/usr/bin/pkill killmenow'
}
