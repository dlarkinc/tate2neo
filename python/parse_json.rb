require 'rubygems'
require 'json'

total = 0

Dir.foreach('/home/larkin/Dropbox/DAH PhD/Neo4J/Metadata/tate/collection/artworks/p/012') do |item|
  	next if item == '.' or item == '..'

	file = open("/home/larkin/Dropbox/DAH PhD/Neo4J/Metadata/tate/collection/artworks/p/012/" + item)
	json = file.read
	total = total + 1
	p total
	parsed = JSON.parse(json)
	p item
	p parsed["title"]

	if parsed["movementCount"] > 0
		if parsed["movements"].kind_of?(Array)
			parsed["movements"].each do |movement|
				p movement["name"]
			end
		end
	end

	if parsed["subjectCount"] > 0
		parsed["subjects"]["children"].each do |subject|
			p subject["name"]
			if subject["children"].kind_of?(Array)
				subject["children"].each do |level2|
					p "-" + level2["name"]
					if level2["children"].kind_of?(Array)
						level2["children"].each do |level3|
							p "--" + level3["name"]
							if level3["children"].kind_of?(Array)
								level3["children"].each do |level4|
									p "---" + level4["name"]
									if level4["children"].kind_of?(Array)
										level4["children"].each do |level5|
											p "---" + level5["name"]
										end
									end
								end
							end
						end
					end
				end
			end
		end
	end
end
