# -*- coding = utf-8 -*-
"""
Main function to build recommendation systems.
"""
import utils
from ItemCF import ItemBasedCF
from UserCF import UserBasedCF
from dataset import DataSet
from utils import LogTime


def run_model(model_name, dataset_name, test_size=0.3, clean=False):
    print('*' * 70)
    print('\tThis is %s model trained on %s with test_size = %.2f' % (model_name, dataset_name, test_size))
    print('*' * 70 + '\n')
    model_manager = utils.ModelManager(dataset_name, test_size)
    try:
        trainset = model_manager.load_model('trainset')
        testset = model_manager.load_model('testset')
    except OSError:
        ratings = DataSet.load_dataset(name=dataset_name)
        trainset, testset = DataSet.train_test_split(ratings, test_size=test_size)
        model_manager.save_model(trainset, 'trainset')
        model_manager.save_model(testset, 'testset')
    '''Do you want to clean workspace and retrain model again?'''
    '''if you want to change test_size or retrain model, please set clean_workspace True'''
    model_manager.clean_workspace(clean)
    if model_name == 'ItemCF':
        model = ItemBasedCF()
    elif model_name == 'UserCF':
        model = UserBasedCF()
    else:
        raise ValueError('No model named ' + model_name)
    model.fit(trainset)
    recommend_test(model, [1, 100, 233, 666, 888])
    model.test(testset)


def recommend_test(model, user_list):
    for user in user_list:
        recommend = model.recommend(str(user))
        print("recommend for userid = %s:" % user)
        print(recommend)
        print()


if __name__ == '__main__':
    main_time = LogTime(words="Main Function")
    dataset_name = 'ml-100k'
    #dataset_name = 'ml-1m'
    model_type = 'ItemCF'
    # model_type = 'UserCF-IIF'
    #model_type = 'ItemCF'
    #model_type = 'Random'
    # model_type = 'MostPopular'
    # model_type = 'ItemCF-IUF'
    # model_type = 'LFM'
    test_size = 0.3
    run_model(model_type, dataset_name, test_size, False)
    main_time.finish()