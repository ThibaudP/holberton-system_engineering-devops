# Fix typo in a require() in wp-settings.php
exec { 'someoneneedsmorecoffee':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    =>  ['/bin', '/usr/bin']
}
