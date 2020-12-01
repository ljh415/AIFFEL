#!/usr/bin/env python
# coding: utf-8

# In[9]:


import face_recognition
import os
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# 이미지에서 얼굴영역만 잘라낸 cropped_face
def get_gropped_face(image_file):
    image = face_recognition.load_image_file(image_file)
    face_locations = face_recognition.face_locations(image)
    try:
        a, b, c, d = face_locations[0]
        cropped_face = image[a:c,d:b,:]
        return cropped_face
    except:
        return False


# 얼굴 영역을 가지고 얼굴 임베딩 벡터를 구하는 함수
def get_face_embedding(face):
    return face_recognition.face_encodings(face)


def get_face_embedding_dict(dir_path):
    file_list = os.listdir(dir_path)
    embedding_dict = {}

    for file in file_list:
        img_path = os.path.join(dir_path, file)
        face = get_gropped_face(img_path)
        try :
            embedding = get_face_embedding(face)
        except :
            pass
        if len(embedding) > 0:  # 얼굴영역 face가 제대로 detect되지 않으면  len(embedding)==0인 경우가 발생하므로 
                    # os.path.splitext(file)[0]에는 이미지파일명에서 확장자를 제거한 이름이 담깁니다. 
            embedding_dict[os.path.splitext(file)[0]] = embedding[0]

    return embedding_dict


import numpy as np
def get_distance(name1, name2, embedding_dict):
    return np.linalg.norm(embedding_dict[name1]-embedding_dict[name2], ord=2)


# name1과 name2의 거리를 비교하는 함수를 생성하되, name1은 미리 지정하고, name2는 호출시에 인자로 받도록 합니다.
def get_sort_key_func(name1, embedding_dict):
    def get_distance_from_name1(name2, embedding_dict):
        return get_distance(name1, name2, embedding_dict)
    return get_distance_from_name1

# sort_key_func = get_sort_key_func('trump')   
# 이렇게 생성된 함수 sort_key_func는 sort_key_func('obama') 라고 호출할 때 trump와 obama 사이의 임베딩 벡터 거리를 계산합니다.


# 우리는 이미 모든 이미지 파일에 대한 얼굴 임베딩 딕셔너리를 가지고 있습니다.
# 이제 우리는 이 딕셔너리를 오름차순 정렬하되, 정렬 기준을 바로 trump와의 임베딩 벡터 거리 함수로 할 것입니다. 이때 lambda 함수가 정렬 key로 활용됩니다.

# sorted(embedding_dict.items(), key=lambda x:sort_key_func(x[0]))


def get_nearest_face(name, embedding_dict, top=4):
    ret_dict = {}
    sort_key_func = get_sort_key_func(name, embedding_dict)
    sorted_faces = sorted(embedding_dict.items(), key=lambda x:sort_key_func(x[0], embedding_dict))

    for i in range(top+1):
        if i == 0 :   # 첫번째로 나오는 이름은 자기 자신일 것이므로 제외합시다. 
            continue
        if sorted_faces[i]:
            print('순위 {} : 이름({}), 거리({})'.format(i, sorted_faces[i][0],sort_key_func(sorted_faces[i][0], embedding_dict)))

    return sorted_faces[1][0]







