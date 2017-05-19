class Sentiment < ActiveRecord::Base
	before_create :api_call

	#list of companies
	#COMPANIES = [['Google (GOOG)', 'Google'], ['Credit Suisse (CS)', 'Credit Suisse'], ['Facebook (FB)', 'Facebook'], ['Yahoo (YHOO)', 'Yahoo'], ['Tableau (DATA)', 'Tableau Software'], ['Microsoft (MS)', 'Microsoft'], ['Thomson Reuters Inc. (TRI)', 'Thomson Reuters'], ['Goldman Sachs(GS)', 'Goldman Sachs'], ['Amazon (AMZN)','Amazon'], ['Cloudera (CLDR)','Cloudera']]
	COMPANIES = ['Google (GOOG)', 'Credit Suisse (CS)', 'Facebook (FB)', 'Yahoo (YHOO)', 'Tableau Software (DATA)', 'Microsoft (MS)', 'Thomson Reuters Inc. (TRI)', 'Goldman Sachs (GS)', 'Amazon (AMZN)', 'Cloudera (CLDR)']
	#validations
	validates :stock_symbol, presence: true, inclusion: { in: Sentiment::COMPANIES } #COMPANIES.map{|key, value| value}
	validates_date :start_date, allow_blank: false
    validates_date :end_date, on_or_after: :start_date, allow_blank: true

    def api_call
    	# Modified from http://developer.nytimes.com/ and LucyBot
    	#reformat start date
    	begin_date = Date.strptime(self.start_date, "%d/%m/%y").strftime("%Y%m%d")
    	til_date = ""
    	if self.end_date.empty?
    		uri = URI("https://api.nytimes.com/svc/search/v2/articlesearch.json")
			http = Net::HTTP.new(uri.host, uri.port)
			http.use_ssl = true
			uri.query = URI.encode_www_form({
			  "api-key" => "3187d3c65dc849aa965473461adcde3d",
			  "q" => "#{self.stock_symbol}",
			  "begin_date" => "#{begin_date}"
			})
    	else
    		#Specify end date only if it exists
    		til_date = Date.strptime(self.end_date, "%d/%m/%y").strftime("%Y%m%d")
    		uri = URI("https://api.nytimes.com/svc/search/v2/articlesearch.json")
			http = Net::HTTP.new(uri.host, uri.port)
			http.use_ssl = true
			uri.query = URI.encode_www_form({
			  "api-key" => "3187d3c65dc849aa965473461adcde3d",
			  "q" => "#{self.stock_symbol}",
			  "begin_date" => "#{begin_date}",
			  "end_date" => "#{til_date}"
			})
    	end
		request = Net::HTTP::Get.new(uri.request_uri)
		@result = http.request(request).body #JSON.parse

		File.open("app/assets/inputs/input.json", "w+") do |f| #  #{self.stock_symbol}
		  # f.write(begin_date)
		  # f.write(til_date)
		  f.write(@result)
		end

		self.json = "app/assets/inputs/input.json"
    end
end


# Date.strptime(date, "%m/%d/%y").strftime("%Y%m%d")