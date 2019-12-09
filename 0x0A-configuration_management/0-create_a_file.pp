# Creates a file n stuff
file { '/tmp/holberton' :
  ensure   =>  'present',
  content  =>  'I love Puppet',
  owner    =>  'www-data',
  group    =>  'www-data',
  mode     =>  '0744'
}
