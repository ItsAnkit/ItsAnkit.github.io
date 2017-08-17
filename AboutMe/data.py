import cgi
import redis
formdata=cgi.fieldStorage()
key=['Name', 'Phone', 'Email', 'Comments']
val=[]
r = redis.Redis(host='localhost', port=6379, db=0)
for i in range(len(key))
	val[i]=formdata.getValue(key[i])
	r.rpush(key[i], val[i])