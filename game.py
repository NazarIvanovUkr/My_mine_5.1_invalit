from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from mobs import Mobs


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # создаём карту
        self.land = Mapmanager()
        x, y = self.land.loadLand("land.txt")

        # создаём героя
        self.hero = Hero((x // 2, y // 2, 4), self.land)

        # создаём моба (для примера один моб в центре)
        self.mob = Mobs((x // 2, y // 2, 4), self.land, hp=100, speed=1.5)

        base.camLens.setFov(90)

        # обновляем мобов каждый кадр
        taskMgr.add(self.update, "update_mobs")

    def update(self, task):
        dt = globalClock.getDt()
        self.mob.update(dt)
        return task.cont


game = Game()
game.run()
