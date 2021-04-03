# Add correct flags in ssh config

exec { '/etc/ssh/ssh_config':
  path    => ['/usr/bin', '/bin'],
  command => 'echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config; echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
}
