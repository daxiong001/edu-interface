import os
import subprocess
from urllib import parse

def run():
    password = parse.quote_plus("a8sblx3x@Nu%1x&Tg037KI@03Y4JRL@2")
    args = "sqlacodegen --outfile portal_models.py mysql+pymysql://root:{0}@106.55.218.224:37313/education_portal".format(password)
    os.system(args)


if __name__ == '__main__':
    run()
