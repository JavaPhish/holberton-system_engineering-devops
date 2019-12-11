  
# Creates a file n stuff
file { '/.ssh/config' :
  ensure   =>  'file',
  content  =>  'PasswordAuthentication no
  ChallengeResponseAuthentication no',
}
