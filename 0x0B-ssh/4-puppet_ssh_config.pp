# Creates a file n stuff
File_line { 'Turn off passwd auth' :
  ensure   =>  'present',
  path     =>  '~/.ssh/config',
  line     =>  'PasswordAuthentication yes',
  content  =>  'PasswordAuthentication no',
}

File_line { 'Declare identity file' :
  ensure  => 'present',
  path    => '~/.ssh/config',
  line    => 'IdentityFile',
  content => 'IdentityFile ~/.ssh/holberton',
}
