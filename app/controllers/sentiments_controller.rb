class SentimentsController < ApplicationController
	def index
		redirect_to new_sentiment_path
	end

	def new
		@sentiment = Sentiment.new
	end

	def create
		@sentiment = Sentiment.new(sentiment_params)
		if @sentiment.save
			#run python script with symbol, dates

			redirect_to sentiment_path(@sentiment)
		else
			render action: 'new'
		end
	end

	def show
		#parse output from file if exists
		#open file, iterate through
		@sentiment_score = nil
		@article_list = nil
	end

	private
	def sentiment_params
		params.require(:sentiment).permit(:stock_symbol, :start_date, :end_date)
	end
end
