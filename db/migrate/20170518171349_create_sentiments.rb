class CreateSentiments < ActiveRecord::Migration
  def change
    create_table :sentiments do |t|
      t.string :stock_symbol
      t.date :start_date
      t.date :end_date
      t.string :sent_result

      t.timestamps null: false
    end
  end
end
