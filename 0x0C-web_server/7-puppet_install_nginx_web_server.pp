# Server configuration with puppet
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}
file { 'index.html':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hellow World\n',
}
file_line { 'default':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => '\tlocation /redirect_me {\n\t\trewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n\t}',
}

