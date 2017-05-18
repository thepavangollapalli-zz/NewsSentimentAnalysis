class Sentiment < ActiveRecord::Base
	#list of companies
	COMPANIES = ['GOOG']

	#validations
	validates :stock_symbol, presence: true, inclusion: { in: Sentiment::COMPANIES}
	validates_date :start_date
    validates_date :end_date, on_or_after: :start_date
end
