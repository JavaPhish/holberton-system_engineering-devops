#!/usr/bin/env ruby
s_from = ARGV[0].scan(/(?<=from:)(.*?)(?=\])/).join
s_phone = ARGV[0].scan(/(?<=to:)(.*?)(?=\])/).join
s_flags = ARGV[0].scan(/(?<=flags:)(.*?)(?=\])/).join

puts s_from + ',' + s_phone + ',' + s_flags
