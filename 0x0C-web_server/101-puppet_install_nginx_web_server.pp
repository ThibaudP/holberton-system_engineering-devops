# Puppet manifest to install nginx
package { 'nginx':
  ensure   => installed,
  provider => 'apt'
}

file_line { 'nyan cat rewrite rule':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Holberton School',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
