class DateToString < ActiveRecord::Migration
  def change
  	change_table :sentiments do |t|
      t.change :start_date, :string
      t.change :end_date, :string
    end
  end
end
