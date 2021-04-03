# Add correct flags in ssh config
include stdlib

file_line {'Turn off passwd auth':
  ensure => present,
  path   => '~/.ssh/config',
  line   => '\tPasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '~/.ssh/config',
  line   => '\tIdentityFile ~/.ssh/holberton',
}
