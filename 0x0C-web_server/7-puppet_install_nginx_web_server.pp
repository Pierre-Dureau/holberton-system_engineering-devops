# Server configuration with puppet
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}
file { 'index.html':
  ensure  => 'present',
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World',
}
file_line { 'default':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'location /redirect_me {rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;}',
}
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
