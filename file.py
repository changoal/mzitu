import os
import pymongo

folders = ['F:\\鐎涳缚绡刓\Android缁楊兛绔寸悰灞煎敩閻焦绨惍涔梊缁楋拷11缁旂嚩\1', 'D:\\鏉╁懘娴勬稉瀣祰']

client = pymongo.MongoClient('localhost', 27017)

collection_video = client['files']['movies']
collection_img = client['files']['imgs']
mzitu_folder = client['mzitu']['dir']
mzitu_img = client['mzitu']['images']

back_videos = [
    '.mp4', '.wmv', '.avi', '.MP4', '.mov', '.null', '.MPG', '.mkv', '.mpg'
]

back_imgs = ['.jpg', '.gif', '.png']


def insertMovie(data):
    collection_video.insert_one(data)


def insertImg(data):
    collection_img.insert_one(data)


def get_file_suffix(file):
    # 閼惧嘲绶遍弬鍥︽閸氬海绱戦崥锟�
    return file[file.rindex('.'):len(file)]


def get_file_name(file):
    # 閼惧嘲绶遍弬鍥︽閸氬海绱戦崥锟�
    return file[0:file.rindex('.')]


def test():
    for folder in folders:
        g = os.walk(folder)
        for path, dir_list, file_list in g:
            for file in file_list:
                # 閸掔娀娅庣粔宥呯摍
                if file.endswith('torrent'):
                    os.remove(path + "/" + file)
                    print(path + "/" + file + " has been deleted")
                back = get_file_suffix(file)

                if back in back_videos:
                    data = {
                        "name": get_file_name(file),
                        'path': path + "/" + file,
                        'size': os.path.getsize(path + "/" + file)
                    }
                    insertMovie(data)
                    print(data)
                elif back in back_imgs:
                    data = {
                        "name": get_file_name(file),
                        'path': path + "/" + file,
                        'size': os.path.getsize(path + "/" + file)
                    }
                    insertImg(data)
                    print(data)


def get_folder_name(path):
    return path[path.rindex('\\') + 1:len(path)]


def get_all_img():
    img_folder = 'D:\\mzitu\\full'
    g = os.walk(img_folder)
    aaa = 0
    for path, dir_list, file_list in g:
        if aaa == 0:
            aaa = 1
        else:
            # folder_id = Folder.objects.get(path=path)['id']
            for file in os.listdir(path):
                image = {
                    "name": file,
                    "path": path + "/" + file,
                    "size": os.path.getsize(path + "/" + file)
                }
                # folder.save()
                print(image)

        # for file in file_list:
        #     data = {
        #         "name": get_file_name(file),
        #         'path': path + "\\" + file,
        #         'size': os.path.getsize(path + "/" + file)
        #     }
        #     mzitu_img.insert_one(data)
        #     print(data)


def fromdb():
    f = mzitu_folder.find()
    for line in f:
        print(line['name'], line['path'], int(line['file_count']))
        # print(line)


if __name__ == '__main__':
    # test()
    get_all_img()
