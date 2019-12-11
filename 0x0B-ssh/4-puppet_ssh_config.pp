# Creates a file n stuff
<<<<<<< HEAD
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
=======
file { '/.ssh/config' :
  ensure   =>  'file',
  content  =>  'PasswordAuthentication no
  ChallengeResponseAuthentication no',
>>>>>>> f4ffb3378a6e302eb212c62c2cd63a75c591962a
}
