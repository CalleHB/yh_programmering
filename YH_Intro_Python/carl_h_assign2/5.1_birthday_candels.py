#declare our variabels how many candels in a box and how old the person going to get
candles_per_box = 24
years = 100

#more vaiables that are empty for out loop
num_candles = 0
total_boxes = 0


#loop that iterates thruoght each year from 1 to years variabel +1
for year in range(1, years + 1):
    num_candles += year #adds the amoun of yers to our vaiable num_candels to get the amount to candels we use each year
    if num_candles >= candles_per_box: #if we need more candels the there is in a box
        boxes_to_buy = num_candles // candles_per_box #we buy more candels and divide it by how many the is in each box
        total_boxes += boxes_to_buy #for each box we buy we add 1 to total_boxes
        num_candles -= boxes_to_buy * candles_per_box #calculat the remaing num,ber of candels use to fill the boxes from the total number of candels
        print(f"Before birthday {year}, buy {boxes_to_buy} box(es)")

print(f"Total number of boxes: {total_boxes}, Remaining candles: {num_candles}")
