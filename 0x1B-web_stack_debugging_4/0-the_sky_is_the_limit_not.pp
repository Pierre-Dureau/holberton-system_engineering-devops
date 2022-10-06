# change the limit
exec {'change ulimit 15 to 15000':
  command  => 'sed -i s/15/15000/g /etc/default/nginx',
  provider => shell,
}
exec {'restart nginx':
  command  => 'sudo service nginx restart',
  path     => '/usr/bin',
}
