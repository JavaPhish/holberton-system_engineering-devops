
# Creates a file n stuff
File_line { 'Turn off passwd auth' :

  path     =>  '~/ssh/ssh_config',
  line     =>  'PasswordAuthentication yes',
  content  =>  'PasswordAuthentication no',
}

File_line { 'Declar identity file' :
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile',
  content => 'IdentityFile ~/.ssh/holberton',
}
