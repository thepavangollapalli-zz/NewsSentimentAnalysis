class AddAggScore < ActiveRecord::Migration
  def change
  	add_column :sentiments, :agg_score, :float
  end
end
