import os

import sys
import _mysql

dbargs = {user:"user",passwd:"pass",db:"blogs"}
wpcontent = "/home/blogs/public_html/wp-content/blogs.dir/"

newsymlinks = []
oldsymlinks = []
ids=[]

def update_symlinks():
    db=_mysql.connect(**dbargs)
    for dir in os.listdir(wpcontent):
	try: 
            ids.append(int(dir))
        except:
            pass
    query_str = "SELECT w.domain, w.blog_id FROM wp_blogs w WHERE w.public = 1 AND w.archived=0 AND w.mature=0 AND w.deleted=0 AND w.spam=0 AND "
    for id in ids:
	query_str += "w.blog_id = "+str(id)+ " OR "
    
#    print query_str[:-4] #remove last stray OR
    db.query(query_str[:-4])

    data=db.store_result()
    #data.fetch_row()

    data.data_seek(0)
    for i in xrange(data.num_rows()):
	row = data.fetch_row()
	try:
            os.symlink(wpcontent+str(row[0][1]), wpcontent+"direct/"+str(row[0][0]))
            print row[0][0], row[0][1]
        except OSError:
            print row[0][0], row[0][1], "link exists"


if (len(sys.argv) > 1):
    if( sys.argv[1] == '-s' ):
        update_symlinks()



