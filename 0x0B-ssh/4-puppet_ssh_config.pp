  
# Creates a file n stuff
file { '/.ssh/config' :
  ensure   =>  'present',
  content  =>  'PasswordAuthentication no
  ChallengeResponseAuthentication no',
}
