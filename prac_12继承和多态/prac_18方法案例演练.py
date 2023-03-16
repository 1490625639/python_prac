class Game:
    top_score=0
    def __init__(self,play_name):
        self.play_name=play_name
    #静态方法   显示帮助
    @staticmethod
    def show_help():
        print("不能让僵尸走进房间")
    #类方法 显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("显示历史最高分复习连接符和占位符",cls.top_score)
    #实例方法  开始游戏
    def study_game(self):
        print("游戏开始了")
        print("%s玩的不错"%self.play_name)
        Game.top_score+=100

#查看帮助信息
Game.show_help()
#显示历史最高分
Game.show_top_score()
#创建实例对象
xiaoming=Game("小明")
# 调用实例方法
xiaoming.study_game()
# 调用类方法
Game.show_top_score()
