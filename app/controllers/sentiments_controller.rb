class SentimentsController < ApplicationController
	before_action :set_sentiment
	def index
		redirect_to new_sentiment_path
	end

	def new
		@sentiment = Sentiment.new
	end

	def create
		@sentiment = Sentiment.new(sentiment_params)
		if @sentiment.save
			@sentiment.agg_score =  %x(python main.py app/assets/inputs/input.json)
			@sentiment.save
			redirect_to sentiment_path(@sentiment)
		else
			render action: 'new'
		end
	end

	def show
		#parse output from file if exists
		#open file, iterate through
		
		#parse csv file


		#ALL FAKE STUFF
		@main_score = 88
		@articles = #title, url, pos, neg, timestamp
	end

	private
	def sentiment_params
		params.require(:sentiment).permit(:stock_symbol, :start_date, :end_date)
	end
end
