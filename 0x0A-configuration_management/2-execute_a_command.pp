# Kills the process killmenow
exec { 'Kill killmenow process':
  command  => 'pkill killmenow',
  path     => '/usr/bin/',
  provider => shell
}
