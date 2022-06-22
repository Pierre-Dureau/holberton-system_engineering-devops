#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(.*?)\].{5,5}(.*?)\].{8,8}(.*?)\]/).join(',')
