class AddJsonToSentiments < ActiveRecord::Migration
  def change
    add_column :sentiments, :json, :string
  end
end
