import time


from bitstamp import bitstamp


def test_ticker():
	api = bitstamp.BitstampPublic()

	while True:
		print(api.ticker())
		# Change this to less at your own risk - Bitstamp has a harsh policy about exceeding allowed number of calls
		time.sleep(1)


def test_order_book_ws():
	def handle_message(message):
		print(message)

	api = bitstamp.BitstampPublic()
	api.attach_ws(bitstamp.WS_CHANNEL_ORDER_BOOK, handle_message,"xrpusd")


test_order_book_ws()

