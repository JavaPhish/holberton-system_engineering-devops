#!/usr/bin/env ruby
send = ARGV[0].scan(/from:(.\w+)/).join
receiv = ARGV[0].scan(/to:(.\w+)/).join
flag = ARGV[0].scan(/flags:(-1|0)(:)(-1|0)(:)(-1|0)(:)(-1|0)(:)(-1|0)/).join 

puts send + "," + receiv + "," + flag
