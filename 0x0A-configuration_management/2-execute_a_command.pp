# Kills the command killmenow
exec { 'Kills killmenow' :
  command  => 'pkill killmenow',
  path     => '/usr/bin:/usr/sbin:/bin',
  creates  => '/killmenow',
  provider => 'shell'
}
