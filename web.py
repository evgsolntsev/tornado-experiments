import tornado.ioloop
import tornado.web
import tornado.httpserver
import os


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hey")

def make_server():

	app = tornado.web.Application([
		(r"/", MainHandler),
	])
	return tornado.httpserver.HTTPServer(app)


if __name__ == "__main__":
	server = make_server()
	server.listen(os.environ.get("PORT", 8080))
	tornado.ioloop.IOLoop.instance().start()
