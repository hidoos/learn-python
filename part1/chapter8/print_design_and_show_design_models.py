undesign_models = ['web design', 'ios design', 'android design']
complete_models = []
def print_design(undesign_models,complete_models):
    while undesign_models:
        model = undesign_models.pop()
        print('printing model:' + model)
        complete_models.append(model)

def show_complete_models(complete_models):
    for model in complete_models:
        print('complete model is:' + model)

# invoke function 
print_design(undesign_models, complete_models)
show_complete_models(complete_models)

# 'int' object is not iterable 
#  iterable ：int 不能被迭代，那么除了使用 python 自带的数据类型，
# 怎么由用户自定义一个可迭代的对象呢？

# todo 看来对list的用法还不太熟悉，再仔细熟悉一下list的api吧