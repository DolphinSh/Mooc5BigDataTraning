import requests


def download_image(url):
    _, image_name = url.rsplit("/", 1)
    r = requests.get(url)
    with open("./images/" + image_name, "wb") as fp:
        fp.write(r.content)


page_limit = 50
page_start = 1

# 新建文件
movie_fp = open("./movies.txt", "w")

# 保存数据
while True:
    print("正在爬去第{}页.......".format(page_start))
    # 发起GET请求
    r = requests.get(
        "https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit={}&page_start={}".format(
            page_limit, page_start),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
        }
        )

    print(r.status_code)
    # 查看请求是否成功
    if r.status_code != 200:
        print("操作失败")
        break
    else:
        # 提取数据
        d = r.json()
        movies = d['subjects']
        if not movies:
            break
        print("获得{}电影".format(len(movies)))
        for movie in movies:
            download_image(movie['cover'])
            movie_fp.write(str(movie) + "\n")

        page_start += 1

# 关闭文件
movie_fp.close()
