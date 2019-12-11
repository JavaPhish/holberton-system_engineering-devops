
# Removes password authentication
file_line { 'Turn off passwd auth' :
  path     =>  '/etc/ssh/ssh_config',
  line     =>  'PasswordAuthentication no'
}
# Enforces use of the holberton key in the ssh folder
file_line { 'Declare identity file' :
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/holberton',
}
