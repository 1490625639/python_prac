# 导包

import unittest
# 2实例化对象并添加测试用例
# unittest.TestLoader().discover(‘用例所在的路径’，‘用例的代码文件名’)
# 用例所在的路径，建议使用相对路径，用例的代码文件名，可以使用*（任意多个字符）通配符，

suite=unittest.TestLoader().discover('./case', 'ts*.py')
#3 实例化运行对象
runer=unittest.TextTestRunner()
#4 执行
runer.run(suite)
# 3 4可以合二为一


