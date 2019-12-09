# Kills the command killmenow
exec { 'Kills killmenow' :
  command  => 'pkill killmenow'
  creates  => '/killmenow'
}
