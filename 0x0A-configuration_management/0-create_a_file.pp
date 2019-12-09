file { 'holberton' :
  ensure   =>  '{md5}f1b70c2a42a98d82224986a612400db9',
  path     =>  '/tmp/holberton',
  content  =>  'I love Puppet',
  owner    =>  'www-data',
  group    =>  'www-data',
  mode     =>  '0744'
}
