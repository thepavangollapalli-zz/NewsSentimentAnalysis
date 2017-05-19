class SentimentsController < ApplicationController
	before_action :set_sentiment, only: [:show]
	require 'csv'

	def index
		redirect_to new_sentiment_path
	end

	def new
		@sentiment = Sentiment.new
	end

	def create
		@sentiment = Sentiment.new(sentiment_params)
		if @sentiment.save
			# @sentiment.agg_score =  %x(python main.py app/assets/inputs/input.json)
			# @sentiment.save
			redirect_to sentiment_path(@sentiment)
		else
			render action: 'new'
		end
	end

	def show
		@nice_start_date = Date.strptime(@sentiment.start_date, "%d/%m/%y").strftime("%A, %e %B %Y")
		if !@sentiment.end_date.empty?
			@nice_end_date = Date.strptime(@sentiment.end_date, "%d/%m/%y").strftime("%A, %e %B %Y")
		end
		#parse output from file if exists
		#open file, iterate through
		
		#parse csv file
		@articles = CSV.read('app/assets/inputs/sentiments.csv', :headers => true) #title, url, pos, neg, timestamp
		@timestamps = @articles['timestamp']

		#ALL FAKE STUFF
		
		@main_score = 88.0

		#deletes csv file - uncomment later
		# File.delete('app/assets/inputs/sentiments.csv') if File.exist?('app/assets/inputs/sentiments.csv')
	end

	private
	def sentiment_params
		params.require(:sentiment).permit(:stock_symbol, :start_date, :end_date)
	end

	def set_sentiment
		@sentiment = Sentiment.find(params[:id])
	end
end
