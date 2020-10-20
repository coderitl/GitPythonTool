import os
'''
问题分析:
    1. 先克隆远程仓库
    2. 进入本地克隆的远程仓库文件夹
    3. 初始化仓库 git init 
    4. 文件的添加 -- > git add .
    5. 关联远程仓库并添加日志信息 git commit -m "日志信息"
    6. 推送至远程
'''
# 克隆仓库
def clone_Repository():
    try:
        # 输入远程仓库地址
        clone_Re = input('请您先克隆您的仓库(请输入仓库地址): ')
        # 通过 os.system 执行 git clone 远程仓库地址
        os.system('git clone {}'.format(clone_Re))
    except:
        print('文件夹存在')

# 初始化仓库
def init_Repository():
    try:
        os.system('git init')
        os.system('git add --all')
        os.system('git commit -m "{}"'.format(input('请输入你的提交日志信息: ')))
        os.system('git branch -M main')
        os.system('git remote add origin {}'.format(input('请输入您的仓库地址: ')))
        os.system('git push -u origin main')
    except:
        print('执行过程中存在错误请检查·················')

def pushExis():
    os.system('git add --all')
    os.system('git commit -m "{}"'.format(input('请输入你的提交日志信息: ')))
    os.system('git remote add origin {}'.format(input('请输入你的仓库地址: ')))
    os.system('git branch -M main')
    os.system('git push -u origin main -f')
def main():
    # 判断仓库是否存在
    isSaveRepository = input(" 克隆仓库-> clone 本地初始化提交-> init  or 文件更新提交-> update: ")
    if isSaveRepository == 'init':
        init_Repository()
    elif isSaveRepository =='update':
        pushExis()
    elif  isSaveRepository =='clone':
        # 1. 克隆远程仓库
        clone_Repository()
    else:
        print('您的输入有误,本次运行已终止·················')
        
if __name__ == '__main__':
    main()