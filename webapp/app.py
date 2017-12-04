from flask import Flask, request, Response
import urllib
import urllib2
import time
import subprocess


app = Flask(__name__)

@app.route('/handler',methods=['GET','POST'])
def handler():
#	if request.method == 'GET':
		cmd_para = request.args.get('cmd')
		url_para = request.args.get('url')
		img_name = str(time.time());
		vPath = "./"+ img_name + ".mp4"
		urllib.urlretrieve(url_para, './%s.jpg' % img_name)

		strcmd = "ffmpeg -r 25 -loop 1 -i " + "./" + img_name + ".jpg" + " -pix_fmt yuv420p -vcodec libx264 -b:v 600k -r:v 25 -preset medium -crf 30 -s 720x576 -vframes 50  -t 2 " + vPath + " >/dev/null 2>&1"
		subprocess.call(strcmd,shell=True)
		img_vod = file(vPath)
		resp = Response(img_vod, mimetype = "video/mp4")
		resp.headers["Content-Disposition"] = "attachment; filename=" + img_name + ".mp4"

		return resp

#	elif request.method == 'POST':
		
#		return "Wrong"

@app.route('/health')
def health():
	return "OK"

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=9100)


