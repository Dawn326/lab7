import unittest
from LifeGameUI import LifeGameUI
from LifeGame import LifeGame
import random
import numpy


class GameTest(unittest.TestCase):
    # 开始测试标志
    def setUp(self):
        self.lifeGame = LifeGameUI(100,100)
        print("start test")

    # 测试游戏开始
    def test_start(self):
        self.assertEqual(self.lifeGameUI.start(), 1, "error")

    #测试游戏暂停
    def test_pause(self):
        self.assertEqual(self.lifeGameUI.pause(), 0, "error")

    # 测试LifeGameUI界面重置
    def test_reset_LifeGameUI(self):
        for i in range(10):
            for j in range(10):
                self.lifeGameUI.frame.GameMap[i][j] = 1
        self.lifeGameUI.reset()
        for i in range(10):
            for j in range(10):
                self.assertEqual(self.lifeGameUI.frame.GameMap[i][j], 0, "error")

    # 测试获取单个细胞周围存活细胞数
    def test_get_neighbor(self):
        lifeGame = LifeGame(100, 100)
        for i in range(0, 3):
            for j in range(0, 3):
                lifeGame.GameMap[i][j] = 1
        # 本格子以及周围格子设置为1
        num = 8  # 总活细胞数目
        for i in range(0, 3):
            for j in range(0, 3):
                # 检测周围或者数量是否为相应数字
                self.assertEqual(lifeGame.get_neighbor(1, 1), num, "error")
                lifeGame.GameMap[i][j] = 0
                if i == 1 and j == 1:
                    continue
                num -= 1

    # 测试count计数功能
    def test_count(self):
        lifeGame = LifeGame(100, 100)
        for i in range(5, 10):
            for j in range(2, 6):
                lifeGame.GameMap[i][j] = 1
        self.assertEqual(lifeGame.get_count(), 20, "error")

    # 测试改变单个细胞状态
    def test_change_status(self):
        n = 5  # 进行了几次单细胞状态测试
        lifeGame = LifeGame(100, 100)
        for i in range(10):
            for j in range(10):
                lifeGame.GameMap[i][j] = 1
        lifeGame.change_status(1, 1)
        self.assertEqual(lifeGame.NextMap[1][1], 0, "error")  # 死亡

        # lifeGame.GameMap[0][0] = 1
        # lifeGame.GameMap[0][1] = 1
        # lifeGame.GameMap[0][2] = 0
        # lifeGame.GameMap[1][0] = 1
        # lifeGame.GameMap[1][2] = 0
        # lifeGame.GameMap[2][0] = 0
        # lifeGame.GameMap[2][1] = 0
        # lifeGame.GameMap[2][2] = 0
        # lifeGame.change_status(1, 1)
        # self.assertEqual(lifeGame.NextMap[1][1], 1, "error")  # 一定活

        # lifeGame.GameMap[0][0] = 1
        # lifeGame.GameMap[0][1] = 0
        # lifeGame.GameMap[0][2] = 0
        # lifeGame.GameMap[1][0] = 1
        # lifeGame.GameMap[1][2] = 0
        # lifeGame.GameMap[2][0] = 0
        # lifeGame.GameMap[2][1] = 0
        # lifeGame.GameMap[2][2] = 0
        # lifeGame.GameMap[1][1] = 1
        # lifeGame.change_status(1, 1)
        # self.assertEqual(lifeGame.NextMap[1][1], 1, "error")  # 不变

        # lifeGame.GameMap[0][0] = 1
        # lifeGame.GameMap[0][1] = 0
        # lifeGame.GameMap[0][2] = 0
        # lifeGame.GameMap[1][0] = 1
        # lifeGame.GameMap[1][2] = 0
        # lifeGame.GameMap[2][0] = 0
        # lifeGame.GameMap[2][1] = 0
        # lifeGame.GameMap[2][2] = 0
        # lifeGame.GameMap[1][1] = 0
        # lifeGame.change_status(1, 1)
        # self.assertEqual(lifeGame.NextMap[1][1], 0, "error")  # 不变

        for time in range(0, n):
            livenum = 9  # 最初生成的活细胞数目
            for i in range(0, 3):
                for j in range(0, 3):
                    if (random.randint(0, 3) % 2 == 1):
                        lifeGame.GameMap[i][j] = 0
                        livenum -= 1
            if lifeGame.GameMap[1][1] == 1:
                if livenum == 3 or livenum == 4:
                    self.assertEqual(lifeGame.NextMap[1][1], 1, "error")  # 不变
                else:
                    self.assertEqual(lifeGame.NextMap[1][1], 0, "error")  # 变
            elif lifeGame.GameMap[1][1] == 0:
                if livenum == 2 or livenum == 3:
                    self.assertEqual(lifeGame.NextMap[1][1], 0, "error")  # 不变
                else:
                    self.assertEqual(lifeGame.NextMap[1][1], 1, "error")  # 变

        # 边界测试
        lifeGame.GameMap[99][99] = 1
        lifeGame.GameMap[0][99] = 0
        lifeGame.GameMap[1][99] = 0
        lifeGame.GameMap[99][0] = 1
        lifeGame.GameMap[1][0] = 0
        lifeGame.GameMap[99][1] = 0
        lifeGame.GameMap[0][1] = 1
        lifeGame.GameMap[1][1] = 0
        lifeGame.change_status(0, 0)
        self.assertEqual(lifeGame.NextMap[0][0], 0, "error")  # 变了0

        lifeGame.GameMap[99][99] = 1
        lifeGame.GameMap[0][99] = 0
        lifeGame.GameMap[1][99] = 0
        lifeGame.GameMap[99][0] = 1
        lifeGame.GameMap[1][0] = 0
        lifeGame.GameMap[99][1] = 0
        lifeGame.GameMap[0][1] = 1
        lifeGame.GameMap[1][1] = 1
        lifeGame.change_status(0, 0)
        self.assertEqual(lifeGame.NextMap[0][0], 1, "error")  # 不变1

    # 测试全部细胞状态更新
    def test_next_phrase(self):
        lifeGame = LifeGame(100, 100)
        lifeGame.GameMap[0][0] = 1
        lifeGame.GameMap[0][1] = 1
        lifeGame.GameMap[0][2] = 1
        lifeGame.GameMap[1][0] = 1
        lifeGame.GameMap[1][2] = 1
        lifeGame.GameMap[2][0] = 1
        lifeGame.GameMap[2][1] = 1
        lifeGame.GameMap[2][2] = 1
        lifeGame.game_update()
        self.assertEqual(lifeGame.GameMap[0][0], 1, "error")
        self.assertEqual(lifeGame.GameMap[1][1], 0, "error")

    # 将所有单元格置为1l检测清空函数是否正常进行。如果正常运行，则应该数组全为0
    def test_reset(self):
        lifeGame = LifeGame(100, 100)
        for i in range(100):
            for j in range(100):
                lifeGame.GameMap[0][0] = 1
        lifeGame.reset()
        for i in range(100):
            for j in range(100):
                self.assertEqual(lifeGame.GameMap[i][j], 0, "error")

    def tearDown(self):
        print("tear down")


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(GameTest("test_start"))  # 测试游戏开始
    suite.addTest(GameTest("test_pause"))  # 测试游戏暂停
    suite.addTest(GameTest("test_get_neighbor"))  # 测试 获取该方格周边存活数量
    suite.addTest(GameTest("test_count"))  # 测试count功能
    suite.addTest(GameTest("test_change_status"))  # 测试 改变该方格存活状态
    suite.addTest(GameTest("test_next_phrase"))  # 测试 改变全部方格状态
    suite.addTest(GameTest("test_reset"))  # 测试 重置内部数组
    suite.addTest(GameTest("test_reset_LifeGameUI"))  # 测试 重置棋盘

    runner = unittest.TextTestRunner()
    runner.run(suite)