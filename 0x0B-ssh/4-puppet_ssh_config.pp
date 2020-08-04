class { 'ssh':
  server_options => {
      'PasswordAuthentication' => 'no',
	'IdentityFile'           => '~/.ssh/holberton',
    }
}
